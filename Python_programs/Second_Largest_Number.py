
# Second largest number

number=[11,12,23,45,89,90,1000]
largest=number[0]
second_Largest=number[0]
for num in number:
    if num>largest:
        second_largest=largest
        largest=num
print("The  largest number is:",largest)
print("The second largest number is:",second_largest)


