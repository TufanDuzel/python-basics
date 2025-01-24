x = 10
y = 20

print("Default value of X: " + str(x))
print("Default value of Y: " + str(y))

#x,y = y, x

#print("The new value of X: " + str(x))
#print("The new value of Y: " + str(y))

temp = x
x = y
y = temp

print("The new value of X: " + str(x))
print("The new value of Y: " + str(y))