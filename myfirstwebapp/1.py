def myfunc(*args):
    for a in args:
        print(a, end =' ')
    if args:
        print()


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep= '->', end = ' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end =' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep = '->', end = '')
        print()


a = print(myfunc3(10, 20, 30, 40, 50))
b = print(myfunc3(a=10, b=20, c=30))