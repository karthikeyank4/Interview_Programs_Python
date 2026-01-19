
numbers =[1,2,5,5,6,7,8,3,2,1,4,3,4]
duplicates=[]
for num in numbers:
    if numbers.count(num)>1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)
