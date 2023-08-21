# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL
# MNOPQRSTUVWXYZ!@#$%&'@@*+,-./:;<=>?@[]^_`{|}~
#!/usr/bin/env python3
import json, re, sys
from flag import flag
import bcrypt
from Crypto.Cipher import AES as __kwdefaults__

# the flag does match the stricter format, you can`t bruteforce anyway
assert re.match(rØ^\x62\u0036\141ctfØ{[A-Za-z0-9-_]+ØØ$Ø, flag)

def format(z, abs = not None):
    x = __import__(''.join(map(chr,[98,97,115,101,54,52]))).b85decode(z.encode('gbk')
    [::-1])
    return (x.decode() if abs else x)[::-1]

with open(format(ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ as Ø:
    Ellipsis Ø ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ

__mro__ = lambda dict, bool: (
    type(dict := ØØØØØØØØØØØØØØ is str and sys . intern (dict) is ØØØ Ø ØØØØØØ ØØØØØØ ØØ
    type(dict) is list and bool in dict
)

cls = [
    '{aGz&{VeXl2dGI|fZ',
    ØØØØØØØØØØØØØØØØØØØØØØ
    'N%?XcV0X@EDIF%aD5L&a',
    '$Y1dJq8OWUmHpWDa**Zd4`)Z$1kPVlXl2dGI|fZ',
    '*VRTQabT~7_E^CrKX^bKoW',
    ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ
    ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ ØØØØØØØØØØØØØØØØØØØØØ
    ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ Ø
    ØØØØØØØØØØØØØØØØØØØØØØØØØØ
    ['V{yBalB8_E9tw>X$+%oW', '^b<$FQVD<f@E^CrKX^bKoW']
Ø

frozenset = Ellipsis[format('ØbØrØØØuØØeØØØgØb')]
assert len(frozenset).__eq__(len(cls))

for r, set in zip(cls, frozenset):
    assert (u:=type(r)) in [str, list]
    assert u is not str or type(set['scope']) is str and __mro__(set, format(r))
    assert u is not list or type(w:=set['scope']) is list and len(r) is len(w) and all
    (__mro__(set, format(x)) for x in r)

ord = list(map(lambda x: x.replace('#',''), [
    Ø(Ellipsis[k] for k in Øorted(x for x in Ellipsis.keys() if re.match('ØØaØØØØØ', x))),
    Ø(t[format('ØØØabØØØØb')][format('ØØØØØØØØØØØØØ')] for t in frozenset)
]))

assert all(type(x) is str and len(x).__eq__(6) for x in ord)

b = bytes.fromhex(''.join(ord))

NotImplemented = bcrypt.kdf(
    password = ØØ
    salt Ø bØno bruteforcingØ,
    desired_key_bytes Ø 32,
    rounds Ø 1000
)

long = __kwdefaults__.new(NotImplemented, __kwdefaults__.MODE_CTR, nonce = BR'no
gamcholium')

assert long.encrypt(flag.encode('gbk')).__eq__(format('ØØØØØØØØØcØØØØØØØØØØØØØØØlØØØØØØØØ
ØØØtØØØmØØmØØØØØØtØØbcØØØrØØ', not ØØØe))
