#  Copyright (c) 2019.
#  Author : Samsul Ma'arif <samsulma828@gmail.com>

import base64

def enc(x):
    key = "secret"
    while len(x) > len(key):
        key += key
    result = []
    for i in range(len(x)):
        decimal = ord(x[i])
        decimalKey = ord(key[i])
        xorFusion = decimal ^ decimalKey
        result.append(chr(xorFusion))
    res = str("".join(result))
    encoded = res.encode()
    res = base64.b64encode(encoded).decode()
    return res

def decr(x):
    x = base64.b64decode(x).decode()
    key = "secret"
    while len(x) > len(key):
        key += key
    result = []
    for i in range(len(x)):
        decimal = ord(x[i])
        decimalKey = ord(key[i])
        xorFusion = decimal ^ decimalKey
        result.append(chr(xorFusion))
    res = str("".join(map(str, result)))
    return res

word = "hei world, what's up"
result = enc(word)
print("your word encrypted : ", result)
back = decr(result)
print("your word decrypted : ", back)