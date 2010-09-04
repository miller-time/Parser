import sys

from ply import yacc

from lexer import tokens

__all__ = ['tokens', 'parser']


things = {}
descriptions = {}


def p_statement(p):
    '''statement : expression'''
    p[0] = p[1]


def p_expression(p):
    """expression : KARMABOT COLON THING
                  | KARMABOT COLON THING IS thinglist
                  | up
                  | down
                  """
    if len(p) > 4 and p[4] == "is":
      result = ' '.join(p[5])
      if p[3] not in descriptions:
        descriptions[p[3]] = result
      else:
        descriptions[p[3]] += ', ' + result
      p[0] = 'Okay.'
    elif len(p) == 4:
      num = things.get(p[3], 0)
      desc = descriptions.get(p[3], '')
      p[0] = p[3]+'('+str(num)+')'+': '+desc
    else:
      p[0] = p[1]


def p_up(p):
    '''up : THING PLUS PLUS'''
    if p[1] not in things:
      things[p[1]] = 1
      descriptions[p[1]] = ''
    else:
      things[p[1]] += 1
    p[0] = 'Done'


def p_down(p):
    '''down : THING MINUS MINUS'''
    if p[1] not in things:
      things[p[1]] = -1
      descriptions[p[1]] = ''
    else:
      things[p[1]] += -1
    p[0] = 'Done'


def p_thinglist(p):
    """thinglist : THING thinglist 
                 | THING"""
    if len(p)<3:
        p[0] = [p[1],]
    else:
        p[0] = [p[1],] + p[2]


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
