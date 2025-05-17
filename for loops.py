fruits =["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for i in fruits:
    print(i)

for i in fruits:
    print(i + " pie")

# working with for loops with If statements.

for num in range (0, 100, 2):
    print(num)

for num in range(1,100):
    print(num)

# write a program that will loop through numbers
# confirm if it is divisible by 3, print fizz
# confirm if it is divisible by 5, print buzz
# confirm if it is divisible by both, print fizzbuzz

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

