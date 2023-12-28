import ply.lex as lex

tokens = (
    'number',
    'ID',
    'bool_val',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULUS',
    'GREATER',
    'SMALLER',
    'EQUAL',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
    'PRINT_NUM',
    'PRINT_BOOL',
    'DEFINE',
    'IF',
    'FUN',
    'separator'
)

reserved = {
    'if': 'IF',
    'mod': 'MODULUS',
    'define': 'DEFINE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'print-num': 'PRINT_NUM',
    'print-bool': 'PRINT_BOOL',
    'fun': 'FUN',
}

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'mod'

t_GREATER = r'>'
t_SMALLER = r'<'
t_EQUAL = r'='

t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_PRINT_NUM = r'print-num'
t_PRINT_BOOL = r'print-bool'
t_DEFINE = r'define'
t_IF = r'if'
t_FUN = r'fun'



def t_number(t):
    r'0|(-?[1-9][0-9]*)'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9-]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_bool_val(t):
    r'\#t|\#f'
    t.value = t.value == '#t'
    return t

def t_separator(t):
    r'[\t\n\r ]+'
    pass

def t_error(t):
    raise SyntaxError(f"Illegal character '{t.value[0]}' at line {t.lineno}:{t.lexpos}")


lexer = lex.lex()

if __name__ == "__main__":
    input_string = "(define a (if (and (< 1 5) (< 5 1)) 123 321)) (print-num a)"
    lexer.input(input_string)
    for token in lexer:
        print(token)
    