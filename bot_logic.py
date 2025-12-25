import random

def gen_pass(l):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    
    for i in range(l):
        password += random.choice(elements)
    return password
def gen_emoji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)
def coin_flip():
    flip = random.randint(0,2)
    if flip == 0:
        return ("ОРЁЛ")
    else:
        return ("РЕШКА")
