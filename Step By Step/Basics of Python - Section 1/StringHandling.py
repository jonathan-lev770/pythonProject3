# this method is good for paragraphs

multiline_data = '''
    This is line 1
    This is line 2
    This is line 3

'''
print(multiline_data)


# must use double quotes if you have an ' in the string

sentence = "It isn't hot outside"
print(sentence)


# concatenation

a = "Hello"
b = "World"
print(a + " " + b)

name = "Jonathan"
phone = 7706057580

print("Welcome, your name is " + name + " your number is " + str(phone))


# you can use * to multiply a string like printing it 3 times

print(name * 3)


# Substrings

data2 = "This is Testing World"

print(data2[1])                  # h
print(data2[0:4].upper())        # THIS
print(data2[8:].lower())         # testing world
print(data2[:7])                 # This is


# Common String Operations

data3 = "This is my string"
print(len(data3))                 # 17
print(data3.upper())
print(data3.lower())


# Initialize first character to Upper case
data4 = "this is another string"
print(data4.capitalize())                        # This is another string














