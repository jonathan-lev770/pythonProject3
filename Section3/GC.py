import ctypes
import gc


def ref_count(address):
    return ctypes.c_long.from_address(address).value


# method that tell us whether item exists in GC

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "object exists"
        return "not found"

# we are going to create a circular reference

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))

