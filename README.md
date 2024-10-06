# Snake-Water-Gun-Game-using-Python

This is a simple Python implementation of the popular "Snake, Water, Gun" game. It allows you to play against the computer in either an infinite number of rounds or a limited number of rounds as chosen by the user.

## Game Rules
- **Snake** drinks **Water** → Snake wins.
- **Water** douses **Gun** → Water wins.
- **Gun** shoots **Snake** → Gun wins.
- If both the player and computer select the same move, it's a draw.

## Features
- Play an infinite number of rounds or set a specific number of rounds.
- The game keeps track of your total wins and losses.
- The user plays by inputting "Snake", "Water", or "Gun", while the computer randomly selects its move.
- After each round, the game shows the result and asks the user if they want to continue (for infinite mode).
- Displays final score after all rounds are completed.

## Requirements

To run this game, you need to have the following:

1. **Python 3.x** - The game is written in Python and requires Python 3.x to execute.
   - You can download the latest version of Python from [Python's official website](https://www.python.org/).
   
2. **Random module** - This is a built-in Python module, so no additional installation is required.

## How to Run

1. Make sure you have Python installed on your system.
2. Save the Python script (the code provided) in a `.py` file (e.g., `snake_water_gun.py`).
3. Run the Python file in your terminal or command line using:
   ```bash
   python snake_water_gun_game.py
