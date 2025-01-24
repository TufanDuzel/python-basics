# Prime numbers.

number = int(input("Enter the number: "))

isPrime = True

for x in range(2, number):
    if (number % x) == 0:
        isPrime = False
        break
    
if isPrime:
    print("The number is prime.")
else:
    print("The number is not prime.")