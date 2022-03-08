# FOR LOOP WITH FINAL RANGE

for i in range(10):                            # 0 - 9    auto-increment each time
    print(i)

print(" -----------   2  ------------------")

number = int(input("Enter your number: "))

for i in range(number):                       # 0 to one less than number (final is excluded)
    print(i)


print(" -----------  3  ------------------")


# FOR LOOP WITH INITIAL AND FINAL RANGE

for i in range(1, 10):                        # 1 - 9
    print(i)

print(" -----------  4  ------------------")

# FOR LOOP INCREMENT / DECREMENT

for i in range(1, 10, 2):                     # 1, 3, 5, 7, 9    (remember final is exlucded)
    print(i)

print(" -----------  5  ------------------")
for i in range(10, 1, -2):                    # 10, 8, 6, 4, 2   (remember final is excluded)
    print(i)


print(" -----------  6  ------------------")
# LOOPS WITH VALUES IN LIST OR TUPLES (FOR EACH LOOP)

list1 = [1, 3, 5, 7, 10, 20]

for i in list1:                                       # prints EVERY element in the list
    print(i)

print(" -----------  7 ------------------")
for i in "Testing":                                   # prints EVERY element in the list
    print(i)

# List with multiple numeric values

print(" -----------  8  ------------------")
list2 = [45, 56, 34, 45, 77]
z = 0

for i in list2:
    z = z + i

print("Sum is: " + str(z))                           # need to print outside the for each loop (or else too many times)

print(" -----------  9  ------------------")
# for each loop with tuple
tuple1 = (1, 3, 5, 7, 9)

for i in tuple1:
    print(i)


print(" -------------  10  ---------------")

# ELSE STATEMENT CAN BE PART OF A FOR LOOP!

for i in range(1, 11):
    print(i)
else:
    print("else statements can be part of for loops")


