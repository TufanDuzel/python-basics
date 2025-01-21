customerSet = {"Ross", "Chandler", "Joe"}

for customer in customerSet:
    print(customer)
    
customerSet.add("Monica")
print("Monica" in customerSet)

customerSet.update(["Rachel", "Phoebe"])

customerSet.remove("Chandler")
customerSet.discard("chandler")

print(len(customerSet))

customerSet.clear()
print(customerSet)

del customerSet
# print(customerSet)