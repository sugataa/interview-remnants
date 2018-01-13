def bottle_caps():
    n = int(input().strip())
    for i in range(n):
        values = input().strip().split()
        cash = int(values[0])
        cost = int(values[1])
        caps = int(values[2])

        beer_from_cash = cash/cost
        print(int(beer_from_cash + beerFromCaps(beer_from_cash, caps)))

def beerFromCaps(curr, needed):
    if curr >= needed:
        new_beer = curr/needed
        leftover = curr%needed
        return new_beer + beerFromCaps(new_beer+leftover, needed)
    return 0

bottle_caps()
def _panagram(sentence):
    import string
    # build map
    d = {}
    for char in string.ascii_lowercase:
        d[char] = 1

    # go through sentence
    for char in sentence:
        if char.lower() in d:
            d[char.lower()] -= 1

    # check if any missing letters
    for k,v in d.items():
        if d[k] > 0:
            return False
    return True

def panagram():
    while True:
        n = input().strip()
        if n:
            print(_panagram(n))
        break

# panagram()
