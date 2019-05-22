# strings as variables
fName = "Rami "
lName = 'Altai'

# strigns with quotes in them? escape the ' and the "
print('then she said "I\'m mad at you"\n')

# printing strings in the raw format
print(r"this\is\a\string\with\a\bunch\of\unescaped\special\characters")

# concatnating strigns
print("\n" + fName + lName + "\n")
# repeating a string
print(fName * 3 + "\n")

# Accessing a character from a string
fullName = fName + lName
print(fullName + "\nprints the whole thing\n")
print(fullName[5] + "\nprints char in index 5\n")
print(fullName[-1] + "\nprints last char")
print(fullName[:4] + "\nprints chars from beggining to 4\n")
print(fullName[5:] + "\nprints chars from 5 to the end\n")
print(fullName[::-1] + "\nreverse the string\n")
