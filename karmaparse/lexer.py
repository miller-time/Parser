#----------------------------------------------------------
# karmaparse.py
#
# This is an attempt to mimic the interaction with karmabot
# using PLY instead of regular expressions
#----------------------------------------------------------
from ply import lex

reserved = {
    'karmabot': 'KARMABOT',
    }

tokens = (
  'THING',
  'PLUS',
  'MINUS',
  'COLON',
  ) + tuple(reserved.values())


def t_THING(t):
    # reserved words should not be made into things
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'THING')    # Check for reserved words
    return t

t_PLUS = r'\+'

t_MINUS = r'-'

t_COLON = r':'

t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

if __name__ == '__main__':

    # A little unit test for the lexer
    s = ("""karmabot: millertime """,
         )
    lex.input(s[0])

    while True:
        tok = lex.token()
        if not tok:
            break
        print tok
