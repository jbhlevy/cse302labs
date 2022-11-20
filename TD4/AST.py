"""
This file contains the implementation of the class structure used to convert from
BX -> ast.json
ast.json -> tac.json
Every instance inherits from the most basic Node class. 
When then distinguish two types of classes, Expressions and Statements. 
Classes implementation is described as they appear in the file. 
"""
# =========== Table used in BX --> AST convrsion ==================

binop_table = {
    "+": "addition",
    "-": "substraction",
    "*": "multiplication",
    "/": "division",
    "%": "modulus",
    "&": "bitwise-and",
    "|": "bitwise-or",
    "^": "bitwise-xor",
    ">>": "logical-shift-right",
    "<<": "logical-shift-left",
}


# =========== Table used in AST --> TAC convrsion =================
op_codes = {'+': 'add',
            '-': 'sub',
            '*': 'mul',
            '/': 'div',
            '%': 'mod',
            '^': 'xor',
            '|': 'or',
            '&': 'and',
            '~': 'not',
            '-.': 'neg',
            '<<':'shl',
            '>>':'shr',
            '==': 'je',
            '!=': 'jnz',
            '<': 'jl',
            '<=': 'jle',
            '>': 'jg',
            '>=': 'jge'}

# ================================================================================

import enum

# Type class used when performing type checking between int or booleans. 
class Type(enum.Enum):

  INT  = enum.auto()
  BOOL = enum.auto()
  VOID = enum.auto()

  def __str__(self):
    if self == Type.INT:
      return "int"
    if self == Type.BOOL:
      return "bool"
    if self == Type.VOID:
        return "void"
    raise ValueError

# Global variables used to track all program variables 
lvars = []
lvars_line = {}

def restore():
    #Function to reset global variables
    global lvars, lvars_line
    lvars = []
    lvars_line = {}

# ================================================================================
# Base Node Class 
class Node:
    vardecls = {}
    fname = ''

    def __init__(self, sloc):
        self.sloc = sloc

    def lookup_variable_type(self, var, var_types):
        #print("TYPE CHECKING IS BACK:", var_types[0])
        for scope in reversed(var_types):
            if var in scope:
                return scope[var]
        raise ValueError(f'Variable {var} not in scope at line {self.sloc.lineno}')


class Expression(Node):
    def __init__(self, sloc):
        super().__init__(sloc)

class ExpressionVar(Expression):
    def __init__(self, sloc, name, type):
      super().__init__(sloc)
      self.name = name
      self.type = type

    def type_check(self, var_types):
        var_type = self.lookup_variable_type(self.name, var_types)
        self.type = var_type

    def syntax_check(self, fname):
        pass

    @property
    def js_obj(self):
        return {'tag': 'Variable', 'type': self.type, 'name': self.name}


    @property
    def expr_to_json(self):
        return [
            '<expression:var>',
            {
                "position": {},
                "name": [
                    "<name>",
                    {
                        "position": {
                            "start": [],
                            "end": []
                        },
                    "value": self.name
                    }
                ]
            }
        ]

class ExpressionInt(Expression):
    def __init__(self, sloc, value):
        super().__init__(sloc)
        self.value = value
        self.type = Type.INT

    def type_check(self, var_types):
        pass

    def syntax_check(self, fname):
        pass

    @property
    def js_obj(self):
        return {'tag': 'Integer', 'value': str(self.value)}


    @property
    def expr_to_json(self):
        return [
            "<expression:int>",
            {
                "position": {
                    "start": [],
                    "end": []
                },
                "value": self.value
            }
        ]

class ExpressionUniOp(Expression):
    def __init__(self, sloc, operator, argument):
        super().__init__(sloc)
        assert isinstance(operator, str), operator
        self.operator = operator
        self.argument = argument

    def type_check(self, var_types):
        self.argument.type_check(var_types)

        if self.operator in {'-.', '~', '!'} and (self.argument.type == Type.INT ): 
            self.type = Type.INT
        elif self.operator in {'!'} and (self.argument.type == Type.BOOL ): 
            self.type = Type.BOOL
        elif self.operator in {'-.', '~',} and (self.argument.type == Type.BOOL ):
            self.type = Type.INT
        else:
            raise TypeError(f'Operator {self.operator} not defined for argument {self.argument} with type {self.argument.type} at line {self.sloc.lineno}')

    def syntax_check(self, fname):
        self.argument.syntax_check(fname)

    @property
    def js_obj(self):
        return {'tag': 'UniOp',
                'op': self.operator,
                'arg': self.argument}


    @property
    def expr_to_json(self):
        return [
            "<expression:uniop",
            {
                "position": {
                    "start": [],
                    "end": []
                },
                "operator": [
                    "<name>",
                    {
                        "position": {
                            "start": [],
                            "end": []
                        },
                        "value": self.operator
                    }
                ],
                "argument": self.argument.expr_to_json
            }
        ]

class ExpressionBinOp(Expression):
    def __init__(self, sloc, operator, left, right):
      super().__init__(sloc)
      assert isinstance(operator, str), operator
      self.operator = operator
      self.left = left
      self.right = right

    def __str__(self):
        s = f"ExpressionBinOp object \n \
            Operator is: {self.operator},\n \
            LHS is: {self.left}\n \
            RHS is: {self.right} \
            "
        return s

    def type_check(self, var_types):
        self.left.type_check(var_types)
    
        if self.operator in {'+', '-', '*', '/',
                       '%', '&', '|', '^',
                       '<<', '>>',} and (self.left.type == Type.INT ): self.type = Type.INT
        elif self.operator in {'==', '!=','<', '<=', '>', '>='} and (self.left.type == Type.INT): 
            self.type = Type.BOOL
        elif self.operator in {'&&', '||', '=='} and (self.left.type == Type.BOOL): self.type = Type.BOOL
        else:
            raise TypeError(f'Operator {self.operator} not defined for argument {self.left} with type {self.left.type} at line {self.sloc.lineno}')

        self.right.type_check(var_types)
        if self.operator in {'+', '-', '*', '/','%', '&', '|', '^','<<', '>>',} and (self.right.type == Type.INT ):
            self.type = Type.INT
        elif self.operator in {'==', '!=','<', '<=', '>', '>='} and (self.right.type == Type.INT): 
            self.type = Type.BOOL
        elif self.operator in {'&&', '||', '=='} and (self.right.type == Type.BOOL): 
            self.type = Type.BOOL
        else:
            raise TypeError(f'Operator {self.operator} not defined for argument {self.right} with type {self.right.type} at line {self.sloc.lineno}')


    def syntax_check(self, fname):
      self.left.syntax_check(fname)
      self.right.syntax_check(fname)

    @property
    def js_obj(self):
      return {'tag': 'BinOp',
              'op': self.operator,
              'larg': self.left,
              'rarg': self.right,
              }

    @property
    def expr_to_json(self):
        return [
            "<expression:binop>",
            {
                "position": [],
                "operator": [
                    "<name>",
                    {
                        "position": {},
                        "value": binop_table[self.operator]
                    }
                ],
                "left": self.left.expr_to_json,
                "right": self.right.expr_to_json
            }
        ]

class Bool(Expression):
    def __init__(self, sloc, value: bool):
        super().__init__(sloc)
        self.value = 1 if value else 0
        self.type = Type.BOOL

    def type_check(self, var_types):
        pass

    def syntax_check(self, fname):
        pass

    @property
    def js_obj(self):
        return {'tag': 'Bool',
                'value': 1 if self.value else 0}

    @property
    def expr_to_json(self):
        pass

    def __str__(self):
        return f"\nA Bool expression with value {self.value}, and type {self.type}"


class Statement(Node):
    def __init__(self, sloc):
        super().__init__(sloc)

    def type_check(self, var_types):
        pass

class Block(Statement):
    def __init__(self, sloc, stmts):
        super().__init__(sloc)
        self.stmts = stmts
        for i in range(len(self.stmts)):
            if isinstance(self.stmts[i], list): 
                offset = len(self.stmts[i])
                for stmt in reversed(self.stmts[i]):
                    self.stmts.insert(i, stmt)
                self.stmts.pop(i+offset)


    def type_check(self, var_types):
        var_types.append(dict())
        for stmt in self.stmts:
            stmt.type_check(var_types)
        #leaving scope
        var_types.pop()

    def syntax_check(self, fname):
        for stmt in self.stmts:
            stmt.syntax_check(fname)

    def check_path(self, proc_type):
        rets = []
        if self.stmts != []:
            for stmt in self.stmts:
                if isinstance(stmt, While):
                    rets += stmt.check_path(proc_type)
                if isinstance(stmt, IfElse):
                    rets += stmt.check_path(proc_type)
            if isinstance(self.stmts[-1], Return):
                if self.stmts[-1].expression.type != proc_type:
                    raise TypeError(f"Invalid return statement has expression of type {self.stmts[-1].expression.type} at line {self.stmts[-1].sloc.lineno}")
                rets += [self.stmts[-1]]
            else: raise SyntaxError(f"Expected return statement in block at line {self.sloc.lineno} but got none")
        else: 
            raise SyntaxError(f"Expected return statement in block at line {self.sloc.lineno} but got none")
        return rets

    def check_no_path(self):
        for stmt in self.stmts:
            if isinstance(stmt, While):
                stmt.check_no_path()
            if isinstance(stmt, IfElse):
                stmt.check_no_path()
            if isinstance(stmt, Return) and stmt.expression is not None:
                raise SyntaxError(f"Found invalid return statement in subroutine block at line {self.sloc.lineno}")

    @property
    def js_obj(self):
        return {'tag': 'Block',
                'stmts': [stmt.js_obj for stmt in self.stmts]}

    @property
    def statement_to_json(self):
        return [stmt.statement_to_json for stmt in self.stmts]


class Vardecl(Statement):
    def __init__(self, sloc, var, expr, type):
        super().__init__(sloc)
        self.var = var
        self.expr = expr
        self.type = type 

    def type_check(self, var_types, glob=False):
        if self.type != Type.INT and self.type != Type.BOOL:
            raise TypeError(f'Variable of dissalowed type:{self.type}')
        self.expr.type_check(var_types)
        if glob:
            if self.type == Type.INT:
                if isinstance(self.expr, ExpressionUniOp) and (self.expr.operator == '-.' and self.expr.type == Type.INT):
                    pass
                else:
                    if not isinstance(self.expr, ExpressionInt):
                        raise ValueError(f"Declaration of global variable of type int can only be to an integer value")
            if self.type == Type.BOOL:
                if not isinstance(self.expr, Bool):
                    raise ValueError(f"Declaration of global variable of type bool can only be to a boolean value")
        if self.expr.type != self.type:
            raise TypeError(f'assignement has wrong type, expected {self.type} and got {self.expr.type}')
        if self.var.name in var_types[-1]:
          raise ValueError(f'Variable {self.var.name} already declared at line {self.sloc.lineno}')
        var_types[-1][self.var.name] = self.var.type


    def syntax_check(self, fname):
      global lvars
      if self.var.name in lvars:
          raise ValueError(f'{fname}:line {self.sloc.lineno}:Error:Another declaration of variable "{self.var.name}"\n'f'{fname}:line {declarations_line[self.var.name]}:Info:Earlier declaration of "{self.var.name}"')
      lvars.append(self.var.name)
      lvars_line[self.var.name] = self.sloc

    @property
    def js_obj(self):
        return {'tag': 'Vardecl',
                'var': self.var,
                'init': self.expr.js_obj}


    @property
    def statement_to_json(self):
        return [
            "<statement:vardecl",
            {
                "position": {
                    "start": [],
                    "end": []
                },
                "name": [
                    "<name>",
                    {
                        "position": {
                            "start": [],
                            "end": []
                        },
                        "value": self.var.name
                    }
                ],
                "type": [
                    "<type:int>",
                    {
                        "position": {
                            "start": [],
                            "end": []
                        }
                    }
                ],
                "init": self.expr.expr_to_json
            }
        ]

class Assign(Statement):
    def __init__(self, sloc, lhs :ExpressionVar, rhs :Expression):
        super().__init__(sloc)
        self.lhs = lhs
        self.rhs = rhs

    def type_check(self, var_types):
        var_type = self.lookup_variable_type(self.lhs.name, var_types)
        self.rhs.type_check(var_types)
        if var_type != self.rhs.type:
            raise TypeError(f"Assignment of variable '{self.lhs.name}' of type '{var_type}' to expr of type '{self.rhs.type}' at line {self.sloc.lineno}")

    def syntax_check(self, fname):
        self.lhs.syntax_check(fname)
        self.rhs.syntax_check(fname)

    @property
    def js_obj(self):
        return {'tag': 'Assign',
        'lhs': self.lhs.js_obj,
        'rhs': self.rhs.js_obj}

    @property
    def statement_to_json(self):
        return [
            "<statement:assign>",
            {
                "position": {
                    "start": [],
                    "end": []
                },
                "lvalue": [
                    '<lvalue:var>',
                    {
                        "position": {},
                        "name": [
                            "<name>",
                            {
                                "position": {
                                    "start": [],
                                    "end": []
                                },
                            "value": self.lhs.name
                            }
                        ]
                    }
                ],
                "rvalue": self.rhs.expr_to_json
            }
        ]

class Print(Statement):
    def __init__(self, sloc, arg :Expression):
        super().__init__(sloc)
        self.arg = arg

    def type_check(self, var_types):
        self.expr.type_check(var_types)
        if self.expr.type != 'int':
            raise TypeError(f'Can only print INT, not {self.expr.type}, at line {self.sloc}')

    def syntax_check(self, fname):
      self.arg.syntax_check(fname)

    @property
    def js_obj(self):
        return {'tag': 'Print', 'arg': self.arg.js_obj}


    @property
    def statement_to_json(self):
        return [
            "<statement:eval>",
            {
                "position": {
                    "start": [],
                    "end": []
                },
                "expression": [
                    "<expression:call>",
                    {
                        "position": {
                            "start": [],
                            "end": []
                            },
                            "target": [
                                "<name>",
                                {
                                    "position": {
                                        "start": [],
                                        "end": []
                                    },
                                    "value": "print"
                                }
                            ],
                        "arguments": [self.arg.expr_to_json]
                    }
                ]
            }
        ]


class IfElse(Statement):
    def __init__(self, sloc, condition: Expression, block: Block, ifrest):
        super().__init__(sloc)
        if ifrest is not None:
            assert isinstance(ifrest, (Block, IfElse))
        self.condition = condition  #to enter the block
        self.block = block          #list of statements
        self.ifrest = ifrest        #else blocks

    def type_check(self, var_types):
        #ar_types[-1]["loop"] = True
        self.condition.type_check(var_types)
        if self.condition.type != Type.BOOL:
            raise TypeError(f'IfElse cannot be of type {self.condition.type} at line {self.sloc},  must be of type bool')
        self.block.type_check(var_types)
        if self.ifrest is not None:
            self.ifrest.type_check(var_types)

    def syntax_check(self, fname):
        self.block.syntax_check(fname)
        self.ifrest.syntax_check(fname)

    def check_path(self, proc_type):
        if self.ifrest is None :
            return self.block.check_path(proc_type)
        else: 
            tmp = self.block.check_path(proc_type) 
            tmp += self.ifrest.check_path(proc_type)
            return tmp

    def check_no_path(self):
        self.block.check_no_path()
        if self.ifrest is not None:
            self.ifrest.check_no_path()

    @property
    def js_obj(self):
        return {'tag': 'IfElse',
                'condition': self.condition.js_obj,
                'block': self.block.js_obj,
                'ifrest': self.ifrest.js_obj}

class While(Statement):
    def __init__(self, sloc, condition: Expression, block: Block):
        super().__init__(sloc)
        self.condition = condition
        self.block = block

    def type_check(self, var_types):
        var_types[-1]["loop"] = True
        self.condition.type_check(var_types)
        if self.condition.type != Type.BOOL:
            raise TypeError(f'WHILE cannot be of type {self.condition.type} at line {self.sloc}, must be of type BOOL')
        self.block.type_check(var_types)

    def syntax_check(self, fname):
        self.block.syntax_check(fname)

    def check_path(self, proc_type):
        return self.block.check_path(proc_type)
    
    def check_no_path(self):
        self.block.check_no_path()

    @property
    def js_obj(self):
        return {'tag': 'While',
                'condition': self.condition.js_obj,
                'stmts': self.block.js_obj}

    @property
    def statement_to_json(self):
        pass

class Jump(Statement):
    def __init__(self, sloc, operator: str):
        super().__init__(sloc)
        self.operator = operator

    def type_check(self, var_types):
        for scope in reversed(var_types):
            if ('loop', True) in scope.items():
                return 
        raise SyntaxError(f"Jump statement {self.operator} used outside of loop body")

    def syntax_check(self, fname):
        pass

    @property
    def js_obj(self):
        return {'tag': self.operator.capitalize()}

    @property
    def statement_to_json(self):
        pass

class Eval(Statement):
    def __init__(self, sloc, expression):
        super().__init__(sloc)
        self.expression = expression

    def type_check(self, var_types):
        self.expression.type_check(var_types)

class Call(Expression):
    def __init__(self, sloc, name, args):
        super().__init__(sloc)
        self.name = name
        self.args = args
    
    def type_check(self, var_types):
        if self.name == "print":
            for arg in self.args:
                arg.type_check(var_types)
            if self.args[0].type is Type.INT:
                self.name = "__bx_print_int"
            elif self.args[0].type is Type.BOOL:
                self.name = "__bx_print_bool"
            self.type = Type.VOID
        else:
            self.type = self.lookup_variable_type(self.name, var_types)
            if self.args != []:
                #print(self.args)
                for arg in self.args:
                    arg.type_check(var_types)

class Return(Statement):
    def __init__(self, sloc, operator: str, expression: Expression = None):
        super().__init__(sloc)
        self.operator = operator, 
        self.expression = expression

    def type_check(self, var_types):
        if self.expression is not None: 
            self.expression.type_check(var_types)

class ProcDecl(Node):
    def __init__(self, sloc, name : str, params: list, block: Block, ty: Type = None):
        super().__init__(sloc)
        self.params = params
        self.block = block
        self.name = name
        self.type = Type.VOID if ty == None else ty
        self.rets = []


    def __str__(self):
        return f"Procedure: @{self.name}\n \
        Type : {self.type}, return expr type: {self.rets} \n \
        params : {self.params} \n \
        block : {self.block.stmts}"
    
    def add_param_to_scope(self, p, var_types):
            var_types[-1][p.name] = p.type


    def check_path(self):
        return self.block.check_path(self.type)

    def check_no_path(self):
        self.block.check_no_path()

    def type_check(self, var_types):
        if self.name == "main" and self.type is not Type.VOID:
            raise TypeError(f"Subroutine @main must return void value")


        var_types.append(dict())
        for param in self.params:
            for p in param:
                self.add_param_to_scope(p, var_types)
        self.block.type_check(var_types)


        if self.type != Type.VOID:
            self.rets = self.check_path()
        else:
            self.check_no_path()
        var_types = var_types[:-1]

class Program(Node):
  def __init__(self, sloc, decls):
    super().__init__(sloc)
    self.global_vars = []
    self.procs = []

    def are_global(decl):
        res = True
        for v in decl:
            if not isinstance(v, Vardecl):
                res = False
        return res

    for decl in decls:
        if isinstance(decl, list):
            if are_global(decl):
                for v in decl:
                    self.global_vars.append(v)
        elif isinstance(decl, Vardecl): self.global_vars.append(decl)
        elif isinstance(decl, ProcDecl):
            self.procs.append(decl)
    
    


  def type_check(self, var_scopes):
    var_scopes.append(dict())
    #Global var type checking
    for var in self.global_vars:
        var.type_check(var_scopes, True)

    names = []
    #Proc type checking 
    for proc in self.procs:
        names.append(proc.name)
        if proc.name in var_scopes[0].keys():
            raise SyntaxError(f"Procedure {proc.name} already declared")
        var_scopes[0][proc.name] = proc.type
    for proc in self.procs:
        proc.type_check(var_scopes)
    
    if 'main' not in names:
        raise SyntaxError(f"Subroutine @main not found in file")


  def syntax_check(self, fname):
    self.block.syntax_check(fname)

  @property
  def js_obj(self):
    return {'tag': 'Program',
            'vars': self.lvars,
            'block': self.block[0].js_obj}

  @property
  def prog_to_json(self):
    return [self.block.statement_to_json]
