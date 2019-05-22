# defining lists
L1 = [5, 8, 2, 9]
print("\nmy first list")
print(L1)
L2 = [3, 9, 6, 4]
print("\nmy 2nd list")
print(L2)
# concatnating lists
L3 = L1 + L2
print("\nConcatnated lists")
print(L3)
# appending a value to a list
L1.append(999)
print("\nfirst list with appended value")
print(L1)
# deleting value
L1[0] = 0
print("\nfirst list with deleted first value")
# deleting range of values
L3[3:5] = []
print("\nlist 3 where elements from 3 to 5 deleted")
print(L3)
# deleting all elements of list
L3[:] = []
print("\nlist 3 emptied completely")
print(L3)
