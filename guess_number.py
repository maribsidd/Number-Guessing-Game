"""
Number Guessing Game
Guess the secret number within limited attempts
"""

import random

print("=" * 50)
print("NUMBER GUESSING GAME")
print("=" * 50)
print()

name = input("Enter your name: ")
print(f"Welcome {name}!")
print()

# Difficulty selection
print("Choose difficulty:")
print("1. Easy (1-50, 10 attempts)")
print("2. Medium (1-100, 7 attempts)")
print("3. Hard (1-200, 5 attempts)")
print()

d = input("Enter choice (1-3): ")

if d == '1':
    mx = 50
    att = 10
    print("Easy mode selected!")
elif d == '2':
    mx = 100
    att = 7
    print("Medium mode selected!")
elif d == '3':
    mx = 200
    att = 5
    print("Hard mode selected!")
else:
    mx = 100
    att = 7
    print("Invalid choice! Default: Medium mode")

print(f"I'm thinking of a number between 1 and {mx}")
print(f"You have {att} attempts to guess it!")
print()

# Generate secret number
s = random.randint(1, mx)
used = att

for i in range(1, att + 1):
    print(f"Attempt {i}/{att}")
    g = int(input("Enter your guess: "))
    
    if g == s:
        print()
        print("*" * 50)
        print(f"Congratulations {name}!")
        print(f"You guessed it right! The number was {s}")
        print(f"You won in {i} attempts!")
        print("*" * 50)
        used = i
        break
    elif g < s:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
    
    if i < att:
        print(f"Attempts remaining: {att - i}")
    print()
else:
    print("=" * 50)
    print("Game Over!")
    print(f"You ran out of attempts!")
    print(f"The secret number was: {s}")
    print("Better luck next time!")
    print("=" * 50)

# Score
if used <= att:
    score = int((1 - (used - 1) / att) * 100)
    print(f"\nYour Score: {score}/100")
    
    if score >= 80:
        print("Performance: Excellent!")
    elif score >= 60:
        print("Performance: Good!")
    elif score >= 40:
        print("Performance: Average")
    else:
        print("Performance: Keep practicing!")

print("\nThanks for playing!")
