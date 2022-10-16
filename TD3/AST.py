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

  def __str__(self):
    if self == Type.INT:
      return "int"
    if self == Type.BOOL:
      return "bool"
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
      #source location
      self.sloc = sloc

  # def syntax_error(self, msg, errfn):
  #   if self.sloc is None:
  #     print('Error:' + msg)
  #   else:
  #     #lexpos : index of the token relative to the start of the input text
  #     lineno, lexpos = self.sloc  #info about the location of the token
  #     errfn(lineno, lexpos, msg)
  #   raise SyntaxError(msg)


class Expression(Node):
    def __init__(self, sloc):
        super().__init__(sloc)

    # @staticmethod
    # def load(js_obj):
    #     if not isinstance(js_obj, list):
    #       return None
    #     if len(js_obj) > 1:
    #       sloc = js_obj[1]
    #     else:
    #       None
    #     if js_obj[0] == '<expression:var>':
    #       return ExpressionVar(sloc, js_obj[1]['name'][1]['value'])
    #     elif js_obj[0] == '<lvalue:var>':
    #       return ExpressionVar(sloc, js_obj[1]['name'][1]['value'])
    #     elif js_obj[0] =='<expression:call>':
    #       return Expression.load(sloc, js_obj[1]['arguments'][0])
    #     elif js_obj[0] == '<expression:int>':
    #       return ExpressionInt(sloc, js_obj[1]['value'])
    #     elif js_obj[0] == '<expression:uniop>':
    #       operator = js_obj[1]['operator'][1]['value']
    #       argument = Expression.load(js_obj[1]['argument'])
    #       return ExpressionUniOp(sloc, operator, argument)
    #     elif js_obj[0] == '<expression:binop>':
    #       operator = js_obj[1]['operator'][1]['value']
    #       left = Expression.load(js_obj[1]['left'])
    #       right = Expression.load(js_obj[1]['right'])
    #       return ExpressionBinOp(sloc, operator, left, right)lexpr.op
    #     else:
    #       return None


class ExpressionVar(Expression):
    def __init__(self, sloc, name, type):
      super().__init__(sloc)
      self.name = name
      self.type = type

    def type_check(self, var_types):
        pass

    def syntax_check(self, fname):
        pass





    #           if self.var.name in var_types[-1]:
    #       raise ValueError(f'Variable {self.var.name} already declared at line {self.sloc}')
    #     self.expr.type_check(var_types)
    #     self.var.ty = self.expr.ty
    #     var_types[-1][self.var.name] = self.var.ty
    #   if self.name not in lvars:
    #      raise ValueError(f'{fname}:line {self.sloc}:Error:Undeclared variable "{self.name}"')

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
        self.type = 'int'

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

        if self.operator in {'PLUS', 'MINUS', 'TIMES', 'DIV',
                       'MODULUS', 'BITAND', 'BITOR', 'BITXOR',
                       'BITSHL', 'BITSHR', 'UMINUS', 'NEG', 'BITCOMPL'
                       } and (self.argument.type == 'int' ):
            self.type = 'int'
        elif self.operator in {'EQ', 'NEQ',
                         'LT', 'LTEQ', 'GT', 'GTEQ'
                         } and (self.argument.type == 'int'):
            self.type = 'bool'
        elif self.operator in {'AND', 'OR', 'NOT'
                         } and (self.argument.type == 'bool'):
            self.type = 'bool'
        else:
            raise TypeError(f'Operator {self.operator} not defined for argument {self.argument} with type {self.argument.type} at line {self.sloc}')

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
        if self.left in {'PLUS', 'MINUS', 'TIMES', 'DIV',
                       'MODULUS', 'BITAND', 'BITOR', 'BITXOR',
                       'BITSHL', 'BITSHR', 'UMINUS', 'NEG', 'BITCOMPL'
                       } and (self.left.type == 'int' ):
            self.type = 'int'
        elif self.left in {'EQ', 'NEQ',
                         'LT', 'LTEQ', 'GT', 'GTEQ'
                         } and (self.left.type == 'int'):
            self.type = 'bool'
        elif self.operator in {'AND', 'OR', 'NOT'
                         } and (self.left.type == 'bool'):
            self.type = 'bool'
        else:
            raise TypeError(f'Operator {self.operator} not defined for argument {self.left} with type {self.left.type} at line {self.sloc}')

        self.right.type_check(var_types)
        if self.right in {'PLUS', 'MINUS', 'TIMES', 'DIV',
                       'MODULUS', 'BITAND', 'BITOR', 'BITXOR',
                       'BITSHL', 'BITSHR', 'UMINUS', 'NEG', 'BITCOMPL'
                       } and (self.right.type == 'int' ):
            self.type = 'int'
        elif self.right in {'EQ', 'NEQ',
                         'LT', 'LTEQ', 'GT', 'GTEQ'
                         } and (self.right.type == 'int'):
            self.type = 'bool'
        elif self.operator in {'AND', 'OR', 'NOT'
                         } and (self.right.type == 'bool'):
            self.type = 'bool'
        else:
            raise TypeError(f'Operator {self.operator} not defined for argument {self.right} with type {self.right.type} at line {self.sloc}')


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
        self.value = value
        self.type = 'bool'

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


class Statement(Node):
    def __init__(self, sloc):
        super().__init__(sloc)

    def type_check(self, var_types):
        pass

    def lookup_variable_type(self, var, var_types):
        for scope in reversed(var_types):
            if var in scope:
                return scope[var]
        raise ValueError(f'Variable {var} not in scope at line {self.sloc}')

#     @staticmethod
#     def load(js_obj):
#         if not isinstance(js_obj, list):
#             return None
#         if len(js_obj) > 1:
#             sloc = js_obj[1]
#         else:
#             sloc = None
#         if js_obj[0] == '<statement:assign>':
#             return Assign(sloc, Expression.load(js_obj[1]['lvalue']), Expression.load(js_obj[1]['rvalue']))
#         elif js_obj[0] == '<statement:eval>':
#             js_obj = js_obj[1]['expression']
#             return Print(sloc, Expression.load(js_obj))
#         else:
#             return None


class Block(Statement):
    def __init__(self, sloc, stmts):
        super().__init__(sloc)
        self.stmts = stmts

    def type_check(self, var_types):
        var_types.append(dict())
        for stmt in self.stmts:
            stmt.type_check(var_types)
        #leaving scope
        var_types = var_types[:-1]

    def syntax_check(self, fname):
        for stmt in self.stmts:
            stmt.syntax_check(fname)

    @property
    def js_obj(self):
        return {'tag': 'Block',
                'stmts': [stmt.js_obj for stmt in self.stmts]}

    @property
    def statement_to_json(self):
        return [stmt.statement_to_json for stmt in self.stmts]


class Vardecl(Statement):
    def __init__(self, sloc, var, expr):
        super().__init__(sloc)
        self.var = var
        self.expr = expr

    def type_check(self, var_types):
        if self.var.name in var_types[-1]:
          raise ValueError(f'Variable {self.var.name} already declared at line {self.sloc}')
        self.expr.type_check(var_types)
        self.var.ty = self.expr.ty
        var_types[-1][self.var.name] = self.var.ty

    def syntax_check(self, fname):
      global lvars
      if self.var.name in lvars:
          raise ValueError(f'{fname}:line {self.sloc}:Error:Another declaration of variable "{self.var.name}"\n'f'{fname}:line {declarations_line[self.var.name]}:Info:Earlier declaration of "{self.var.name}"')
      lvars.append(self.var.name)
      lvars_line[self.var.name] = self.sloc

    @property
    def js_obj(self):
        return {'tag': 'Vardecl',
                'var': self.var.js_obj,
                'init': self.init.js_obj}


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
        var_type = self.lookup_variable_type(self.var.name, var_types)
        self.expr.type_check(var_types)
        if var_type != self.expr.ty:
            raise TypeError(f"Assignment of variable '{self.var.name}' of type '{var_type}' to expr of type '{self.expr.ty}' at line {self.sloc}")

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
            raise TypeError(f'Can only print INT, not {self.expr.ty}, at line {self.sloc}')

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
        assert isinstance(ifrest, (Block, IfElse))
        self.condition = condition  #to enter the block
        self.block = block          #list of statements
        self.ifrest = ifrest        #else blocks

    def type_check(self, var_types):
        self.condition.type_check(var_types)
        if self.condition.type != 'bool':
            raise TypeError(f'IfElse cannot be of type {self.condition.type} at line {self.sloc},  must be of type bool')
        self.block.type_check(var_types)
        self.ifrest.type_check(var_types)

    def syntax_check(self, fname):
        self.block.syntax_check(fname)
        self.ifrest.syntax_check(fname)

    @property
    def js_obj(self):
        return {'tag': 'IfElse',
                'condition': self.condition.js_obj,
                'block': self.block.js_obj,
                'ifrest': self.ifrest.js_obj}

    #@property
    # def statement_to_json(self):
    #     return [
    #         "<statement:ifelse>",
    #         {
    #             "position": {
    #                 "start": [],
    #                 "end": []
    #             }
    #             "condition": [
    #                 f"<expression:{str()}"
    #             ]
    #         }

    #     ]


class While(Statement):
    def __init__(self, sloc, condition: Expression, block: Block):
        super().__init__(sloc)
        self.condition = condition
        self.block = block

    def type_check(self, var_types):
        self.condition.type_check(var_types)
        if self.condition.ty != 'bool':
            raise TypeError(f'WHILE cannot be of type {self.condition.ty} at line {self.sloc}, must be of type BOOL')
        self.block.type_check(var_types)

    def syntax_check(self, fname):
        self.block.syntax_check(fname)

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
        pass

    def syntax_check(self, fname):
        pass

    @property
    def js_obj(self):
        return {'tag': self.operator.capitalize()}

    @property
    def statement_to_json(self):
        pass


class Program(Node):
  def __init__(self, sloc, lvars, block):
    super().__init__(sloc)
    self.block = block
    self.lvars = lvars
    #self.type_check([])


  # @staticmethod
  # def load(js_obj):
  #   assert isinstance(js_obj, list)
  #   if len(js_obj) > 1:
  #       sloc = js_obj[1]
  #   else:
  #       sloc = None
  #   js_obj = js_obj[0]
  #   assert len(js_obj) == 2
  #   js_obj = js_obj[1]
  #   assert len(js_obj) == 5
  #   section = js_obj['body'][:]
  #   stmts = []
  #   while len(section) > 0:
  #     stmtt = block.pop(0)
  #     stmt = Statement.load(stmtt)
  #     assert stmt is not None, stmtt
  #     stmts.append(stmt)
  #   return Program(sloc, stmts)

  def type_check(self, var_types):
    self.block.type_check(var_types)

  def syntax_check(self, fname):
    self.block.syntax_check(fname)

  @property
  def js_obj(self):
    return {'tag': 'Program',
            'vars': self.lvars,
            'block': self.block.js_obj}

  @property
  def prog_to_json(self):
    return [self.block.statement_to_json]
