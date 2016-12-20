import string
import datetime
from functools import wraps

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
CAPITALS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cypher_letter(l, key):
    if l in CAPITALS:
        return CAPITALS[(string.ascii_uppercase.index(l) + key) % 26]
    elif l in LETTERS:
        return LETTERS[(string.ascii_lowercase.index(l) + key) % 26]
    return " "

def c_cypher(strr, key):
    res = ""
    for c in strr:
        res += cypher_letter(c, key)
    return res

def log(logfile):
    def accepter_outer(func_outer):
        @wraps(func_outer)
        def output_changer_2():
            result = func_outer()
            f = open(logfile, 'a')
            f.write("{0} was called at {1}\n".format(func_outer.__name__, datetime.datetime.now()))
            f.close()
            return result
        return output_changer_2
    return accepter_outer


def encrypt(key):
    def accepter(func):
        @wraps(func)
        def output_changer():
            return c_cypher(func(), key)
        return output_changer
    return accepter


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

print(get_low())

# Igv igv igv nqy
