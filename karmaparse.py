#----------------------------------------------------------
# karmaparse.py
#
# This is an attempt to mimic the interaction with karmabot
# using PLY instead of regular expressions
#----------------------------------------------------------

import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
  'KARMABOT',
  'THING',
  'PLUS',
  'MINUS',
  'COLON'
  )

# Tokens

t_KARMABOT = 'karmabot'

t_THING = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_PLUS = r'\+'

t_MINUS = r'-'

t_COLON = r':'

t_ignore = " \t"

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

# Build the lexer
import lex
lex.lex()

# dictionary of things
things = {}

def p_statement_expr(p):
  'statement : expression'
  print(p[1])
#  if p[2] not in things:
#    things[p[2]] = 0
#  print '%s : %d' % (p[2],things[p[2]])

def p_statement_up(p):
  'statement : KARMABOT COLON THING PLUS PLUS'
  print(p[3])
#  if p[2] not in things:
#    things[p[2]] = 1
#  else:
#    things[p[2]] += 1

def p_statement_down(p):
  'statement : KARMABOT COLON THING MINUS MINUS'
  print(p[3])
#  if [p[2]] not in things:
#    things[p[2]] = -1
#  else:
#    things[p[2]] += -1

def p_expression_thing(p):
  "expression : KARMABOT COLON THING"
  try:
    p[0] = things[p[3]]
  except LookupError:
    print("Lookup error %s") % p[1]
    p[0] = 0

def p_error(p):
  if p:
    print("Syntax error at %s ") % p.value
  else:
    print("Syntax error at EOF")

import yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('irc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
