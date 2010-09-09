# first attempt to add a module - eightball

# the eightball lexer tokens

reserved = {
    'eightball': 'EIGHTBALL',
    }
    
tokens = tuple(reserved.values())

# the eightball parser functions

predictions = [ "As I see it, yes",
		"It is certain",
		"It is decidedly so",
		"Most likely",
		"Outlook good",
		"Signs point to yes",
		"Without a doubt",
		"Yes",
		"Yes - definitely",
		"You may rely on it",
		"Reply hazy, try again",
		"Ask again later",
		"Better not tell you now",
		"Cannot predict now",
		"Concentrate and ask again",
		"Don't count on it",
		"My reply is no",
		"My sources say no",
		"Outlook not so good",
		"Very doubtful"]

def p_eightball(p):
    """expression : KARMABOT COLON EIGHTBALL"""
    p[0] = random.choice(predictions) + "."
