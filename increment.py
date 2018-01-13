# Technical test
# Instructions:
# You have one hour to solve the problem
# Use python as the language
# Use basic python library ONLY
# You cannot search answers on the internet
# Upon completion, send the increment_YourName.py back with this email.

# Tips:
# Use the test function to verify your code
# You can write helper functions to solve the problem.
# Write clean & readable code with commentaries where necessary

# Problem:
# Let integers be represented as lists, where the first item of the list is the most significant digit,
# and the last item of the list is the least significant digit.
#
# For example, 13 would be represented as [1, 3]. 514 would be represented as [5, 1, 4].
# -8142 would be represented as [-8, 1, 4, 2].
#
# Implement a function increment() which, given an integer as represented above, returns the integer incremented by one.
#
# For example:
#  - Given the input [1, 5, 4] it should return [1, 5, 5]
#  - Given the input [-1, 0] it should return [-9]
#  - Given the input [2, 9, 9, 9] it should return [3, 0, 0, 0]
#
# A few pytest-style test cases have been provided in test_increment.py. Feel free to add your own to ensure that your
# implementation works as expected.
#
# Avoid trivial but inefficient solutions, such as converting the elements in the list to strings:
#
# def inefficient_solution(integer):
#     # This doesn't even pass all the tests
#     strings = [str(i) for i in integer]
#     to_int = int(''.join(strings))
#     to_int += 1
#     return [int(i) for i in str(to_int)]
#

def increment_positive(integer):
    idx = len(integer) - 1
    carry = 1
    while carry and idx >= 0:
        val = integer[idx]
        if val == 9:
            integer[idx] = 0
        else:
            integer[idx] = val + carry
            carry = 0
        idx -= 1

    if carry > 0:
        integer.insert(0, 1)
    return integer

def increment_negative(integer):
    if integer == [-1]:
        return [0]
    idx = len(integer) - 1
    carry = 1
    while carry and idx > 0:
        val = integer[idx]
        if val == -1:
            integer[idx] = 0
        elif val == 0:
            integer[idx] = 9
        else:
            integer[idx] = val - carry
            carry = 0
        idx -= 1

    if carry == 1:
        new_num = integer[0] + 1
        if new_num == 0:
            del integer[0]
            if len(integer) > 0:
                integer[0] = -integer[0]
            else:
                integer[0] = -integer[-1]
        else:
            integer.insert(0, new_num)
            del integer[1]
    return integer

def increment(integer):
#     # This doesn't even pass all the tests
    strings = [str(i) for i in integer]
    print(''.join(strings))
    to_int = int(''.join(strings))
    to_int += 1
    return [int(i) for i in str(to_int)]
