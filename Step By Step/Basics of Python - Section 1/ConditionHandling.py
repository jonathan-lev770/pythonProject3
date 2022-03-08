# take input from user - number
# check if number is even, print the number
# if not even, don't do anything

number = int(input("choose a number: "))

if number % 2 == 0:
    print(number)

if number % 2 == 0:
    print("even number")
else:
    print("odd number")

if number < 0:
    print("negative")
elif number == 0:
    print("number is 0")
elif number % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# NESTED CONDITION

# take 1 input from user (Numeric)
# check if number is negative or positive
# if neg, display "it's neg", is positive, check number is even or odd

new_number = int(input("Choose a number"))

# approach 1
if new_number < 0:
    print("it's neg")
else:
    if new_number % 2 == 0:
        print("it's even")
    else:
        print("it's odd")


# approach 2
if new_number >= 0:
    if (new_number % 2 == 0):
        print("this is even")
    else:
        print("this is odd")
else:
    print("this is negative")


# take a marks from user and check if number is > 100 or < 0, this is invalid marks
# if number is in between 0 and 100, then display valid marks

marks = int(input("Please enter subject marks: "))


if marks > 100 or marks < 0:
    print("invalid marks")
else:
    print(marks)






