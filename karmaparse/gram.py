import sys

from ply import yacc

from lexer import tokens

__all__ = ['tokens', 'parser']


things = {}


def p_statement(p):
    '''statement : expression'''
    p[0] = p[1]
    #  if p[2] not in things:
    #    things[p[2]] = 0
    #  print '%s : %d' % (p[2],things[p[2]])


def p_expression(p):
    """expression : KARMABOT COLON THING
                  | up
                  | down
                  """
    if len(p) == 4:
        p[0] = things.get(p[3], ' '.join((p[3], '(0)')))
    else:
        p[0] = p[1]


def p_up(p):
    '''up : THING PLUS PLUS'''
    p[0] = ''.join([p[1], '+', '+'])
    #  if p[2] not in things:
    #    things[p[2]] = 1
    #  else:
    #    things[p[2]] += 1


def p_down(p):
    '''down : THING MINUS MINUS'''
    p[0] = ''.join([p[1], '-', '-'])
    #  if [p[2]] not in things:
    #    things[p[2]] = -1
    #  else:
    #    things[p[2]] += -1


def p_error(p):
    if p:
        print("Syntax error at %r, %s ") % (p.value, p)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc(debug=True)


if __name__ == '__main__':
    import readline
    if sys.version_info.major >= 3:
        raw_input = input

    while 1:
        try:
            s = raw_input('irc > ')
            if s:
                output = yacc.parse(s)
                print output
        except EOFError:
            break
