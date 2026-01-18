# fizz - Its divisible by 3
#buzz -Its divisble by 5
# fizzbuzz - Its divisble by 3 & 5

# num =25
# if num%3==0:
#     print("Buzz")
# if num%5==0:
#     print("Fizz")
# if num%3==0 and num%5==0:
#     print("FizzBuzz")

for i in range(1,15):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)