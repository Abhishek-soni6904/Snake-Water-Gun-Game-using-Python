import random

# Define possible moves
move_list = ["Snake", "Water", "Gun"]

# Initialize variables
game_active = True
total_win = 0
total_lose=0
# Welcome message
print("Welcome to Snake, Water, Gun Game!")
print("===================================")

# Ask if user wants to play infinite or limited turns
while True:
    infinite_turns = input("\nDo you want to play an infinite number of rounds? (y/n): ").lower()
    if infinite_turns == "y":
        turns = -1  # Infinite rounds
        print("\nYou have chosen to play infinite rounds.")
        break
    elif infinite_turns == "n":
        turns = int(input("\nHow many rounds would you like to play? "))
        print(f"\nYou have chosen to play {turns} rounds.")
        break
    else:
        print("\nInvalid input! Please enter 'y' for yes or 'n' for no.")

# Main game loop
turn_count = 0
while game_active:
    user_move = None
    if turns != -1 and turn_count >= turns:  # Check if limited rounds have been completed
        break

    print(f"\nRound {turn_count + 1}")
    print("-------------------------")

    # Prompt user for move, with input validation
    while user_move not in move_list:
        user_move = input("Please enter your move (Snake, Water, Gun): ").capitalize()
        if user_move not in move_list:
            print("\nInvalid move! Please choose either 'Snake', 'Water', or 'Gun'.")

    # Generate computer's move
    computer_move = random.choice(move_list)
    print(f"\nYour move: {user_move}\nComputer's move: {computer_move}")

    # Determine the result of the round
    if computer_move == user_move:
        print("<---- It's a Draw ---->")
    elif (user_move == "Snake" and computer_move == "Water") or \
         (user_move == "Water" and computer_move == "Gun") or \
         (user_move == "Gun" and computer_move == "Snake"):
        print("Congratulations, you win this round!")
        total_win+=1
    else:
        print("Sorry, you lost this round.")
        total_lose+=1

    # For infinite turns, ask if the player wants to continue
    if turns == -1:
        while True:
            play_again = input("\nWould you like to play another round? (y/n): ").lower()
            if play_again == "y":
                break
            elif play_again == "n":
                print("\nThank you for playing! Goodbye.")
                game_active = False
                break
            else:
                print("\nInvalid input! Please enter 'y' for yes or 'n' for no.")
    
    # Reset user move for the next round and increment the turn count
    user_move = None
    turn_count += 1

# End game message
if turns != -1:
    print("\nYou've completed all your rounds! Thank you for playing. Goodbye!")
print(f"\nYour total wins = {total_win}\nYour total lose = {total_lose}")
print("\n************* Game Over *************")