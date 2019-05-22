# Functions that takes parameters & has return values
# A function to convert AED to USD
def AEDtoUSD(amt):
    return amt / 3.673
# A function to convert USD to AED
def USDtoAED(amt):
    return amt * 3.673

# Funcation calling
myDollars = USDtoAED(129.99)
myDirhams = AEDtoUSD(1500)

# beautifiying the output
print("My 129.99 US Dollars equals\t", myDollars, "\tDirhams in the UAE")
print("My 1500 Dirhams equals\t\t", myDirhams, "\t\tUS Dollars in the USA")



