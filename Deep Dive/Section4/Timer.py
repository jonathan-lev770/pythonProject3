import time
from datetime import datetime


# create function that times  how long a function takes to run
# note the function's arguments take a function name (which is an object), and collects positionals and keywords
# args in a tuple, kwargs result in dictionary

def time_it(fn, *args, **kwargs):
    print(args, kwargs)


time_it(print, 1, 2, 3, sep=' - ', end=' *** ')


def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)


time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)

# COMPUTER_POWERS FUNCTIONS DIDN'T WORK.    :  (

def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n ** i)
        return results


compute_powers_1(2, end=5)


def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n ** i for i in range(start, end)]


compute_powers_2(2, end=5)


def compute_powers_3(n, *, start=1, end):
    # using generator expressions
    return (n ** i for i in range(start, end))


##########################################################

print(datetime.utcnow())


# bc we put the default value inside defining the function, the memory location of that date/time stays same always

def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))


log('message 1', dt='2010-01-01 00:00:00:.000')

log('message 2')

log('message 3')


# now we set dt=None, which is not going to save memory location and the date/time will change when function called,
# EXCEPT IT DIDN'T WORK, same time saved
def log(msg, *, dt=None):
    if not dt:
        dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))


log('message 4')
log('message 5')
