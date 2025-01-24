# Traffic lights.

lights = ["Red", "Yellow", "Green"]

currentLight = lights[0]

print(currentLight)

if currentLight == "Red":
    print("Stop!")
elif currentLight == "Yellow":
    print("Wait...")
else:
    print("Go!")