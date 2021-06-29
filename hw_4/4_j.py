import sys


def allow_in_range(a : set, mode='loweralpha'):
    if mode == 'loweralpha':
        for i in range(ord('a'), ord('z') + 1):
            a.add(chr(i))
    elif mode == 'upperalpha':
        for i in range(ord('A'), ord('Z') + 1):
            a.add(chr(i))
    elif mode == 'numbers':
        for i in range(ord('0'), ord('9') + 1):
            a.add(chr(i))
    return a


def check_and_add(identifier: str):
    if set(identifier).difference(set('0123456789')):
        if (ord(identifier[0]) in list(range(ord('0'), ord('9') + 1)) and number_startable) or \
                (ord(identifier[0]) not in list(range(ord('0'), ord('9') + 1))):
            if not case_sensitive:
                identifier = identifier.lower()
            if identifier not in lang_keywords:
                if identifier not in vocab:
                    vocab[identifier] = 1
                else:
                    vocab[identifier] += 1


n, case_sensitive, number_startable = input().split()
n = int(n)
case_sensitive = (case_sensitive == 'yes')
number_startable = (number_startable == 'yes')

lang_keywords = set()
for _ in range(n):
    if case_sensitive:
        lang_keywords.add(input())
    else:
        lang_keywords.add(input().lower())
allowed_symbols = {'_'}
allow_in_range(allowed_symbols, mode='loweralpha')
allow_in_range(allowed_symbols, mode='upperalpha')
allow_in_range(allowed_symbols, mode='numbers')

vocab = {}
for line in sys.stdin.readlines():
    line = line.strip()
    identifier = ''
    for char in line:
        if char in allowed_symbols:
            identifier += char
        elif char not in allowed_symbols and identifier:
            check_and_add(identifier)
            identifier = ''
    if identifier:
        check_and_add(identifier)

max_count = 0
for key in vocab:
    if vocab[key] > max_count:
        max_count = vocab[key]
        res = key
print(res)