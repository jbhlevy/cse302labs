import argparse
import json
import sys
import AST as ast

tmp_counter = -1
temporaries = []
instructions = []
temporaries_table = {}

all_vars = []

def json_to_name(js_obj):
    """
    Function to obtain the string format of the name of a JSON object
    """
    return js_obj[1]['value']
# ============ Class for Instructions ===================

class Instruction:
    def __init__(self, opcode, args, result) -> None:
        self.opcode = opcode
        self.args = args
        self.result = result

    @property
    def js_obj(self):
        return {'opcode': self.opcode,
            'args': self.args,
            'result': self.result}

# ===================================

def add_instruction(opcode, args, result):
    """
    Useful function to add an instance of class Instruction to the gloabl list of instructions
    """
    instructions.append(Instruction(opcode, args, result))


# ========== Allocating and managing temporaries ========

def fresh_temp():
    """
    Function to create a 'new' temporary (that has never been used before)
    """
    global tmp_counter 
    tmp_counter += 1
    temp = f"%{tmp_counter}"
    temporaries.append(temp)
    return temp

def check_temp_table(var):
    """
    Function to check if the variable being worked on is already stored in a temporary
    """
    current_temp = temporaries_table.get(var)
    if current_temp is None:
        current_temp = fresh_temp()
        temporaries_table[var] = current_temp
    return current_temp

# =============== Dealing with program variables  ========== 
# def var_to_temps(all_vars):
#     """
#     Function to generate all var declaration instructions
#     """
#     opcode = "const"
#     args = [0]
#     result = "%0"
#     for var in all_vars:
#         #operate on args (to bee able to initiate to smth else than 0)
#         result = check_temp_table(var.left.name)
#         instructions.append(Instruction(opcode, args, result))

"""
The following will be used if the user specified the -tmm option when calling the program at the command line 
It is also set to be the default option.
"""

#=============== Dealing with program expressions (TMM)  ==========

def expressions_tmm(expr, target):
    if isinstance(expr, ast.ExpressionVar):
        tmp = check_temp_table(expr.name)
        instructions.append(Instruction("copy", [tmp] , target))
    elif isinstance(expr, ast.ExpressionInt):
        instructions.append(Instruction("const", [expr.value], target))
    elif isinstance(expr, ast.ExpressionUniOp):
        arg_target = fresh_temp()
        expressions_tmm(expr.argument, arg_target)
        instructions.append(Instruction(ast.uniop_map[expr.operator], [arg_target], target))
    elif isinstance(expr, ast.ExpressionBinOp):
        args = []
        for arg in expr.arguments:
            #print("arg:", arg)
            arg_target = fresh_temp()
            expressions_tmm(arg, arg_target)
            args.append(arg_target)
        instructions.append(Instruction(ast.binop_map[expr.operator], args, target))
    elif isinstance(expr, ast.ExpressionCall):
        pass
    else:
        ValueError(f'tmm statement: unknown statement kind: {expr.__class__}')

# =============== Dealing with program statments (TMM)  ========== 

def statements_tmm(statements):
    for stmt in statements:
        if isinstance(stmt, ast.VarAssignement):
            lhs = check_temp_table(stmt.left.name)
            expressions_tmm(stmt.right, lhs)
        elif isinstance(stmt, ast.Eval):
            if stmt.name == "print":
                tmp = fresh_temp()
                expressions_tmm(stmt.arguments, tmp)
                instructions.append(Instruction("print", [tmp], None))
        elif isinstance(stmt, ast.VarDecl):
            result = check_temp_table(stmt.name)
            args = stmt.value.value
            add_instruction("const", [args], result)
        else:
            raise ValueError(f'tmm statement: unknown statement kind: {stmt.__class__}')


"""
The following will be used if the user specified the -bmm option when calling the program at the command line 
"""

#=============== Dealing with program expressions (BMM)  ==========

def expressions_bmm(expr):
    if isinstance(expr, ast.ExpressionVar):
        tmp = check_temp_table(expr.name)
        return tmp
    elif isinstance(expr, ast.ExpressionInt):
        target = fresh_temp()
        add_instruction("const", [expr.value], target)
        return target
    elif isinstance(expr, ast.ExpressionUniOp):
        arg = expressions_bmm(expr.argument)
        target = fresh_temp()
        add_instruction(ast.uniop_map[expr.operator], [arg], target)
        return target
    elif isinstance(expr, ast.ExpressionBinOp):
        args = []
        for arg in expr.arguments:
            #print("arg:", arg)
            arg_ = expressions_bmm(arg)
            args.append(arg_)
            target = fresh_temp()
        add_instruction(ast.binop_map[expr.operator], args, target)
        return target
    elif isinstance(expr, ast.ExpressionCall):
        pass
    else:
        ValueError(f'tmm statement: unknown statement kind: {expr.__class__}')


# =============== Dealing with program statments (BMM)  ========== 

def statements_bmm(statements):
    for stmt in statements:
        if isinstance(stmt, ast.VarAssignement):
            lhs = check_temp_table(stmt.left.name)
            rhs = expressions_bmm(stmt.right)
            add_instruction("copy", [rhs], lhs)
        elif isinstance(stmt, ast.Eval):
            if stmt.name == "print":
                tmp = expressions_bmm(stmt.arguments)
                instructions.append(Instruction("print", [tmp], None))
        else:
            raise ValueError(f'tmm statement: unknown statement kind: {stmt.__class__}')


# ============================================ End of implementation =======================================================

"""
Part C of the file: Driver Code 
"""

"""
The following block contains top level functions to work from the AST to the classes
The two first functions allow us to strip the JSON input to retain only the AST. 
The other functions are used to obtain a list of all variable declarations and of all statements in the program
"""

# ============ Functions to work on the program ========

def json_strip_ast(js_obj):
    """
    Function to only keep the "ast" field from initial JSON objct
    """
    if "ast" not in js_obj.keys():
        return "ERROR function called on wrong js_obj"
    return js_obj["ast"][0]

def json_to_proc(js_obj):
    """
    Function to remove the top-level procdure (and store some useful info about it)
    """
    if js_obj[0] ==  "<decl:proc>":
        name = js_obj[1]['name'][1]["value"]
        arguments = js_obj[1]['arguments']
        returnType = js_obj[1]['returntype']
        print(f"Found a top level procedure named: {name}")
        print(f"It has input arguments: {arguments}")
        print(f"It has return type: {returnType}")
        print("Will proceed to body evaluation...")
        body = js_obj[1]['body']
        return body, name 

# def json_to_var(js_obj):
#     """
#     Function to handle variable declarations
#     """
#     name = json_to_name(js_obj[1]["name"])
#     #_type = js_obj[1]["type"][0] not used at th moment, maybe in later labs ?
#     value = ast.Expression.json_to_expr(js_obj[1]["init"])
#     return ast.VarAssignement(ast.ExpressionVar(name), value)

# def load_variables(js_obj, vars : list()):
#     """
#     Function to add all variable declarations to a global list
#     """

#     while len(js_obj) > 0:
#         if js_obj[0][0] != "<statement:vardecl>": 
#             break
#         vars.append(json_to_var(js_obj[0]))
#         js_obj = js_obj[1:]
#     return js_obj 

def load_statements(js_obj):
    """
    Function to add all statements in the program to a global list
    """
    statements = []
    while len(js_obj) > 0:
        statement = ast.Statement.json_to_statement(js_obj[0])
        if statement is not None:
            statements.append(statement)
        js_obj = js_obj[1:]
    return statements 

# =============================================

# =========== Write to output file ===========

def write_out(file_name, procedure):
    """
    Function to write obtained JSON object to a file
    """
    filename = file_name[:-8] + '.tac.json'
    print("name:", filename)
    js = procedure.js_obj
    with open(filename, 'w') as out_file:
        json.dump(js, out_file)
    print(f'{filename} -> {filename}')

# =========== TESTING FUNCTIONS ===========

# def check_1(instructions):
#     for instr in instructions:
#         print("ha", instr.js_obj)

# def check2(procedure):
#     print("The obtained JSON file will be:", procedure.js_obj)

# =========== RUNING CODE ===========

def main():
    """
    Driver function
    """
    #Handling arguments for diffrent option flags
    parser = argparse.ArgumentParser(description='Convert AST (JSON format) to TAC (JSON)')
    parser.add_argument("--tmm", dest='tmm', action='store_true', default=False, help='Set flag for top-down maximal munch')
    parser.add_argument("--bmm", dest='bmm', action='store_true', default=False, help='Set flag for bottom-up maximal munch')
    parser.add_argument('fname', metavar='FILE', type=str, nargs=1, help='Th input JSON file')
    args = parser.parse_args(sys.argv[1:])

    if args.tmm and args.bmm:
        raise ValueError('Expcted 1 flag but received 2. Cannot use both --tmm and --bmm')
    #Boolean to handle method picking
    method = 0
    method = 1 if args.bmm else 0
    #Reading whole JSON file once
    input_file = args.fname[0]
    with open(input_file, 'r') as json_file :
        js_object = json.load(json_file) 

    #Removing useless information (all but the AST field)
    ast_object = json_strip_ast(js_object)
    body_object, name = json_to_proc(ast_object)

    #Since there is only on top-level procedur, we kep only the body of AST 
    #body_stripped = load_variables(body_object, all_vars)
    statements = load_statements(body_object)
    top_procedure = ast.Procedure(name) #Procedure(name, statements, location=[])

    #var_to_temps(all_vars)

    if method == 0:
        statements_tmm(statements)
    elif method == 1:
        statements_bmm(statements)
    top_procedure.instructions = instructions   


    write_out(input_file, top_procedure)

    return 0

########################
#ENTRY POINT 
main()

# ========================================= EOF =========================================================================



