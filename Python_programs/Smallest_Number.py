numbers =[12,3,2,10,9,8]
smallest_numbers=numbers[0]
for i in numbers:
    if i<smallest_numbers:
        smallest_numbers=i
print(smallest_numbers)