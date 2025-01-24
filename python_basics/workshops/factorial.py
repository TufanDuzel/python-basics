number = int(input("Number: "))

factorial = 1

if (number < 0):
    print("Undefined.")
elif (number == 0):
    print(number)
else:
    for i in range(1,number + 1):
        factorial = factorial * i
            
print(factorial)