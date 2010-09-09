from pprint import PrettyPrinter

from gram import parser


pp = PrettyPrinter(indent=4)


def do_parse(s):
    s = ' '.join(s.splitlines())
    print s

    result = parser.parse(s)
    pp.pprint(result)


if __name__ == '__main__':

    s = (
        """karmabot: millertime """,
        """millertime++""",
        """karmabot: millertime""",
        """millertime--""",
        """karmabot: millertime""",
        """karmabot: millertime is testing the parser""",
        """karmabot: millertime""",
        """karmabot: millertime!""",
        """karmabot: millertime is very excited!""",
        """karmabot: millertime""",
        """karmabot: millertime is punctuates.""",
        """karmabot: millertime.""",
        )
    for x in s:
        do_parse(x)
