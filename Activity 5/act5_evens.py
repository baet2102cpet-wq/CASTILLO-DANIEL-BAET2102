#DANIEL IVAN CASTILLO
#BAET 2102
#EVEN NUMBERS FILTER

numbers = [12, 7, 9, 4, 15, 22, 31, 18, 6, 11]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Original list:", numbers)
print("Even numbers:", even_numbers)
