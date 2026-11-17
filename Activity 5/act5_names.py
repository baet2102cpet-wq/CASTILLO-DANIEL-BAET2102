#DANIEL IVAN CASTILLO
#BAET 2102
#NAME REVERSER

names = []

for number in range(5):
    name = input("Enter name " + str(number + 1) + ": ")
    names.append(name)

print("Names in reverse order:", names[::-1])
print("Names in alphabetical order:", sorted(names))
print("Original list (unchanged):", names)
