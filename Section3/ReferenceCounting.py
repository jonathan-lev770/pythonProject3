# reference counting
import sys

a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))           # reference count is 2, 1 from when we built a, and then again when we call it)


import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))                 #1 b/c id(a) alreay recorded?

b = a
print(id(b))                            # same id as a
print(ref_count(id(a)))                 # now is 2, b/c now b has the same ref id

c = a
print(ref_count(id(a)))                 # now is 3, b/c now c has the same ref id

c = 10
print(ref_count(id(a)))                # changed value of c, now ref count back down to 2

b = None
print(id(b))                          # now id of b does not equal to a
print(ref_count(id(a)))               # back down to bc we changed b

a_id = id(a)
a = None
print(ref_count(a_id))                 # a points to non, a_id is equal to a, now has no ref count either





