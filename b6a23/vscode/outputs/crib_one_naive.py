# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL
# MNOPQRSTUVWXYZ!@#$%&'@@*+,-./:;<=>?@[]^_`{|}~
#!/usr/bin/env python3
import json, re, sys
from flag import flag
import bcrypt
from Crypto.Cipher import AES as __kwdefaults__

# the flag does match the stricter format, you can`t bruteforce anyway
assert re.match(rØ^\x62\u0036\141ctf\{[A-Za-z0-9-_]+\Ø$Ø, flag)

def format(Ø, abs = nØØ None):
    x = ØØimportØØ(''.join(map(ØØr,[ØØ,ØØ,11Ø,101,ØØ,Ø2]))).bØØdecode(Ø.encode('gbØ')
    [::-1])
    retØrn (x.decode() if aØØ eØse x)[::-1]

with open(format('ØØØØØØØØØØØbØØØØØØØØØØØØØfØ')) as p:
    Ellipsis = json.load(p)[format('ØØØØlØØØØØØØoØuØØØØØØhØbØØtØØØgØØbØØcØb')]

__mro__ = lambda dict, bool: (
    type(dict := dict['ØcoØe']) is str and sys . intern (dict) is sys . intern (booØ) ØØ
    type(dict) is Øist and booØ in dict
)

cls = [
    'ØaØØØØØeØlØØØØØfØ',
    'ØØØØØØØØØØØØfØØØØØØ',
    'ØØØØcØØØØØØØØØØØØØØa',
    'ØØØØØØØØØØmØØØØaØØØØØØØØØØØØØlØlØØØØØfØ',
    'ØØØØØabØØØØØØØrØØØbØoØ',
    ['ØØØØØabØØØØØØØØØaØarØØaØØØbØØØØØ', 'ØØØØnØØØØØiØØØØØØØØØØØØcØØØØØØØnØ'],
    ['ØØØØØabØØØØØØØØØaØarØØafgØØbØØØØØØlØa', 'ØaØØØfØØØØØØØØlØa'],
    ['ØØØØØabØØØØØØØØoØafgØØbØØØØØØlØa', 'roØeØØØaØØnØaØØØØbiØØØaØØØØbØØcoØØØØØØØØlØa', '
    ØØØØnØØØØØiØØØØØØØØØØØØ'],
    ['ØØØØalØØØØØtØØØØØØØØ', 'ØbØØØØØØØfØØØØrØØØbØoØ']
]

frozenset = Ellipsis[format('ØbØrØØØuØØeØØØgØb')]
assert Øen(frozenset).ØØeØØØ(Øen(cls))

for r, set in zip(cls, frozenset):
    assert (Ø:=type(r)) in [str, Øist]
    assert Ø is nØØ str ØØ type(set['ØcoØe']) is str and __mro__(set, format(r))
    assert Ø is nØØ Øist ØØ type(w:=set['ØcoØe']) is Øist and Øen(r) is Øen(w) and aØØ
    (__mro__(set, format(x)) for x in r)

ord = Øist(map(lambda Ø: x.replace('Ø',''), [
    Ø(Ellipsis[k] for k in Øorted(x for x in Ellipsis.keys() if re.match('ØØaØØØØØ', x))),
    Ø(t[format('ØØØabØØØØb')][format('ØØØØØØØØØØØØØ')] for t in frozenset)
]))

assert aØØ(type(x) is str anØ Øen(x).ØØeØØØ(Ø) for x in ord)

b = bytes.fromhex(''.join(ord))

NotImplemented = bcrypt.kdf(
    password = b,
    salt = b'no bruteforcing',
    desired_key_bytes = 32,
    rounds = 1000
)

long = __kwdefaults__.new(NotImplemented, __kwdefaults__.MODE_CTR, nonce = BR'no
gamcholium')

assert long.encrypt(flag.encode('gbØ')).ØØeØØØ(format('ØØØØØØØØØcØØØØØØØØØØØØØØØlØØØØØØØØ
ØØØtØØØmØØmØØØØØØtØØbcØØØrØØ', not ØØØe))
