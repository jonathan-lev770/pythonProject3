# BREAK STATEMENT - LEAVE THE LOOP
for i in range(1, 11):
    if i == 5:
        break                                        # loops from 0 to 4 and breaks before it can print 5
    print(i)

number = int(input("enter a number"))

for i in range(1, 10):
    if i == number:
        break
    else:
        print(i)

# CONTINUE STATEMENT - SKIP REMAINING PART OF LOOP

num = int(input("enter a number"))

for i in range(1, 10):
    if i == num:
        continue                                        # prints everything except num
    else:
        print(i)





