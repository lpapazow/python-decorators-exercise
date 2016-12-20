import string
import inspect
import datetime

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
        def output_changer_2():
            called_functs = inspect.getouterframes(inspect.currentframe(), 3)
            piece_of_code = called_functs[1][4][1] # :((
            func_we_want = piece_of_code[6:len(piece_of_code) - 4] # :{{
            result = func_outer()
            f = open(logfile, 'a')
            f.write("{0} was called at {1}\n".format(func_we_want, datetime.datetime.now()))
            f.close()
            return result
        return output_changer_2
    return accepter_outer


def encrypt(key):
    def accepter(func):
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

