"""
    Name: TTT_class.py
    Written by: Jessica Soler
    Date: 8/30/2024
    Purpose: Class file for tic tac toe game
"""

from rich.console import Console
from rich.text import Text

# create TTT class
class TTT:
    
    # initialize class
    def __init__(self):
        self.board = self.create_board()
        self.console = Console()
        self.human_player = 'X'
        self.computer_player = 'O'
        
    # create board
    # AI CODE SNIPPET
    def create_board(self):
        return [[' ' for _ in range(3)] for _ in range(3)]
    
    # display board
    def display_board(self):
        
        # clear the screen
        self.console.clear()
        
        # display title
        print("\n")
        title = Text("  Let's play", style="bold blue")
        self.console.print(title)
        subtitle = Text(" Tic Tac Toe!!", style="bold blue")
        self.console.print(subtitle)

        # column labels
        # AI CODE SNIPPET
        column_labels = Text("   A   B   C", style="bold red")
        self.console.print(column_labels)
        
        # row labels
        # AI CODE SNIPPET
        for i, row in enumerate(self.board):
            row_label = Text(f"{i + 1}", style="bold green")
            row_content = '|  '.join(row)
            self.console.print(row_label, Text(" "), Text(row_content))
            
            if i < 2:
                print("  -----------")
        print("\n")
        
    def player_move(self):
        # get player input
        move = input("Enter your move (Column: A B C & Row: 1 2 3)(Ex. B3): ")
        move = move.upper()
        
        #testing to see if the move
        print(move)
        
        # Define mappings for columns and rows
        # AI CODE SNIPPET
        # create a list of strings with the possible column lettters
        # create a list of strings with the possible row numbers
        columns = ['A', 'B', 'C']  # Column letters
        rows = ['1', '2', '3']     # Row numbers
        
        # check if input is valid
        # AI CODE SNIPPET
        if len(move) == 2 and move[0] in columns and move[1] in rows:
            # this determines if move index [0] is in the column list
            # this determines if move index [1] is in the row list
            # then assigns them to a variable
            column_letter = move[0]
            row_number = move[1]
            
            # extract column and row from the input
            # input is a string
            # first character is column
            # second character is row
            
            # convert column letter to a column index
            self.column_index = columns.index(column_letter)
            # convert row number to a row index
            self.row_index = rows.index(row_number)
        
            # check if selected cell is empty
            if self.board[self.row_index][self.column_index] == ' ':
                # place player's mark in the selected cell
                self.board[self.row_index][self.column_index] = self.human_player
            else:
                print("Cell is occupied. Try again.")
        
        else:
            print("Invalid move. Try again.")
                
                
    
    def add_game_piece(self):
        
        # place players mark in the selected cell
        self.board[self.row_index][self.column_index] = self.human_player
        
        # display the board
        self.display_board()
        
        
# TESTING:
# THIS WILL BE MOVED INTO ANOTHER FILE
# this code create and display a tic tac toe board

# thoughts-- when I set the game up the way I do below, it doens't produce an error when I chose the same cell twice
# I need to add_game_piece into the player_move function
# but first I need to convert to GUI and the player clicks on the cell instead of typing it in
# orrr do I figure out this logic first using rich and then convert?

game = TTT()
game.display_board()
game.player_move()
game.add_game_piece()
game.player_move()
game.add_game_piece()

#TODO: create computer move logic




#TODO: game pieces, computer player, GUI, win/lose/draw conditions, play again, save game, load game, game history, game statistics, game options, game settings, game menu, game help, game about, game exit
#TODO: GUI: title, board, status, buttons, menu, dialog, message, input, output, image, sound, video, animation, timer, clock, progress bar, slider, scrollbar, window, screen, display, resolution, fullscreen, theme, style, font, color, size, position, layout, alignment, padding, margin, border, shadow, shape, icon, cursor, tooltip, help, about, exit