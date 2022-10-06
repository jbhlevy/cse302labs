"""
This file contains a class Prog that performs maximal munch IR translation
"""
from ast import Assign, While
import AST as ast

ast.op_codes_bis

class Instruction:
  __slots__ = ['opcode', 'args', 'result']

  def __init__(self, opcode, args, result):
    self.opcode = opcode
    self.args = args
    self.result = result

  @property
  def js_obj(self):
    return {'opcode': self.opcode,
            'args': self.args,
            'result': self.result}


class Prog:
  def __init__(self, program, alg):
    self.localtemporaries = []
    self.instrs = []
    self.__tempdict = dict()
    self.__last = -1
    self.__last_label = -1
    self._break_stack = []
    self._continue_stack = []

    if alg == 'tmm':
      for stmt in program.lvars:
        self._emit('const', [0], self._lookup(stmt))
      self.tmm_stmt(program.block)
    elif alg == 'bmm':
      for stmt in program.lvars:
        self._emit('const', [0], self._lookup(stmt))
      self.bmm_stmt(program.block)

  @property
  def js_obj(self):
    return [{'proc': '@main',
             'body': [i.js_obj for i in self.instrs]}]

  def _freshtemp(self):
    self.__last += 1
    t = f'%{self.__last}'
    self.localtemporaries.append(t)
    return t

  def _fresh_label(self):
    self.__last_label += 1
    t = f'%.L{self.__last_label}'
    return t

  def _lookup(self, var):
    t = self.__tempdict.get(var)
    if t is None:
      t = self._freshtemp()
      self.__tempdict[var] = t
    return t

  def _emit(self, opcode, args, result):
    self.instrs.append(Instruction(opcode, args, result))

# =============================================================

  def tmm_expr(self, expr, target):
      if isinstance(expr, ast.ExpressionVar):
        self._emit('copy', [self._lookup(expr.name)], target)
      elif isinstance(expr, ast.ExpressionInt):
        self._emit('const', [expr.value], target)
      elif isinstance(expr, ast.ExpressionUniOp):
        #print("TMM: op:", expr.operator)
        arg_target = self._freshtemp()
        self.tmm_expr(expr.argument, arg_target)
        self._emit(ast.op_codes[expr.operator], [arg_target], target)
      elif isinstance(expr, ast.ExpressionBinOp):
        #print("TMM: op:", expr.operator)
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
        #print("DIDN'T DO ANYTHING YE")
        #pass
      else:
        raise ValueError(f'In tmm_expr: unknown expression {expr.__class__}')

  def tmm_bool_expr(self, boolexpr, Lt, Lf):
    '''jump to Lt if true & Lf if false'''
    if isinstance(boolexpr, ast.Bool):
      if boolexpr.value == True:
        self._emit('jmp', [Lt], None)
      elif boolexpr.value == False:
        self._emit('jmp', [Lf], None)
    elif isinstance(boolexpr, ast.ExpressionUniOp):
      if boolexpr.operator in {'EQ', 'NEQ', 'LT', 'LTEQ', 'GT', 'GTEQ'}:
        #print(boolexpr.operator)
        arg_target = self._freshtemp()
        self.tmm_expr(boolexpr.argument, arg_target)
        self._emit('sub', [boolexpr.argument], [boolexpr.argument][0])
        self._emit(ast.op_codes[boolexpr.operator], [[boolexpr.argument][0], Lt], None)
        self._emit('jmp', [Lf], None)
      elif boolexpr.operator == '&&':
        Li = self._fresh_label()
        self.tmm_bool_expr([boolexpr.argument][0], Li, Lf)
        self._emit('label', [Li], None)
        self.tmm_bool_expr([boolexpr.argument][1], Lt, Lf)
      elif boolexpr.operator == '||':
        Li = self._fresh_label()
        self.tmm_bool_expr([boolexpr.argument][0], Lt, Li)
        self._emit('label', [Li], None)
        self.tmm_bool_expr([boolexpr.argument][1], Lt, Lf)
      elif boolexpr.operator == '!':
        self.tmm_bool_expr([boolexpr.argument][0], Lf, Lt)
    elif isinstance(boolexpr, ast.ExpressionBinOp):
      #print('location tmm bool expr: operator; ', boolexpr.operator)
      if boolexpr.operator in {'==', '!=', '<', '<=', '>', '>='}:
        #print('2222 location tmm bool expr: left; ', boolexpr.left)
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
      elif boolexpr.operator == '!':
        self.tmm_bool_expr([boolexpr.left][0], Lf, Lt)
    else:
      raise ValueError(
        f'In tmm_expr:unknown expr kind: {boolexpr.__class__}')


  def tmm_stmt(self, stmt):
    #print(stmt)
    if isinstance(stmt, ast.Vardecl):
      target = self._lookup(stmt.var.name)
      self.tmm_expr(stmt.expr, target)
    elif isinstance(stmt, ast.Assign):
      target = self._lookup(stmt.lhs.name)
      self.tmm_expr(stmt.rhs, target)
    elif isinstance(stmt, ast.Print):
      target = self._freshtemp()
      self.tmm_expr(stmt.arg, target)
      self._emit('print', [target], None)
    elif isinstance(stmt, ast.IfElse):
      Lt = self._fresh_label()
      Lf = self._fresh_label()
      Lo = self._fresh_label()
      #print("INSIDE TMM STMT, condition:", stmt.condition)
      self.tmm_bool_expr(stmt.condition, Lt, Lf)
      self._emit('label', [Lt], None)
      self.tmm_stmt(stmt.block)
      self._emit('jmp', [Lo], None)
      self._emit('label', [Lf], None)
      self.tmm_stmt(stmt.ifrest)
      self._emit('label', [Lo], None)
    elif isinstance(stmt, ast.Block):
      for stmt in stmt.stmts:
        self.tmm_stmt(stmt)
    elif isinstance(stmt, ast.While):
      #print("INSIDE TMM, WHILE")
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
