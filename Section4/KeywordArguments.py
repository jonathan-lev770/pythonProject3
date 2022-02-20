def func1(a, b, c):
    print(a, b, c)


# regular way to call it
func1(1, 2, 3)

# once you make a named argument, like c=3, then the rest have to be  named (UNLESS YOU USE * ARGS)
func1(1, c=3, b=2)


# *args allows more args to be called after a and b

def func1(a, b, *args):
    print(a, b, args)


func1(1, 2, 3, 4)  # a = 1, b =2, c = (3, 4)


def func1(a, b, *args, d):
    print(a, b, args, d)


# funct1(1 ,2, 3, 4, 5)   -- >   error, if you have * args, it has to be keyword after

func1(1, 2, 3, 4, d=5)


def func1(*args, d):  # put everything in args or nothing but d must be keyword
    print(args, d)


func1(1, 2, 3, d='a')
func1(d='a')  # no *args, just keyword d


def func(*, d):  # no positional args allowed bc of *
    print(d)


func(d=100)


# this one takes 2 positional args, then * for no more positional, then next has to be keyword parameter

def func(a, b, *, d):
    print(a, b, d)


func1(1, 2, d=100)


# we can use default values for positional params as well as keyword

def func(a, b=2, *args, d):  # when func is called, you don't have to call b
    print(a, b, *args, d)


func(1, 5, 3, 4, d='a')


def func(a, b=20, *args, d=0, e):
    print(a, b, *args, d, e)


func(5, 4, 3, 2, 1, e='all engines running')            # d would be 0, we didnt' need to call it


def func2(a, b=1, *, d, e=True):
    print(a, b, d, e)


func2(0, d=2)



