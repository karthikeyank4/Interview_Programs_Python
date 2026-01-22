word ="python"
reverse=""
for i in word:
    reverse = i + reverse
if word ==reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")