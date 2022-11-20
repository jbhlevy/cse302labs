import AST as ast
import AST

class Instruction:
  __slots__ = ['opcode', 'args', 'result'] # slots allow us to pre-allocate the memory for each instance of the class we create (makes the compiler more efficient)

  def __init__(self, opcode: str, args: list, result: str):
    self.opcode = opcode
    self.args = args
    self.result = result

  @property
  def js_obj(self):
    return {'opcode': self.opcode,
            'args': self.args,
            'result': self.result}
  
  def __repr__(self):
        return f"{{opcode: {self.opcode}, args: {self.args}, result: {self.result}}}"

class GlobalVar:
    __slots__ = ['var', 'init']

    def __init__(self, var: str, init:int):
        self.var = "@"+var
        self.init = init

    @property
    def js_obj(self):
        return {'var': self.var, 
                'init': self.init
                }

    # def __repr__(self):
    #     return f"{{var: {self.var}, init: {self.init}}}"

class Procedure:
    def __init__(self, name: str, args: list, body):
        self.name = "@"+name
        self.args = args
        self.body = body

    @property
    def js_obj(self):
        return {"proc": self.name,
                "args": self.args,
                'body': [i.js_obj for i in self.body]
                }


class Prog:
    def __init__(self, program: ast.Program, alg: str):
        self.localtemporaries = []
        self.tac = []
        self.scope = dict()

        if alg == 'tmm':
            for stmt in program.global_vars:
                self._emit_global_var(stmt.var.name, stmt.expr.value)
                self._add_global_to_scope(stmt.var)
            for proc in program.procs:
                print("proc name:", proc.name)
                current_proc = ProcUnit(proc, self.scope)
                #print("current proc:", current_proc)
                self._emit_procedure(current_proc.name, current_proc.args, current_proc.body)

    def _emit_global_var(self, var: str, init: int):
        self.tac.append(GlobalVar(var, init))
    
    def _add_global_to_scope(self, var: ast.ExpressionVar):
        self.scope[var.name] = "@"+var.name

    def _emit_procedure(self, name: str, args: list, body: list):
        self.tac.append(Procedure(name, args, body))

    @property
    def js_obj(self):
        return [i.js_obj for i in self.tac]

class ProcUnit:
    def __init__(self, proc, gvars):
        self.name = proc.name
        self.args = []
        self.instructions = []
        self.localtemporaries = []
        self.__last = -1
        self.__last_label = -1
        self.body = []

        for i in range(len(proc.params)):
            for j in range(len(proc.params[i])):
                self.args.append('%'+proc.params[i][j].name)

        # for args in proc.params:
        #     for arg in args:
        #         self.args.append(f"%{arg.name}")
        #         self.__tempdict[arg.name] = f"%{arg.name}"

        # stacks for munching 
        self._break_stack = []
        self._continue_stack = []

        # gvars scope
        self.scope_stack = [{gvar.var[1:]: gvar.var for gvar in gvars}]

        # procs scope
        self.scope_stack.append({arg[1:]: arg for arg in self.args})

        for stmt in proc.block.stmts:
            self.tmm_stmt(stmt)

        # self.tmm_stmt(proc.block)

        # for (k, v) in self._global.items():
        #     t = self.__tempdict.get(k)
        #     print(t)
        #     if t is None:
        #         self.__tempdict[k] = v
        # self.body = []

        # print(f"procedure {self.name} has block: {proc.block} and scope is {self.__tempdict}")
    
    # def __repr__(self) -> str:
    #     return f"Proc name : {self.name}\n args : {self.args} \n body : {self.body}"

    def _freshtemp(self):
        #Creating a new temporary 
        self.__last += 1
        t = f'%{self.__last}'
        self.localtemporaries.append(t)
        return t

    def _fresh_label(self):
        #Creating a new label 
        self.__last_label += 1
        t = f'%.L{self.__last_label}'
        return t

    def _lookup(self, var: str, scope = -1):
        #Checking if there already exists a temporary for a given var
        print("lookup", self.scope_stack)
        t = self.scope_stack[scope].get(var)
        if t is None:
            print("t was None")
            t = self._check_global(scope, var)


        return t

    def _check_global(self, scope, var):
        if scope == -len(self.scope_stack):
            print("branch 1")
            t = self._freshtemp()
            self.scope_stack[-1][var] = t
        else:
            print("branch 2")
            t = self._lookup(var, scope-1)
        return t

    def _emit(self, opcode, args, result):
        self.body.append(Instruction(opcode, args, result))

# ================= Maxmimal Munch =================================================

    def tmm_expr(self, expr: ast.Expression, target: str):
    #TMM for expressions 
        if isinstance(expr, ast.ExpressionVar):
            self._emit('copy', [self._lookup(expr.name)], target)

        elif isinstance(expr, ast.ExpressionInt):
            self._emit('const', [expr.value], target)

        #no comprendo    
        elif isinstance(expr, ast.ExpressionUniOp):
            arg_target = self._freshtemp()
            self.tmm_expr(expr.argument, arg_target)
            self._emit(ast.op_codes[expr.operator], [arg_target], target)

        #no comprendo    
        elif isinstance(expr, ast.ExpressionBinOp):
            args = []
            arg_target1 = self._freshtemp()
            self.tmm_expr(expr.left, arg_target1)
            args.append(arg_target1)
            arg_target2 = self._freshtemp()
            self.tmm_expr(expr.right, arg_target2)
            args.append(arg_target2)
            self._emit(ast.op_codes[expr.operator], args, target)

        elif isinstance(expr, ast.Bool):
            self._emit('const', [1 if expr.value else 0], target)

        #no comprendo    
        elif isinstance(expr, ast.Call):
            #Setting up parameters 
            p = 0
            for arg in expr.args:
                p += 1
                ptarget = self._freshtemp()
                self.tmm_expr(arg, ptarget)
                self._emit('param', [p, ptarget], None)
            self._emit('call', ["@"+expr.name, p], target)
        #j'aurais fait comme ca:
        elif isinstance(expr, ast.Call):
            for i in range(min(6, len(expr.args))):
                arg_t = self._freshtemp()
                self.tmm_expr(expr.args[i], arg_t)
                self._emit('param', [i+1, arg_t], None)
            for i in range(len(expr.args)-1, 5, -1):
                arg_t = self._freshtemp()
                self.tmm_expr(expr.args[i], arg_t)
                self._emit('param', [i+1, arg_t], None)
            self._emit('call', ['@'+expr.name, len(expr.args)], target)
        else:
            raise ValueError(f'In tmm_expr: unknown expression {expr.__class__}')

# ================================================================================

    def tmm_bool_expr(self, boolexpr: ast.Expression, Lt: str, Lf: str): 
        print(boolexpr.__class__)
    #TMM for boolean expressions, the main idea is the following: 
    #jump to Lt if true, to Lf if false

        # if not (
        #     (
        #         isinstance(boolexpr, AST.Bool) and (not isinstance(boolexpr, ast.Bool))
        #     ) or ((not isinstance(boolexpr, AST.Bool)) and isinstance(boolexpr, ast.Bool))):
        #         print("worked !")
        # else: 
        #     raise ValueError(f"In tmm_bool_expr:unknown expr kind: {boolexpr.__class__}")

        if (boolexpr.__class__ is AST.Bool):
            print("this makes no sense: ", int(boolexpr.__class__ is AST.Bool))
            print("instance does work but ... ")
            if boolexpr.value == True:
                self._emit('jmp', [Lt], None)
            elif boolexpr.value == False:
                self._emit('jmp', [Lf], None)

        elif isinstance(boolexpr, ast.ExpressionInt):
            if boolexpr.value:
                self._emit('jmp', [Lt], None)
            else:
                self._emit('jmp', [Lf], None)

        elif isinstance(boolexpr, ast.ExpressionVar):
            self.tmm_expr(boolexpr, self._freshtemp())
            self._emit('je', [self._freshtemp(), Lf], None)
            self._emit('jnz', [self._freshtemp(), Lt], None)

        #no comprendo
        elif isinstance(boolexpr, ast.ExpressionUniOp):
            if boolexpr.operator == '!':
                self.tmm_bool_expr([boolexpr.argument][0], Lf, Lt)

        #no comprendo
        elif isinstance(boolexpr, ast.ExpressionBinOp):
            print("Went into BINOP ")
            if boolexpr.operator in {'==', '!=', '<', '<=', '>', '>='}:
                largs = []
                arg_target1 = self._freshtemp()
                self.tmm_expr(boolexpr.left, arg_target1)
                largs.append(arg_target1)
                arg_target2 = self._freshtemp()
                self.tmm_expr(boolexpr.right, arg_target2)
                largs.append(arg_target2)
                self._emit('sub', largs, largs[0])
                self._emit(ast.op_codes[boolexpr.operator], [largs[0], Lt], None)
                self._emit('jmp', [Lf], None)
            elif boolexpr.operator == '&&':
                Li = self._fresh_label()
                self.tmm_bool_expr([boolexpr.left][0], Li, Lf)
                self._emit('label', [Li], None)
                self.tmm_bool_expr([boolexpr.right][0], Lt, Lf)
            elif boolexpr.operator == '||':
                Li = self._fresh_label()
                print()
                self.tmm_bool_expr(boolexpr.left, Lt, Li)
                self._emit('label', [Li], None)
                self.tmm_bool_expr(boolexpr.right, Lt, Lf)
        else:
            print("weird")
            raise ValueError(f"In tmm_bool_expr:unknown expr kind: {boolexpr.__class__}")
        # else:
        #     raise ValueError( f'In tmm_bool_expr:unknown expr kind: {boolexpr.__class__}')


        # if isinstance(boolexpr, ast.Bool):
        #     if boolexpr.value == True:
        #         self._emit('jmp', [Lt], None)
        #     elif boolexpr.value == False:
        #         self._emit('jmp', [Lf], None)

        # if isinstance(boolexpr, ast.ExpressionInt):
        #     if boolexpr.value:
        #         self._emit('jmp', [Lt], None)
        #     else:
        #         self._emit('jmp', [Lf], None)

        # if isinstance(boolexpr, ast.ExpressionVar):
        #     self.tmm_expr(boolexpr, self._freshtemp())
        #     self._emit('je', [self._freshtemp(), Lf], None)
        #     self._emit('jnz', [self._freshtemp(), Lt], None)

        # #no comprendo
        # elif isinstance(boolexpr, ast.ExpressionUniOp):
        #     if boolexpr.operator == '!':
        #         self.tmm_bool_expr([boolexpr.argument][0], Lf, Lt)

        # #no comprendo
        # elif isinstance(boolexpr, ast.ExpressionBinOp):
        #     if boolexpr.operator in {'==', '!=', '<', '<=', '>', '>='}:
        #         largs = []
        #         arg_target1 = self._freshtemp()
        #         self.tmm_expr(boolexpr.left, arg_target1)
        #         largs.append(arg_target1)
        #         arg_target2 = self._freshtemp()
        #         self.tmm_expr(boolexpr.right, arg_target2)
        #         largs.append(arg_target2)
        #         self._emit('sub', largs, largs[0])
        #         self._emit(ast.op_codes[boolexpr.operator], [largs[0], Lt], None)
        #         self._emit('jmp', [Lf], None)
        #     elif boolexpr.operator == '&&':
        #         Li = self._fresh_label()
        #         self.tmm_bool_expr([boolexpr.left][0], Li, Lf)
        #         self._emit('label', [Li], None)
        #         self.tmm_bool_expr([boolexpr.right][0], Lt, Lf)
        #     elif boolexpr.operator == '||':
        #         Li = self._fresh_label()
        #         self.tmm_bool_expr(boolexpr.left, Lt, Li)
        #         self._emit('label', [Li], None)
        #         self.tmm_bool_expr(boolexpr.right[0], Lt, Lf)
        
# ================================================================================

    #ca m'a l'air pas mal ca
    def tmm_stmt(self, stmt: ast.Statement):
    #TMM for statements (same as in previous lab with addition of If and While statements)
        if isinstance(stmt, ast.Vardecl):
            target = self._lookup(stmt.var.name)
            self.tmm_expr(stmt.expr, target)
        elif isinstance(stmt, ast.Assign):
            target = self._lookup(stmt.lhs.name)
            print("Assign target", target)
            self.tmm_expr(stmt.rhs, target)
        elif isinstance(stmt, ast.Print):
            target = self._freshtemp()
            self.tmm_expr(stmt.arg, target)
            self._emit('print', [target], None)
        elif isinstance(stmt, ast.IfElse):
            Lt = self._fresh_label()
            Lf = self._fresh_label()
            Lo = self._fresh_label()
            print("statement:", stmt.condition)
            self.tmm_bool_expr(stmt.condition, Lt, Lf)
            print("Label:", Lt)
            self._emit('label', [Lt], None)
            self.tmm_stmt(stmt.block)
            self._emit('jmp', [Lo], None)
            self._emit('label', [Lf], None)
            self.tmm_stmt(stmt.ifrest)
            self._emit('label', [Lo], None)
        elif isinstance(stmt, ast.Block):
            print('found block')
            for stmt in stmt.stmts:
                print(stmt)
                self.tmm_stmt(stmt)
                print(f"Finished with stmt {stmt}")
        elif isinstance(stmt, ast.While):
            Lhead = self._fresh_label()
            Lbody = self._fresh_label()
            Lend = self._fresh_label()
            self._break_stack.append(Lend)
            self._continue_stack.append(Lhead)
            self._emit('label', [Lhead], None)
            self.tmm_bool_expr(stmt.condition, Lbody, Lend)
            self._emit('label', [Lbody], None)
            self.tmm_stmt(stmt.block)
            self._emit('jmp', [Lhead], None)
            self._emit('label', [Lend], None)
            self._break_stack.pop()
            self._continue_stack.pop()
        elif isinstance(stmt, ast.Jump):
            if stmt.operator == 'break':
                if len(self._break_stack) < 1:
                    raise ValueError(f'Bad break at line {stmt.sloc}')
                self._emit('jmp', [self._break_stack[-1]], None)
            elif stmt.operator == 'continue':
                if len(self._continue_stack) < 1:
                    raise ValueError(f'Bad continue at line {stmt.sloc}')
                self._emit('jmp', [self._continue_stack[-1]], None)
            else:
                print(stmt)
                raise ValueError(f'tmm_stmt: unknown stmt kind: {stmt.__class__}')
        elif isinstance(stmt, ast.Eval):
            callee = stmt.expression
            print("called:", callee)
            print('args', callee.args)
            #Setting up parameters 
            p = 0
            for arg in callee.args:
                p += 1
                target = self._freshtemp()
                self.tmm_expr(arg, target)
                self._emit('param', [p, target], None)
            #Differentiating functions and subroutines
            if callee.type == ast.Type.VOID:
                #Subroutine
                self._emit('call', ["@"+callee.name, p], None)
            else:
                raise Exception("ERROR")
                # target = self._freshtemp()
                # self._emit('call', [callee.name, p], target)

        elif isinstance(stmt, ast.Return):
            #Differentiating return; and return expr; 
            if stmt.expression is not None:
                target = self._freshtemp()
                self.tmm_expr(stmt.expression, target)
                self._emit('ret', [target], None)
            else:
                self._emit('ret', [], None)

        #else:
            #print(f'Statement {stmt} did not find match')
            #raise Exception("STOP")
            #print("DID NOT FIND TMM CASE")

import bx2front 
from AST import ProcDecl
from AST import Vardecl
from AST import Bool
import json

def bx_to_json(fn):
    assert fn.endswith('.bx')
    gvars = []
    procs = []

    file = open(fn, "r")
    text = file.read()
    file.close()
    reader = bx2front.Reader(fn, text)
    ast = reader.read()
    ast.type_check([])

    def add_gvar(decl):
        if isinstance(decl.expr, Bool):
            value = 1 if decl.expr.value else 0
        else:
            value = decl.expr.value
        gvar = GlobalVar(decl.var.name, value)
        gvars.append(gvar)

    # Global Variables
    for decl in ast.global_vars:
        if isinstance(decl, Vardecl):
            add_gvar(decl)
            # transform into json

    # Function Declarations
    for decl in ast.procs:
        if isinstance(decl, ProcDecl):
            proc_tac = ProcUnit(decl, gvars)
            # convert tac into json
            procs.append(Procedure(proc_tac.name, proc_tac.args, proc_tac.body))

    full = gvars + procs
    full_json = []
    for elem in full:
        full_json.append(elem.js_obj)

    tac = fn[:-2] + 'tac.json'
    with open(tac, 'w') as fp:
        json.dump(full_json, fp)
    return tac


