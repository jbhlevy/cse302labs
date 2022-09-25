"""
This file consists of the declarations of all the classes used for the AST of programs in BX.
Methods serve two main purposes :
1) going from BX (source code) ----> AST (json)
2) going from AST (json) ---> TAC (json)
"""
# ==========================================================

"""
Part A: Tables
"""
# ============== Operators Tables ==========================

# ====== Used in BX --> AST convrsion ======================

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
# ====== Used in AST --> TAC convrsion =====================

uniop_map = {
    "opposite": "neg",
    "bitwise-negation": "not",
    "bitwise-and": "and",
    "bitwise-or": "or",
    "bitwise-xor": "xor",
    "logical-shift-right": "shr",
    "logical-shift-left": "shl",
}
binop_map = {
    "addition": "add",
    "substraction": "sub",
    "multiplication": "mul",
    "division": "div",
    "modulus": "mod",
    "bitwise-and": "and",
    "bitwise-or": "or",
    "bitwise-xor": "xor",
    "logical-shift-right": "shr",
    "logical-shift-left": "shl",
}


# ==============================================
""" 
The following block consists of the Classes definitions used when crating or analyzing the AST 
All classes inhrit from a basee Node Class
All expr. inherit from a base Expression Class. 
All stmt. inherit from a base Statement Class. 
Both classes contain a static method: json_to_class to convert the JSON object into instancs of each class.
Finally, the whole program is encapsulated in on single class calld procdure that contains all the instructions before converting to JSON format.
 """

def json_to_name(js_obj):
    """
    Function to obtain the string format of the name of a JSON object
    """
    return js_obj[1]['value']

class Node:
    def __init__(self, location = []):
        self.loc = location

    def syntax_error(self, msg, err):
        if self.loc is None:
            print(f"Error: {msg}")
        else:
            linenb, lexpos = self.loc
            err(linenb, lexpos, msg)
        raise SyntaxError(msg)


# ============ Classes for expressions ===================

class Expression(Node):

    def __init__(self, location = []):
        super().__init__(location)

    @staticmethod
    def json_to_expr(js_obj):
        """
        Method to convert json data into an Expression instance
        """
        if js_obj[0] == '<expression:var>' or js_obj[0] == "<lvalue:var>":
            return ExpressionVar(json_to_name(js_obj[1]['name']))
    
        if js_obj[0] == '<expression:int>':
            return ExpressionInt(js_obj[1]['value']) 
    
        if js_obj[0] == '<expression:uniop>':
            operator = json_to_name(js_obj[1]['operator'])
            argument = Expression.json_to_expr(js_obj[1]['argument'])
            return ExpressionUniOp(operator, argument)
    
        if js_obj[0] == '<expression:binop>':
            operator = json_to_name(js_obj[1]['operator'])
            arguments = [
                Expression.json_to_expr(js_obj[1]['left']),
                Expression.json_to_expr(js_obj[1]['right'])]
            return ExpressionBinOp(operator, arguments)

        if js_obj[0] == '<expression:call>':
            target = json_to_name(js_obj[1]['target'])
            arguments = Expression.json_to_expr(js_obj[1]['arguments'][0])
            #print("making eval instance:", js_obj[1]['arguments'][0])
            return ExpressionCall(target, arguments)
        
        return None


class ExpressionVar(Expression): 
    def __init__(self, name, location = []):
        """
        name: string representing the variable in the program
        """
        super().__init__(location)
        self.name = name

    def check_syntax(self, vars, err):
        if self.name not in vars:
            self.syntax_error(f'Unknown variable {self.name}', err)
    
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
    def __init__(self, value, location = []):
        """
        value: int representing the value of the number 
        """
        super().__init__(location)
        self.value = value
        assert (0 <= self.value < 9223372036854775808), "Invalid Operation, int declaration too large"

    def check_syntax(self, vars, err):
        pass

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
    def __init__(self, operator, argument, location = []):
        """
        operator: string representing the operator used
        argument: variable we use the operator on (Expressions)
        """
        super().__init__(location)
        self.operator = operator
        self.argument = argument
        assert isinstance(argument, Expression), f"Invalid operation, argument must be of type Expression but is of type {argument.__class__}"

    def check_syntax(self, vars, err):
        self.argument.check_syntax(vars, err)

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
    def __init__(self, operator, arguments, location = []):
        """
        operator: string representing the operator used
        argument: variables we use the operator on (Expressions)
        """
        super().__init__(location)
        self.operator = operator
        self.arguments = arguments
        for arg in arguments:
            assert isinstance(arg, Expression), f"Invalid operation, argument must be of type Expression but is of type {arg.__class__}"

    def check_syntax(self, vars, err):
        for arg in self.arguments:
            arg.check_syntax(vars, err)

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
                "left": self.arguments[0].expr_to_json, 
                "right": self.arguments[1].expr_to_json
            }
        ]

class ExpressionCall(Expression):
    def __init__(self, target, argument, location = []):
        """
        target: json_obj containing the target function call
        argument: Expression to be passed as argument to the function
        """
        super().__init__(location)
        self.name = target
        self.argument = argument

    def check_syntax(self, vars, err):
        self.argument.check_syntax(vars, err)
        
    @property
    def expr_to_json(self): 
        return [
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
                        "value": self.name
                    }
                ], 
                "arguments": [self.argument.expr_to_json]
            }
        ]

# ============ Classes for statements ===================

class Statement(Node):

    def __init__(self, location = []):
        super().__init__(location)
    
    @staticmethod
    def json_to_statement(js_obj):
        """
        Method to convert json data into a Statement instance
        """
        if js_obj[0] == "<statement:assign>":
            left = js_obj[1]["lvalue"]
            right = js_obj[1]["rvalue"]
            return VarAssignement(
                Expression.json_to_expr(left),
                Expression.json_to_expr(right)
                )
        elif js_obj[0] == "<statement:eval>":
            call = Expression.json_to_expr(js_obj[1]["expression"])
            return Eval(call.name, call.argument)
        elif js_obj[0] == "<statement:vardecl>":
             name = json_to_name(js_obj[1]["name"])
             value = json_to_name(js_obj[1]["init"])
             return VarDecl(ExpressionVar(name), ExpressionInt(value))
        return None

class VarAssignement(Statement):
    def __init__(self, left: ExpressionVar, right: Expression, location = []):
        """
        left: ExpressionVar 
        Right: Expression
        """
        super().__init__(location)
        self.left = left
        self.right = right

    def check_syntax(self, vars, err):
        self.left.check_syntax(vars, err)
        self.right.check_syntax(vars, err)


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
                            "value": self.left.name
                            }
                        ]
                    }
                ], 
                "rvalue": self.right.expr_to_json
            }
        ]


#Only used for print at the moment 
class Eval(Statement):
    def __init__(self, name, arguments, location = []):
        """
        name: name of the function to be evaluated 
        arguments: args to be passed to the function
        """
        super().__init__(location)
        self.name = name
        self.arguments = arguments
        self.call = ExpressionCall(self.name, self.arguments, location)

    def check_syntax(self, vars, err):
        self.call.check_syntax(vars, err)

    @property
    def statement_to_json(self):
        return [
            "<statement:eval>", 
            {
                "position": {
                    "start": [], 
                    "end": []
                }, 
                "expression": self.call.expr_to_json
            }
        ]

class VarDecl(Statement):
    def __init__(self, var, value, location = []):
        super().__init__(location)
        self.var = var
        self.name = self.var.name
        self.value = value

    def check_syntax(self, vars, err):
        if self.name in vars:
            self.syntax_error(f'Invalid Operation: Variable {self.var.name} already declared', err)
        self.value.check_syntax(vars, err)
        vars[self.name] = self

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
                    "value": self.name
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
             "init": self.value.expr_to_json
            }
        ]


# ============ Classe for procedures ===================

class Procedure(Node):
    def __init__(self, name, statements = [], location = []):
        """
        name: string being the name of the top-level procedure
        instructions: list initially empty to which we will append instructions when performing maximal munch
        """
        super().__init__(location)
        self.name = name

        #BX --> AST 
        self.statements = statements

        #AST --> TAC
        self.instructions = []

    def check_syntax(self, err):
        vars = {}
        for statement in self.statements:
            statement.check_syntax(vars, err)

    @property
    def proc_to_json(self):
        return [
            "<decl:proc>", 
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
                        "value": self.name
                    }
                ],
                "arguments": [], 
                "returntype": None,
                "body": [stmt.statement_to_json for stmt in self.statements] 
            }
        ]

    @property
    def js_obj(self):
        """
        Property used to convert class structure back to JSON TAC
        """
        return [{
            "proc": self.name,
            "body": [instr.js_obj for instr in self.instructions]
        }]


# ========================================= EOF =========================================================================


