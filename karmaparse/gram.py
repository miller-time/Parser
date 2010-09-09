import sys

from ply import yacc

from lexer import tokens

__all__ = ['tokens', 'parser']


things = {}
descriptions = {}


helptext = ', '.join(("Usage: karmabot: help",
                      "karmabot: <thing>",
                      "karmabot: <thing> is <description>",
                      "<thing>++",
                      "<thing>--",
                      ))


def p_statement(p):
    '''statement : expression'''
    p[0] = p[1]


def p_expression(p):
    """expression : KARMABOT COLON HELP
                  | KARMABOT COLON THING
                  | KARMABOT COLON THING IS thinglist
                  | up
                  | down
                  """
    if len(p) >= 5:
        descriptions.update({p[3]: descriptions.get(p[3], []) + [p[5]]})
        p[0] = 'Okay.'
    elif len(p) == 4:
        if p[3] == "help":
            p[0] = helptext
        else:
            p[0] = "%s (%d): %s" % (p[3], things.get(p[3], 0),
                                    ', '.join(descriptions.get(p[3], [])))
    else:
        p[0] = p[1]


def p_up(p):
    '''up : THING PLUS PLUS'''
    things.update({p[1]: things.get(p[1], 0) + 1})
    p[0] = 'Done'


def p_down(p):
    '''down : THING MINUS MINUS'''
    things.update({p[1]: things.get(p[1], 0) - 1})
    p[0] = 'Done'


def p_thinglist(p):
    """thinglist : THING thinglist
                 | THING"""
    if len(p) == 3:
        p[0] = ' '.join((p[1], p[2]))
    else:
        p[0] = p[1]


def p_error(p):
    if p:
        print("Syntax error at %r, %s ") % (p.value, p)
    else:
        print("Syntax error at EOF - for help try 'karmabot: help'")


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
