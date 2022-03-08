# list
a = [1, 2, 3]

# lists are implicitly multiple lines so you can write it like this
a = [1, 2,
     3, 4, 5]

# you can add comments to implicit multi-line list
a = [1,  # item1
     2,  # items2
     3]

# same thing with tuples
b = (1,  # item1
     2,  # item2
     3)

# same thing with dictionaries
c = {'key1': 1,  # value for key 1
     'key2': 2,  # value for key 2
     'key3': 3}  # value for key 3


# parameters in functions can be implicit multi line
def my_func(x,
            y,
            z):
    print(x + y + z)


# calling a function can be implicit multi line

my_func(10, 20, 30)  # normal
my_func(10,  # implicit multi line, good if function has lots parameters, connecting to database or server
        20,
        30)
my_func(10,  # comment 1
        20,  # comment 2
        30)  # comment 3

# explicit using \

a = 10
b = 20
c = 30

if a > 5 \
        and b > 10 \
        and c > 20:
    print('yes')

#  multi line string, don't try to line it up like I did below, b/c it printed extra spaces
a = '''this is a string'''
b = '''this
       is a string'''

print(b)


def my_func2():
    a = '''a multi-line string
     that is idented in the second line and wouldn't look good'''
    print(a)


lambda x: x ** 2
fn1 = lambda x: x ** 2
print(fn1(2))

min_length = 2
name = input("Enter your name")

while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Enter your name")

print("Hello, {0}".format(name))

l = [1, 2, 3]
val = 10
idx = 0

while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)

a = 10
b = 0

try:
    a / b
except ZeroDivisionError:
    print("cant divide by zero")
finally:
    print("finally always executes")

a = 0
b = 2

while a < 4:
    print("-----------------")
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0".format(a, b))
        continue
    finally:
        print("{0}, {1} - always executes".format(a, b))

    print("{0}, {1} - main loop".format(a, b))

s = 'hello'
for i in s:
    print(i)

s = 'hello'

for i in range(len(s)):
    print(i, s[i])

s = 'hello'

for i, c in enumerate(s):
    print(i, c)


class Rectangle:
    def __init__(self, width, height):              # is like the constructor
        self.width = width                          # attributes/properties
        self.height = height

    def area(self):                                 # method
        return self.width * self.height

    def perimeter(self):                            # method
        return 2 * (self.width + self.height)

    def to_string(self):
        return 'Rectangle: width = {0}, height = {1}'.format(self.width, self.height)

    def __str__(self):
        return 'Rectangle: width = {0}, height = {1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)    #this shows you would build the object again?


r1 = Rectangle(10, 20)                                # instance of the class
r1.area()                                             # takes the object and calls the method


print(str(r1))                                        # Rectangle: width = 10, height = 20

# without __str__ dunder method, str(r1) would print out some memory address, same as this hex
print(hex(id(r1)))

print(r1.to_string())                                 # to string method created, so we can use the object to call it


# str by default, just looks at class and the memory address, so to overwrite it, adn provide our own definition of str
# we have special methods like  __str__   which is dunder str







