tupleType = (2, 4, "Berlin", (1, 2, 3), [])
listType = [2, 4, "Berlin", ()]

listType[0] = 6
print(listType[0])
# tupleType[0] = 6
print(tupleType[0]) 

print(tupleType[-2])

print(tupleType[1:2])
print(listType[1:2])

tupleValue = ("Tufan",)
print(type(tupleValue))