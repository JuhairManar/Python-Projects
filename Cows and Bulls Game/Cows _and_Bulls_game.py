import random

secret_code=''.join(random.choice('0123456789') for _ in range(4))

Tries=2
print("Welcome to game of Cows and Bulls\nYou have 5 number of tries\nStart!!!")

while Tries:
    Guess=input("Guess a 4 digit number:")
    
    if(len(Guess)!=4):
        print("Enter a valid 4 digit number")
        continue
    
    bulls=0
    cow=0
    
    
    for i in range(len(Guess)):
        if(Guess[i]==secret_code[i]):
            bulls+=1
        elif Guess[i] in secret_code:
            cow += 1
            
    if bulls==4:
        print("You guessed right!")
        break
    
    print(f'Response: {bulls} bulls , {cow} cow --- you have {Tries-1} Tries left')
    Tries-=1