import os
import sys
import ply 
import ply.lex as lex 
import ply.yacc as yacc
import AST as ast
import json 

"""
Part A of the file: Lexer
Using some documentation found online: https://www.dabeaz.com/ply/ply.html we encapsulates the lexer in 
our own Lexer class. This is easier in order to manage the different parts of the program
"""
# =========================================================

class Lexer:

    def __init__(self, data):
        """
        name: string representing the file source 
        """
        self.data = data 
        self.lexer = ply.lex.lex(module=self)
        self.lexer.input(self.data)
        #self.endof = False 

    # =========== PLY used variables ======================

    reserved = {
        'print': "PRINT",
        'var': "VAR", 
        'int': 'INT', 
        'def': "DEF",
        'main': "MAIN"
    }

    tokens = ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULUS', 
    'BIT_OR', 'BIT_AND', 'BIT_XOR', 'BIT_LSHIFT', 'BIT_RSHIFT', 'BIT_NEGATION', 
    'LPAREN', 'RPAREN', 'IDENT', 'NUMBER', 
    'SEMICOLON', 'COLON', 'EQ', 'LBRACKET', 'RBRACKET') + tuple(reserved.values())


    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MODULUS = r'%'
    t_BIT_OR = r'\|'
    t_BIT_AND = r'&'
    t_BIT_XOR = r'\^'
    t_BIT_LSHIFT = r'<<'
    t_BIT_RSHIFT = r'>>'
    t_BIT_NEGATION = r'~'
    t_LPAREN = r'\('
    t_LBRACKET = r'{'
    t_RBRACKET = r'}'
    t_RPAREN = r'\)'
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_EQ = r'='

    # ========== PLY token processing code ================

    def t_IDENT(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = Lexer.reserved.get(t.value, 'IDENT')
        return t 

    def t_NUMBER(self, t):
        r'0|[1-9][0-9]*'
        t.value = int(t.value)
        return t

    def t_error(self, t):
        print(f"Illegal character ’{t.value[0]}’ on line {t.lexer.lineno}")
        t.lexer.skip(1)

    def t_newline(self, t):
        r'\n'
        t.lexer.lineno += 1

    def t_whitespace(self, t): 
        r'//.*\n'
        if t.value[-1] == '\n': 
            t.lexer.lineno+=1

    def t_COMMENT(self, t):
        r'//.*'
        t.lexer.lineno += 1
        pass

    t_ignore = ' \t\f\v'

# ============== Error Handling =======================

    def position(self, t):
        line_start = self.data.rfind('\n', 0, t.lexpos) + 1
        return f'line:{t.lineno}, col:{t.lexpos - line_start + 1}'

    def error_message(self, t, msg):
        print(f'{self.position(t)}: Error:{msg}')
        msg = f'{self.position(t)}: Error:{msg}'
        raise SyntaxError(msg)

"""
Part B of the file: Parser
Similar to the Lexer, we encapsulate the PLY parser in our own Parser class
in order to better manage which part of the program is acting on what input
"""

class Parser: 
    def __init__(self, lexer):
        """
        lexer: An object of type Lexer (our class)
        """
        self.lexer = lexer
        self.parser = yacc.yacc(module=self, start='program')

    def parse(self):
        return self.parser.parse(lexer=self.lexer.lexer)

    # =========== PLY used variables ======================
    tokens = Lexer.tokens + ('UMINUS',)

    precedence = (
        ('left', 'BIT_OR'),
        ('left', 'BIT_XOR'),
        ('left', 'BIT_AND'),
        ('left', 'BIT_LSHIFT', 'BIT_RSHIFT'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MODULUS'),
        ('left', 'UMINUS'),
        ('left', 'BIT_NEGATION'),
    )

    # ================== Expressions ======================

    def p_expr_ident(self, p):
        #  p[0]   p[1]
        """expr : IDENT"""
        p[0] = ast.ExpressionVar(p[1], [p.lineno(1), p.lexpos(1)])

    def p_expr_number(self, p):
        #  p[0]   p[1]
        """expr : NUMBER"""
        p[0] = ast.ExpressionInt(int(p[1]), [p.lineno(1), p.lexpos(1)])

    def p_expr_uniop(self, p):
        #  p[0]   p[1]        p[2]
        """expr : BIT_NEGATION expr
                | MINUS expr %prec UMINUS
                | UMINUS expr
        """
        if p[1] == '-': #Handling the UMINUS
            p[1] = '-.'
        p[0] = ast.ExpressionUniOp(p[1], p[2], [p.lineno(1), p.lexpos(1)])

    def p_expr_binop(self, p):
        #  p[0]   p[1] p[2] p[3] 
        """expr : expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDE expr
                | expr MODULUS expr
                | expr BIT_OR expr
                | expr BIT_AND expr 
                | expr BIT_XOR expr
                | expr BIT_LSHIFT expr 
                | expr BIT_RSHIFT expr
        """
        p[0] = ast.ExpressionBinOp(p[2], [p[1], p[3]], [p.lineno(1), p.lexpos(1)])


    def p_expr_parens(self, p):
        #  p[0]   p[1]   p[2] p[3] 
        """expr : LPAREN expr RPAREN"""
        p[0] = p[2]

    # ================== Statements =======================

    def p_stmt(self, p):
        #   p[0]    p[1]  p[2]
        """ stmts : stmts stmt 
                    |"""
        if len(p) == 1:
            p[0] = []
        else:
            p[0] = p[1]
            p[1].append(p[2])

    def p_stmt_decl(self, p):
        #  p[0]  p[1] p[2]  p[3] p[4] p[5] p[6] p[7]
        """stmt : VAR IDENT EQ expr COLON INT SEMICOLON"""
        p[0] = ast.VarDecl(ast.ExpressionVar(p[2], [p.lineno(2), p.lexpos(2)]), p[4], [p.lineno(1), p.lexpos(1)])

    def p_stmt_assign(self, p):
        #  p[0]   p[1] p[2] p[3] p[4]
        """stmt : IDENT EQ expr SEMICOLON"""
        p[0] = ast.VarAssignement(ast.ExpressionVar(p[1], [p.lineno(1), p.lexpos(1)]), 
                                p[3], 
                                [p.lineno(1), p.lexpos(1)])

    def p_stmt_print(self, p):
        #   p[0]   p[1]  p[2]   p[3] p[4]   p[5]
        """ stmt : PRINT LPAREN expr RPAREN SEMICOLON"""
        p[0] = ast.Eval("print", p[3], [p.lineno(1), p.lexpos(1)])

    # ================== Procedures =======================

    def p_program(self, p):
        # p[0]       p[1] p[2] p[3]  p[4]   p[5]     p[6]  p[7] 
        """program : DEF MAIN LPAREN RPAREN LBRACKET stmts RBRACKET"""
        p[0] = ast.Procedure(p[2], p[6], [p.lineno(1), p.lexpos(1)])

    # ================== Error Handling ===================
    def p_error(self, p):
        if not p:
            return 
        p.lexer.lexpos -= len(p.value)
        self.lexer.error_message(p, f'Syntax error while parsing {p.type}')

    def error_message(self, lineno, lexpos, msg):
        token = lex.LexToken()
        token.lineno = lineno
        token.lexpos = lexpos
        token.type = None 
        token.value = None 
        print("token line:", token.lineno)
        self.lexer.error_message(token, msg)


"""
Part C of the file: Program and main 
In order to have a more clear code, we encapsulate the lexing/parsing of an input into 
a Program class that also holds usefull information on the program to be parsed. 
The execution of the script is done via the main function. 
"""

# ================ Class for Programs =====================
class Program:
    def __init__(self, provenance, source, lexer, parser):
        #self.name = filename #To Be Implemented...
        self.provenance = provenance
        self.source = source
        self.lexer = lexer
        self.parser = parser
        self.procedure = self.parser.parse()
        assert self.procedure is not None
        self.procedure.check_syntax(self.parser.error_message)

    @property
    def prog_to_json(self):
        return {
            "provenance": self.provenance, 
            "source": self.source,
            "ast": [self.procedure.proc_to_json]
        }

# ================== Script Functions =====================

def write_out(file_name, prog):
    """
    Function to write obtained JSON object to a file
    """
    save_path = "../examples/json"
    filename = file_name[15:] + '.json'
    complete_name = os.path.join(save_path, filename)
    print("name:", complete_name)
    js = prog.prog_to_json
    with open(complete_name, 'w') as out_file:
        json.dump(js, out_file)
    print(f'{filename} -> {filename}')


def main(test_file=''):
    if len(test_file) !=0:
        input_file = test_file
    else:
        input_file = sys.argv[1]
    
    assert input_file.endswith('.bx')
    with open(input_file, 'r') as bx_file:
        file_string = bx_file.read()


    lexer = Lexer(file_string)
    parser = Parser(lexer)
    prog = Program("<stdin>", file_string, lexer, parser)
    #print(prog.prog_to_json)

    write_out(input_file, prog)

    return 0

# ================== Testing functions =====================
def test1(lexer, test_string):
    lexer.input(test_string)
    for i in range(13):
        print("i:",i,lexer.token())

def test2(lexer, parser, test_string):
    lexer.input(test_string)
    p = parser.parse(lexer=lexer)
    return p.proc_to_json

# =============== Runing Code ===============================

#test1(lexer, test_string)
#p = test2(lexer, parser, test_string)
#print(p)


########################
#ENTRY POINT 
#main() #In order to usee the tester file, please comment out this line

# ========================================= EOF =========================================================================




