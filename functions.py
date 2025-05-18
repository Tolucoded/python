choice = int(input("what number would you like to choose? "))

def function(choice):
    for num in range (1, choice):
        if num % 3 ==0 or num % 5 == 0:
            print("Divisible!")
        else:
            print(num)

function(choice)


# Create a program that can take in input asking for the user's name.
# save the name of the variable.
# Pass the variable through a function and print "Hello..."

name = input("What is your name? ")
def greeting(name):
    print(f"Welcome to Tocoded academy, {name}")
    
greeting(name)

# Let's go cyber
# We want to use this for reconnaisance
ip = input("WHat is the target ip address? ")

def nmap(ip):
    print(f"targetting the ip {ip}")
    
nmap(ip)