from tkinter import *
import random 

def next_turn(row, column):
    """
    Function to handle the next turn in the game.
    Updates the button text with the current player's symbol ('x' or 'o').
    Checks if there's a winner after the move.
    If there's a winner or a tie, it updates the label to display the result.
    Otherwise, it switches the player and updates the label to show the next turn.
    """
    global player

    # Check if the button is empty and no winner has been declared
    if buttons[row][column]['text'] == '' and not check_winner():
        buttons[row][column]['text'] = player  # Set the player's symbol on the button
        winner = check_winner()  # Check if this move resulted in a win or tie

        if winner == 'Tie':
            label.config(text='Tie!')  # Update label if the game is a tie
        elif winner:
            label.config(text=f'{player} wins')  # Update label if the current player wins
        else:
            # Switch player if no winner or tie
            player = 'x' if player == 'o' else 'o'
            label.config(text=f'{player} turn')  # Update label for the next player's turn

def check_winner():
    """
    Function to check if there's a winner or a tie.
    Checks rows, columns, and diagonals for three matching symbols in a line.
    Returns True if a player wins, 'Tie' if the game is tied, and False otherwise.
    """
    # Check rows for a win
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            return True 
    
    # Check columns for a win
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            return True
    
    # Check diagonals for a win
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    
    # Check for a tie if all spaces are filled
    elif empty_spaces() is False:
        return 'Tie'
    
    else:
        return False  # No winner and no tie, continue the game

def empty_spaces():
    """
    Function to check if there are any empty spaces left on the board.
    Returns False if there are no empty spaces (indicating a tie), and True otherwise.
    """
    spaces = 9  # Start with 9 empty spaces

    # Count how many spaces are still empty
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    
    return spaces != 0  # Return False if no spaces are left, otherwise return True

def new_game():
    """
    Function to start a new game.
    Resets the board, randomly chooses the starting player, and updates the label.
    """
    global player 

    player = random.choice(players)  # Randomly choose the starting player

    label.config(text=player+' turn')  # Update the label to show the starting player

    # Reset all buttons on the board to be empty with the default background color
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg="#F0F0F0")

window = Tk()
window.title('Tic-Tac-Toe')

# Initialize player list and randomly choose the starting player
players = ['x', 'o']
player = random.choice(players)

# Create a 3x3 grid of buttons for the tic-tac-toe board
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Create a label to display whose turn it is
label = Label(text=player + ' turn', font=('consolas', 40))
label.pack(side='top')

# Create a reset button to restart the game
reset_button = Button(text='restart', font=('consolas', 20), command=new_game)
reset_button.pack(side='top')

# Create a frame to hold the buttons (tic-tac-toe grid)
frame = Frame(window)
frame.pack()

# Initialize the buttons in the grid
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', font=('consolas', 40), width=5, height=2,
                                command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the main loop to run the application
window.mainloop()


