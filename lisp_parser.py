import ply.yacc as yacc
from lisp_lexer import tokens
from lisp_types import *

start = 'PROGRAM'
vars = {}
call_stack = ['__main__']
func_scope = {}


# PROGRAM
def p_PROGRAM(p):
    'PROGRAM : STMTS'
    p[0] = p[1]
    vars.clear()
    call_stack = ['__main__']
    func_scope = {}

# STMTS
def p_STMTS(p):
    '''
    STMTS : STMT STMTS
          | empty
    '''
    p[0] = [p[1]] + p[2] if p[1] is not None else []

# STMT
def p_STMT_exp(p):
    'STMT : EXP'
    p[0] = f'exp-stmt, result: {p[1]}'

def p_STMT_def(p):
    'STMT : DEF_STMT'
    p[0] = 'def-stmt'

def p_STMT_print(p):
    'STMT : PRINT_STMT'
    p[0] = p[1]

# PRINT_STMT
def p_PRINT_STMT_num(p):
    'PRINT_STMT : LPAREN PRINT_NUM EXP RPAREN'
    if isinstance(p[3], Integer):
        print(p[3].val)
        p[0] = p[3]
    else:
        raise TypeError(f"Expect type 'Integer', got '{p[3].__class__.__name__}'")

def p_PRINT_STMT_bool(p):
    'PRINT_STMT : LPAREN PRINT_BOOL EXP RPAREN'
    if isinstance(p[3], Boolean):
        print("#t" if p[3].val else "#f")
        p[0] = p[3]
    else:
        raise TypeError(f"Expect type 'Boolean', got '{p[3].__class__.__name__}'")

# EXP
def p_EXP(p):
    '''
    EXP : BOOL
        | INT
        | VARIABLE
        | NUM_OP
        | LOGIC_OP
        | IF_EXP
        | FUN_EXP
        | FUN_CALL
    '''
    p[0] = p[1]

def p_EXPS(p):
    '''
    EXPS : EXP EXPS
         | empty
    '''
    p[0] = [p[1]] + p[2] if p[1] is not None else []

# NUM_OP
def p_NUM_OP_plus(p):
    'NUM_OP : LPAREN PLUS EXP EXP EXPS RPAREN'
    ans = Integer(0)
    for i in p[5]:
        ans += i
    p[0] = p[3] + p[4] + ans

def p_NUM_OP_minus(p):
    'NUM_OP : LPAREN MINUS EXP EXP RPAREN'
    p[0] = p[3] - p[4]

def p_NUM_OP_multiply(p):
    'NUM_OP : LPAREN MULTIPLY EXP EXP EXPS RPAREN'
    ans = Integer(1)
    for i in p[5]:
        ans *= i
    p[0] = p[3] * p[4] * ans

def p_NUM_OP_divide(p):
    'NUM_OP : LPAREN DIVIDE EXP EXP RPAREN'
    p[0] = p[3] // p[4]

def p_NUM_OP_modulus(p):
    'NUM_OP : LPAREN MODULUS EXP EXP RPAREN'
    p[0] = p[3] % p[4]

def p_NUM_OP_greater(p):
    'NUM_OP : LPAREN GREATER EXP EXP RPAREN'
    p[0] = p[3] > p[4]

def p_NUM_OP_smaller(p):
    'NUM_OP : LPAREN SMALLER EXP EXP RPAREN'
    p[0] = p[3] < p[4]

def p_NUM_OP_equal(p):
    'NUM_OP : LPAREN EQUAL EXP EXP EXPS RPAREN'
    p[0] = Boolean(all(expr == p[3] for expr in [p[4]] + p[5]))

# LOGIC_OP
def p_LOGIC_OP_and(p):
    'LOGIC_OP : LPAREN AND EXP EXP EXPS RPAREN'
    p[0] = Boolean(all(expr for expr in [p[3]] + [p[4]] + p[5]))

def p_LOGIC_OP_or(p):
    'LOGIC_OP : LPAREN OR EXP EXP EXPS RPAREN'
    p[0] = Boolean(any(expr for expr in [p[3]] + [p[4]] + p[5]))

def p_LOGIC_OP_not(p):
    'LOGIC_OP : LPAREN NOT EXP RPAREN'
    p[0] = Boolean(not p[3])


# Function def
def p_FUN_EXP(p):
    'FUN_EXP : LPAREN FUN FUN_IDS FUN_BODY RPAREN'
    p[0] = Function(func_scope.copy(), p[4])
    func_scope.clear()

def p_IDS(p):
    '''
    IDS : ID IDS
        | empty
    '''
    p[0] = [p[1]] + p[2] if p[1] is not None else []

def p_FUN_IDS(p):
    'FUN_IDS : LPAREN IDS RPAREN'
    p[0] = p[2]
    for var_name in p[0]:
        func_scope[var_name] = Function.var()

def p_FUN_BODY(p):
    '''
    FUN_BODY : INT
             | BOOL
             | FUN_VAR
             | LPAREN OP OPERANDS RPAREN
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Function._OpTreeNode(p[2], p[3])

def p_OPERANDS(p):
    '''
    OPERANDS : FUN_BODY OPERANDS
             | empty
    '''
    p[0] = [p[1]] + p[2] if p[1] is not None else []

def p_FUN_VAR(p):
    'FUN_VAR : ID'
    var_name = p[1]
    if var_name in func_scope.keys():
        p[0] = func_scope[var_name]
    elif var_name in vars:
        p[0] = vars[var_name]
    else:
        raise NameError(f"name '{var_name}' is not defined")

# Function operators
def p_OP_plus(p):
    'OP : PLUS'
    def f(c):
        ans = Integer(0)
        for i in c:
            ans += i
        return ans
    p[0] = f

def p_OP_minus(p):
    'OP : MINUS'
    p[0] = lambda c: c[0] - c[1]

def p_OP_multiply(p):
    'OP : MULTIPLY'
    def f(c):
        ans = Integer(1)
        for i in c:
            ans *= i
        return ans
    p[0] = f

def p_OP_divide(p):
    'OP : DIVIDE'
    p[0] = lambda c: c[0] // c[1]

def p_OP_modulus(p):
    'OP : MODULUS'
    p[0] = lambda c: c[0] % c[1]

def p_OP_greater(p):
    'OP : GREATER'
    p[0] = lambda c: c[0] > c[1]

def p_OP_smaller(p):
    'OP : SMALLER'
    p[0] = lambda c: c[0] < c[1]

def p_OP_equal(p):
    'OP : EQUAL'
    p[0] = lambda c: c[0] == c[1]

def p_OP_and(p):
    'OP : AND'
    p[0] = lambda c: c[0] and c[1]

def p_OP_or(p):
    'OP : OR'
    p[0] = lambda c: c[0] or c[1]

def p_OP_not(p):
    'OP : NOT'
    p[0] = lambda c: not c[0]

def p_OP_if(p):
    'OP : IF'
    p[0] = lambda c: c[1] if c[0] else c[2]

# Function call
def p_FUN_CALL_exp(p):
    'FUN_CALL : LPAREN FUN_EXP EXPS RPAREN'
    func = p[2]
    param_values = p[3]
    for idx, param in enumerate(func.parameters.keys()):
        func.parameters[param]._set(param_values[idx])
    p[0] = func.evaluate()

def p_FUN_CALL_name(p):
    'FUN_CALL : LPAREN ID EXPS RPAREN'
    func_name = p[2]
    if func_name in vars and isinstance(vars[func_name], Function):
        func = vars[func_name]
        param_values = p[3]
        for idx, param in enumerate(func.parameters.keys()):
            func.parameters[param]._set(param_values[idx])
        p[0] = func.evaluate()
    else:
        raise NameError(f"name '{func_name}' is not defined")

# define Statement
def p_DEF_STMT(p):
    'DEF_STMT : LPAREN DEFINE ID EXP RPAREN'
    var_name = p[3]
    if var_name not in vars:
        vars[var_name] = p[4]
    else:
        raise Exception(f"variable '{var_name}' redefined")

# if Exp
def p_IF_EXP(p):
    'IF_EXP : LPAREN IF TEST_EXP THEN_EXP ELSE_EXP RPAREN'
    if p[3]:
        p[0] = p[4]
    else:
        p[0] = p[5]

def p_TEST_EXP(p):
    'TEST_EXP : EXP'
    p[0] = p[1]

def p_THEN_EXP(p):
    'THEN_EXP : EXP'
    p[0] = p[1]

def p_ELSE_EXP(p):
    'ELSE_EXP : EXP'
    p[0] = p[1]

# Variable
def p_VARIABLE(p):
    'VARIABLE : ID'
    var_name = p[1]
    if var_name in vars:
        p[0] = vars[var_name]
    else:
        raise NameError(f"name '{var_name}' is not defined")

# Typing
def p_INT(p):
    'INT : number'
    p[0] = Integer(p[1])

def p_BOOL(p):
    'BOOL : bool_val'
    p[0] = Boolean(p[1])

# Empty production
def p_empty(p):
    'empty :'
    p[0] = None

# Error handling
def p_error(p):
    raise SyntaxError(f"Illegal token '{p.value}' at line {p.lineno}:{p.lexpos}")


parser = yacc.yacc()

if __name__ == "__main__":
    input_string = """
        (define foo
  (fun (num)
    (if (> num 1) 1 (= num 1))))

(print-num (* 8 (foo 1)))
        """
    result = parser.parse(input_string)
    