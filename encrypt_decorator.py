import string
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

def encrypt(key):
    def accepter(func):
        def output_changer():
            return c_cypher(func(), key)
        return output_changer
    return accepter

@encrypt(2)
def get_low():
    return "Get get get low"

print(get_low())


