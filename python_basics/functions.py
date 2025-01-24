def greet(name = "user"):
    print("Hello, " + name + ".")
    
greet("Tufan")
greet()


def calculateArea(a,b):
    return a * b

area = calculateArea(5, 10)
print("Area: ", area)


calculateArea2 = lambda a,b : a*b
print(calculateArea2(2,4))