import string
import secrets
import re
import random
def generate(lent=8, num=2, low=2, up=2, spec=2):
    alt = string.ascii_letters + string.punctuation + string.digits
    while True:
        pasw = ''
        for _ in range(lent):
            pasw += random.choice(alt)
        
        cons = [
            (num, '\d'),
            (low, '[a-z]'),
            (up, '[A-Z]'),
            (spec, fr'[{string.punctuation}]')
        ]
        if all(
            con <= len(re.findall(pat, pasw))
            for con, pat in cons
        ):
            break
        name = re.search('Jesse', pasw)
        print(name)
    return pasw

print(generate(12))