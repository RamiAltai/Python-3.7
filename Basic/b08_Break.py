# an example of the use of break
magicNumber = 26
i = 0

while i < 101:
    if i == magicNumber:
        print("your magic number is "+ str(i))
        break
    else:
        print("it's not "+ str(i))
    i += 1

# an example of the use of continue
