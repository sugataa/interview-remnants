from string import ascii_lowercase
from collections import OrderedDict

def MergeStrings(strings):
    d = OrderedDict((ch, 0) for idx, ch in enumerate(ascii_lowercase, 0))

    # build dict
    for given_str in strings:
        for char in given_str:
            if char in d:
                d[char] += 1

    # create str
    result = ''
    for k,v in d.items():
        print(k,v)
        result += k*v
    print(result)

MergeStrings(['2', 'ace', 'bdf'])
