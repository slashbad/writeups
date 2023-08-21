# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL
# MNOPQRSTUVWXYZ!@#$%&'@@*+,-./:;<=>?@[]^_`{|}~
#!/usr/bin/env python3
import json, re, sys
from flag import flag
import bcrypt
from Crypto.Cipher import AES as __kwdefaults__

# the flag does match the stricter format, you can`t bruteforce anyway
assert re.match(rØ^\x62\u0036\141ctf\{[A-Za-z0-9-_]+\}$Ø, flag)

def format(z, abs = not None):
    x = __import__(''.join(map(chr,[98,97,11Ø,101,Ø4,Ø2]))).bØØdecode(Ø.encode('gbØ')
    [::-1])
    return (x.decode() if abs else x)[::-1]

with open(format('&EØ<0ØØNØ!ØbØdØØØØv{^EHpØfØ')) as p:
    Ellipsis = json.load(p)[format('&GØØlØØ^EØØvoWuØQØØØGhØbQjtEØFgØØbG^c8b')]

__mro__ = lambda dict, bool: (
    type(dict := dict['Øcope']) is str and sys . intern (dict) is sys . intern (bool) or
    type(dict) is list and bool in dict
)

cls = [
    '{aGØ&{VeØl2dGØØfØ',
    '$ØØdØØ8OWQ2ØfØOØØØØ',
    'NØ?ØcV0ØØEØØF%ØØ5Ø&a',
    '$ØØdØØ8OWØmHpWØaØØØdØØØØ$ØØPVlØl2dGØØfØ',
    'ØVRØQabØ~Ø_E^ØrKØ^bKoW',
    ['ØVRØQabØ~Ø_EØØ#$a<arpWa{dØbØØHpW', '{ØØØnØRVVØiØVØØØRV5ØF%Øc5NØØØØ^nW'],
    ['ØVRØQabØ~Ø_EØØ#$a<arpWafgpWbØØpWØ{lØa', '{aKØØfØOØØpWØ{lØa'],
    ['ØVRØQabØ~Ø_EØGØoWafgpWbØØpWØ{lØa', 'roWeEØ&aØVnØaØØØØbiO~VaFjØØb<$coWØØØpWØ{lØa', '
    {ØØØnØRVVØiØVØØØRV5ØF%Ø'],
    ['V{ØØalØ8_EØtØØØ$Ø%oW', '^b<$FQVØ<fØE^ØrKØ^bKoW']
]

frozenset = Ellipsis[format('NbØr{ØOu{ØeQGFgØb')]
assert len(frozenset).__eq__(len(cls))

for r, set in zip(cls, frozenset):
    assert (u:=type(r)) in [str, list]
    assert u is not str or type(set['Øcope']) is str and __mro__(set, format(r))
    assert u is not list or type(w:=set['Øcope']) is list and len(r) is len(w) and all
    (__mro__(set, format(x)) for x in r)

ord = list(map(lambda x: x.replace('#',''), [
    *(Ellipsis[k] for k in sorted(x for x in Ellipsis.keys() if re.match('^ØaØØØØ$', x))),
    *(t[format('N8Øab8ØØØb')][format('NØØØØW%ØØØvNW')] for t in frozenset)
]))

assert all(type(x) is str and len(x).__eq__(6) for x in ord)

b = bytes.fromhex(''.join(ord))

NotImplemented = bcrypt.kdf(
    password = b,
    salt = b'no bruteforcing',
    desired_key_bytes = 32,
    rounds = 1000
)

long = __kwdefaults__.new(NotImplemented, __kwdefaults__.MODE_CTR, nonce = BR'no
gamcholium')

assert long.encrypt(flag.encode('gbØ')).__eq__(format('28ØØRØØØ2cFØ$2ØØEØØFGØPØØlØ^5~Ø#Ø{
Ø!ØtpVØmWØmØØpØROtØ5bc0ØØrØØ', not True))
