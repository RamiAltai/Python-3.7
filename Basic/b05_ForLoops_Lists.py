# for loops with lists
foodToBuy = ["tuna", "ham", "beef", "egg", "milk"]
stuffToSell = ["arts", "brush", "soil", "car", "couch"]
thingsToFix = ["your brain", "your sink", "your screen", "your tv!"]
my_Lists = [foodToBuy, stuffToSell, thingsToFix]

for list in my_Lists:

    print("Here We Go With another one\n")
    for item in list:

        print(item)
        print(len(item))

    print("moving on to the next list!\n")
