def stupid_String(fW = "firstWordisDumb",
                  sW="secondWordIsStupid",
                  tW="thirdWordIsWeird"):
    ans: str = fW + sW + tW
    return ans

# Your don't have to pass all parameters.
# They don't have to be in the right order.

mySentance = stupid_String(sW="Ass Kisser", fW="You Are An")
print(mySentance)