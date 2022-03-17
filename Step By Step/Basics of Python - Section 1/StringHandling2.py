# Strip from left, right and both

data = "  Hello, this is Testing World  "
print(data)
print(len(data))  # 32
print(data.lstrip())  # "Hello, this....
print(len(data.lstrip()))  # 30
print(data.rstrip())  # ...Testing World"
print(len(data.rstrip()))  # 30
print(data.strip())  # removed spaces on both sides

# Advance String Operations

data2 = "Hello this is the testing world, this this"

data2 = data2.replace("is", "##", 2)                              # can pass the count to limit the replacement
print(data2)

data3 = "Hello this is the Testing World"
data3 = data3.replace("is", "IS".replace("IS", "$$$"))            # can do it twice
print(data3)

data3 = data3.replace(" ", "-")                                   # can replace spaces
print(data3)

# Find data in a string, will return the index

print(data3.find("t"))                                           # 6, t is the at index 6
print(data3.find("z"))                                           # -1 bc "z" is not there


# Split String

print(data3.split("-"))                                          # returns a list (just like java)
result_list = data3.split("-")                                   # can save into a list (obvi)


for data in result_list:
    print(data)                                                 # can loop through the list (printed each word)







