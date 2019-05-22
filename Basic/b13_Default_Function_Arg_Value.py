def gender(sex="a hoe"):
    '''
    :param sex: 
    :return sex or def val: 
    '''
    print(sex)
    if (sex == "m") or (sex == "M"):
        ans = "You're A Male!"
    elif (sex == "f") or (sex == "F"):
        ans = "You're A Female!"
    elif sex == "a hoe":
        ans = "You're a HOE!"

    return ans


print(gender('m'))
print(gender('f'))
print(gender())
print(gender('F'))
print(gender('M'))