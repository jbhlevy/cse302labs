import AST as ast

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
        return {'var': self.var, 'init': self.init}

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

    # def _lookup(self, var: str):
    #     #Checking if there already exists a temporary for a given var
    #     t = self.__tempdict.get(var)
    #     if t is None:
    #         t = self._freshtemp()
    #         self.__tempdict[var] = t
    #     return t



    def _emit_procedure(self, name: str, args: list, body: list):
        self.tac.append(Procedure(name, args, body))

    @property
    def js_obj(self):
        return [i.js_obj for i in self.tac]

class ProcUnit:
    def __init__(self, proc, global_scope):
        self.name = proc.name
        self.args = []
        self._global = global_scope
        self.localtemporaries = []
        self.__tempdict = dict()
        self.__last = -1
        self.__last_label = -1
        self._break_stack = []
        self._continue_stack = []
        for args in proc.params:
            #self.args += [f"%{arg.name}" for arg in args]
            for arg in args:
                self.args.append(f"%{arg.name}")
                self.__tempdict[arg.name] = f"%{arg.name}"

        for (k, v) in self._global.items():
            t = self.__tempdict.get(k)
            print(t)
            if t is None:
                self.__tempdict[k] = v
        self.body = []

        print(f"procedure {self.name} has block: {proc.block} and scope is {self.__tempdict}")

        self.tmm_stmt(proc.block)
    
    def __repr__(self) -> str:
        return f"Proc name : {self.name}\n args : {self.args} \n body : {self.body}"

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

    def _lookup(self, var: str):
        #Checking if there already exists a temporary for a given var
        t = self.__tempdict.get(var)
        print(f"Lookup function, t = {t}")
        if t is None:
            t = self._freshtemp()
            self.__tempdict[var] = t
        return t

    def _check_global(self, var:str):
        t = self._global.get(var)
        if t is None:
            t = self._freshtemp()
            self.__tempdict[var] = t
            return False
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
        elif isinstance(expr, ast.ExpressionUniOp):
            arg_target = self._freshtemp()
            self.tmm_expr(expr.argument, arg_target)
            self._emit(ast.op_codes[expr.operator], [arg_target], target)
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
        elif isinstance(expr, ast.Call):
            #Setting up parameters 
            p = 0
            for arg in expr.args:
                p += 1
                ptarget = self._freshtemp()
                self.tmm_expr(arg, ptarget)
                self._emit('param', [p, ptarget], None)
            self._emit('call', ["@"+expr.name, p], target)
        else:
            raise ValueError(f'In tmm_expr: unknown expression {expr.__class__}')

# ================================================================================

    def tmm_bool_expr(self, boolexpr: ast.Expression, Lt: str, Lf: str):
    #TMM for boolean expressions, the main idea is the following: 
    #jump to Lt if true, to Lf if false
        if isinstance(boolexpr, ast.Bool):
            if boolexpr.value == True:
                self._emit('jmp', [Lt], None)
            elif boolexpr.value == False:
                self._emit('jmp', [Lf], None)
        elif isinstance(boolexpr, ast.ExpressionUniOp):
            if boolexpr.operator == '!':
                self.tmm_bool_expr([boolexpr.argument][0], Lf, Lt)
        elif isinstance(boolexpr, ast.ExpressionBinOp):
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
                self.tmm_bool_expr([boolexpr.left][0], Lt, Li)
                self._emit('label', [Li], None)
                self.tmm_bool_expr([boolexpr.right][0], Lt, Lf)
        else:
            raise ValueError(
                f'In tmm_expr:unknown expr kind: {boolexpr.__class__}')

# ================================================================================

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
            self.tmm_bool_expr(stmt.condition, Lt, Lf)
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

    



