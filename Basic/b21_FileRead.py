fileReading = open(r"C:\Users\Root\PycharmProjects\Beggining\FileManipulation\Written.txt", "r")

text = fileReading.read()
print(text)

fileReading.close()