import random

def randomwords():
    words=['alice','wonder','land','fajar','silsal','janaki','veendum']
    word = random.choice(words)
    return word

value=randomwords()
name=input("Enter your name?:")
print(f"welcome to word guessing game {name}")
max_attempts=0
max_attempts_allowed =6
while max_attempts<max_attempts_allowed:
    guess=input("enter your guess:?")
    max_attempts+=1
    if guess==value:
        print(f"congratulations,you attempt{max_attempts}")
        break
    else:
        print("You are wrong")
        
    
if guess!=value:
        print(f"sorry,yournumber of attempts{max_attempts},the correct word is {value}")
    

print("game is over")