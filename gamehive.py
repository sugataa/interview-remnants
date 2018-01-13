number = [8,9]
def add_one(number):
    i = len(number)-1
    carry = 1
    while(carry and i >= 0) :
        n = number[i]
        if n == 9:
            number[i] = 0
        else:
            number[i] = n + carry
            carry = 0
        i = i-1

    if carry == 1:
        number.insert(0, 1)
    return number

def add_one_negative(number):
    return [0] if number == [-1]
    i = len(number)-1
    carry = 1
    while(carry and i > 0) :
        n = number[i]
        if n == -1:
            number[i] = 0
        elif n == 0:
            number[i] = 9
        else:
            number[i] = n - carry
            carry = 0
        i = i-1

    if carry == 1:
        new_num = number[0] + 1
        if new_num == 0:
            del number[0]
            if len(number) > 0:
                number[0] = -number[0]
            else:
                number[0] = -number[-1]
        else:
            number.insert(0, new_num)
            del number[1]
    return number

# print(add_one(number))
number2 = [0]
print(add_one_negative(number2))
