import random
print("Number Guessing Game ......")
large = int(input("Enter the Largest Range : "))
small = int(input("Enter the Smallest Range : "))
number = random.randint(small,large)
count  = 0
while True:
    count+=1
    Guess = int(input("Guess A number "))
    if(Guess>number):
        print("Too large")
    elif(Guess<number):
        print("Too Small")
    elif(Guess == number):
        print("Congrats ! You Won in ", count," Tries")
        break
