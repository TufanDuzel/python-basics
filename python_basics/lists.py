students = ["Tufan", "Rabia", "James"]

students[2] = "John"
print(students[2])

students.append("Ross")
print(students)

students.remove("John")
print(students)

# List constructor
cities = list(("London", "Roma", "Roma"))
print("Length of cities list: " + str(len(cities)))

#print(cities.clear())
#print(len(cities))

print("How many times was Roma used: " + str(cities.count("Roma")))

print("Index of Roma: " + str(cities.index("Roma")))

cities.pop(2)
print(cities)

cities.insert(0, "Istanbul")
print(cities)

cities.reverse()
print(cities)

cities.sort()
print(cities)
