
'''
Using Python 2.7, or 3.3-3.5 syntax/semantics, please fill out the bodies of
the included functions to include implementations of what is described in the
docstrings.
'''

def list_of_integers():
    '''
    Returns a list of integers from 17 to 100 that are evenly divisible by 11.
    '''
    return [num for num in range(17, 100) if num%11==0]

def dict_mapping():
    '''
    Returns a dictionary mapping integers to their 2.75th root for all integers
    from 2 up to 100 (including the 2.75th root of 100).
    '''


def find_ips(inp):
    '''
    Returns a list of ip addresses of the form 'x.x.x.x' that are in the input
    string and are separated by at least some whitespace.
    >>> find_ips('this has one ip address 127.0.0.1')
    ['127.0.0.1']
    >>> find_ips('this has zero ip addresses 1.2.3.4.5')
    []
    '''
    is_ip = lambda f: lambda n:
    is_ip = list(filter(lambda x: lambda y: x.count('.')==3, inp.split()))
    return

def generate_cubes_until(modulus):
    '''
    Generates the cubes of integers greater than 0 until the next is 0 modulo
    the provided modulus.
    >>> list(generate_cubes_until(25))
    [1, 8, 27, 64]
    '''
    for val in range(fro, to + 1):
        yield val * val * val

def total_size(filenames):
    '''
    Given a list of filenames in Apache Common Log format, return a mapping
    of the total number of responses of different types to the total number of
    bytes returned by all responses of that type.
    >>> total_size(['/var/log/httpd.log', '/var/log/httpd.log.1'])
    {'200': 7362899, '404': 28710, ...}

    The format can be found: https://en.wikipedia.org/wiki/Common_Log_Format
    And an example line of common log format is:
    127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
    '''

def check_type(typ):
    '''
    Write a function decorator that takes an argument and returns a decorator
    that can be used to check the type of the argument to a 1-argument function.
    Should raise a TypeError if the wrong argument type was passed.
    >>> @check_type(int)
    ... def test(arg):
    ...   print arg
    ...
    >>> test(4)
    4
    >>> test(4.5) # raises TypeError because 4.5 isn't an int type
    '''
