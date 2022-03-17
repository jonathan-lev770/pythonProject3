a = "Hello"
b = "Hello"

c = "  Hello"
d = "Hello    "


if (a == b):
    print("same")
else:
    print("not same")


if (c.strip() == d.strip()):
    print("same")
else:
    print("not same")                       # same but not same memory location in original form

print(id(a) == id(b))                        # same memory location
print(id(c) == id(d))                        #  not same, each has diff spaces so diff object in storage


# Case Insensitive Comparison

a1 = "Hello"
b1 = "hello"

if a.upper() == b.upper():
    print("this is same")

