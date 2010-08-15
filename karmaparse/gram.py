import sys

from ply import yacc

from lexer import tokens

__all__ = ['tokens', 'parser']


things = {}


def p_statement(p):
    '''statement : expression'''
    p[0] = p[1]


def p_expression(p):
    """expression : KARMABOT COLON THING
                  | KARMABOT COLON THING IS DESCRIPTION
                  | up
                  | down
                  """
    if len(p) > 4 and p[4] == "is":
      print 'So you want',p[2],' to be described as:'
      print ' '.join(p[5:])
      print 'Right?'
    if len(p) == 4:
      num = things.get(p[3], 0)
      p[0] = p[3]+'('+str(num)+')'
#    elif len(p) == 3:
#      num = things.get(p[2], 0)
#      p[0] = p[2]+'('+str(num)+')'
    else:
      p[0] = p[1]


def p_up(p):
    '''up : THING PLUS PLUS'''
    if p[1] not in things:
      things[p[1]] = 1
    else:
      things[p[1]] += 1
    p[0] = 'Done'


def p_down(p):
    '''down : THING MINUS MINUS'''
    if p[1] not in things:
      things[p[1]] = -1
    else:
      things[p[1]] += -1
    p[0] = 'Done'


def p_error(p):
    if p:
        print("Syntax error at %r, %s ") % (p.value, p)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc(debug=True)


if __name__ == '__main__':
    import readline
    if sys.version_info[0] >= 3:
        raw_input = input

    while 1:
        try:
            s = raw_input('irc > ')
            if s:
                output = yacc.parse(s)
                print output
        except EOFError:
            break
