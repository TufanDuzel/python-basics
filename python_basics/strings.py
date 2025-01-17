# substring
message = "Hello world!"
print(message)

print(message[2:5])
print(message[:2])

word = message[6:]
print(word)

# len function
message2 = "Hello everyone, I'm Tufan."

character = message2[len(message2)-1:len(message2)]
print(character)

# lower and upper
print(message2.upper())
print(message2.lower())

# replace
newMessage = message2.replace("Hello", "Hi")
print(newMessage)

# split function
print(newMessage.split())
print(newMessage.split() [2])
print("Name = " + newMessage.split() [3])

# input
name = input("What is your name?")
print("Your name is " + name)

evenNumber = input("Even number: ")
oddNumber = input("Odd number: ")
print(int(evenNumber) + int(oddNumber))