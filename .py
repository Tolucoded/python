# What this is: Nested if statement.
# Define score 
# Define age 

score = input("What was your test score? ")
score = int(score)

if score >= 90:
    age = int(input("what is your age? "))
    if age <= 10:
        print("You got an A+ based on your age")
    elif age > 10:
        print("You got an A, congrats!")
elif score >= 80:
    age = int(input("what is your age? "))
    if age <= 10:
        print("You got an B+ based on your age")
elif score >= 70:
    age = int(input("what is your age? "))
    if age <= 10:
        print("You got an C+ based on your age")
elif score >= 60:
    print("You got a D, do better next time!")
else:
    print("you didnt pass, try again next year!")
