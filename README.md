Number Guessing Game:
An interactive command-line game where you try to guess a randomly generated number within limited attempts.

Description:
This is a Python-based guessing game that challenges players to find a secret number using strategic guessing and hints. The game offers three difficulty levels with varying number ranges and attempt limits. After each guess, the program provides feedback (too high or too low) to help narrow down the answer. This project demonstrates fundamental programming concepts including random number generation, loops, conditionals, input validation, and score calculation. It's perfect for beginners learning Python or as a portfolio project.

Game Rules:
Computer generates a random secret number
Player must guess the number within limited attempts
After each guess, receive "too high" or "too low" hints
Win by guessing correctly before attempts run out
Score is calculated based on attempts used

Features:
Three difficulty levels (Easy, Medium, Hard)
Different number ranges for each difficulty
Limited attempts based on difficulty
Hint system (too high/too low feedback)
Remaining attempts counter
Performance score calculation
Personalized gameplay with player name
Simple and engaging interface

How to Play:
1. Enter your name when prompted
2. Choose difficulty level (1-3)
3. Computer generates secret number
4. Enter your guess
5. Follow the hints (too high/too low)
6. Keep guessing until you win or run out of attempts
7. View your score and performance rating

Variables Used:
name - Player's name
d - Difficulty choice
mx - Maximum number range
att - Total attempts allowed
s - Secret number (randomly generated)
used - Attempts used to win
i - Current attempt counter
g - Player's guess
score - Performance score (0-100)

Main Components:
1. Welcome & Setup - Get player name and difficulty
2. Number Generation - Create random secret number
3. Game Loop - Process guesses with attempt limit
4. Hint System - Provide feedback (high/low)
5. Win Condition - Check if guess matches secret
6. Score Calculation - Rate player performance
7. Results Display - Show final outcome and score

Project Structure:
number_guessing/
│
├── guess_number.py        # Main game file
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
└── .gitignore            # Git ignore file

Test your guessing skills! Can you beat the computer?
