short = {
    'CU' : 'see you',
    ':-)': 'I’m happy',
    ':-(': 'I’m unhappy',
    ';-)': 'wink',
    ':-P': 'stick out my tongue',
    '(~.~)': 'sleepy',
    'TA':	'totally awesome',
    'CCC':	'Canadian Computing Competition',
    'CUZ':	'because',
    'TY':	'thank-you',
    'YW':	'you’re welcome',
    'TTYL':	'talk to you later'
}

while True:
    value = input()
    print(short[value] if value in short else value)
    if value == 'TTYL':
        break