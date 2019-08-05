"""
Connect Four Game
author: Raúl Pichardo
email: devpichardo@gmail.com
date: 8/4/2019
"""

#Class to make the board of the game
class Board():
    def __init__(self, col, rows):
        #initial state of the board is 0. can be changed by space or other char
        self.board_bx_style = '0'

        #making the board
        self.board = [[ self.board_bx_style for x in range(col)] for r in range(rows)]
        
        #initial state. state 0 is for exit the game
        self.option = '1'

        #Change the player
        self.toggle_player(True)

        #Game over var
        self.gameover = False
#---------------------------------------------------------------
    def toggle_player(self, player=False):
        """
        This function change the player. There are only two players.
        player: True for playar 'R', False for player 'Y'
        """
        if player: 
            print('Playing R')  
            self.player_red = True
            self.player_yellow = False 
        else:
            print('Playing Y')
            self.player_yellow = True
            self.player_red = False
#---------------------------------------------------------------
    def show_table(self):
        """
        This function show the board with all plays. Also shows the position in the board to play
        """
        board_position = [str(x) for x in range(1, len(self.board[0] ) + 1)]
        print("\n====SELECT POSITION TO PLAY====")
        print(board_position)
        print("\n===============================\n")
        for position, value in enumerate(self.board):
            print(value)
#---------------------------------------------------------------   
    def play(self):
        """
        Init the game
        """

        #wait for user input
        self.option = input("Enter position to play: ")       
        
        #Rows: start at the botton. This way we fill the botton first.
        for i in range(len(self.board)-1, -1, -1):

            #cols 
            for j in range(len(self.board[0])):

                #Comparing user position with cols in the board
                if int(self.option) == (j+1):

                    #Verify if the space is empty
                    if self.board[i][j] == self.board_bx_style:
                        
                        #verify player
                        if self.player_red:
                            
                            #fill up the board
                            self.board[i][j] = 'R'
                            
                            #determine winning
                            self.winner(i, j, 'R','line')
                            self.winner(i, j, 'R','topline')
                            self.winner_diagonal(j, 'R','up')
                            self.winner_diagonal(j, 'R','down')
                            
                            #Change player
                            self.toggle_player()
                        else:
                            #fill up the board
                            self.board[i][j] = 'Y'

                            #determine winner
                            self.winner(i, j,'Y', 'line')
                            self.winner(i, j, 'Y','topline')
                            self.winner_diagonal(j, 'Y','up')
                            self.winner_diagonal(j, 'Y','down')

                            #Change player
                            self.toggle_player(True)
                    else:
                        #evaluate column
                        self.evaluate_column(j)
                    return
#---------------------------------------------------------------
    def evaluate_column(self, col_position):
        """
        Determine if there is a empty space in a column. is there is any, fill up
        """

        #row, start at the botton
        for i in range(len(self.board)-1, -1, -1):

            #oly row change, col_pisition is the same for all conditions. 
            #We are only evaluating if there are any empty space in a column
            if self.board[i][col_position] == self.board_bx_style:
                
                #player Red
                if self.player_red:
                    #fill the board
                    self.board[i][col_position] = 'R'
                    
                    #verify is there is a winner
                    self.winner(i, col_position, 'R','line')
                    self.winner(i, col_position, 'R','topline')
                    self.winner_diagonal(col_position, 'R','up')
                    self.winner_diagonal(col_position, 'R','down')

                    #change the player
                    self.toggle_player()
                
                #player Yellow                
                else:
                    #fill the board with the Y
                    self.board[i][col_position] = 'Y'

                    #verify is there is a winner
                    self.winner(i, col_position,'Y', 'line')
                    self.winner(i, col_position, 'Y','topline')
                    self.winner_diagonal(col_position, 'Y','up')
                    self.winner_diagonal(col_position, 'Y','down')
                    
                    #change the player
                    self.toggle_player(True)
                break

#---------------------------------------------------------------
    def winner(self, i, j, player,method):
        """
        Determine if there is a winner
        """
        #Vertical Line
        if method == 'line':
            
            #determine a winner
            count = 1
            
            #row stay the same, only the column position change
            for value in range(1, len(self.board[i])):

                #if we found the player mark
                if self.board[i][value] == player:
                    
                    #evaluate the past position with the present position
                    if self.board[i][value-1] == self.board[i][value]:
                        count+=1
                        
                        #determine a winner
                        if count==4:
                            print('Winner is', player,count)
                            self.gameover = True
                
                    #Reset if the patther don't match
                    else:
                        count = 1

                #reset if found other player mark
                else:
                    count = 1
        
        #Horizontal Line
        elif method == 'topline':
            count = 1

            #Itetare in every row
            for value in range(1, len(self.board) ):
                
                #if found player mark
                if self.board[value][j] == player:
                    
                    #if the mark below is the same as the mark at the top
                    if self.board[value-1][j] == self.board[value][j]:
                        count+=1
                        
                        #Winner
                        if count==4:
                            print('Winner is', player,count)
                            self.gameover = True
                    #Reset
                    else:
                        count = 1
                #reset
                else:
                    count = 1
#---------------------------------------------------------------
    def winner_diagonal(self, j, player, method):
        """
        Determine if a player win but diagonal
        """
        #Iterate all over the board
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                try:
                    #if found player mark
                    if self.board[row][col] == player:
                        
                        #Call the function to determine the winner. if was diagonal up or diagonal down
                        self.up_down(row, col, player, method)
                except:
                    pass
#---------------------------------------------------------------
    def up_down(self, i, j, player, method):
        count = 0
        plus = 0

        #Iterate rows
        for row in range(i, len(self.board)):
            
            #Depending of the method we evaluated diagonal up or down. 
            col = j-plus if method=='up' else j+plus
            try:
                #Row stay the same, only col change. 
                if self.board[row][col] == player:
                    
                    #diagonal variable
                    plus+=1
                    
                    count +=1

                    #determine a winner
                    if count == 4:
                        print("Winner is {} with {} in a row".format(player, count))
                        self.gameover = True
            except:
                pass
#---------------------------------------------------------------

#Instance of the class. Board size 6 cols, 5 rows
table = Board(6,5)

#Condition to game over
while table.option != '0' and not table.gameover:
    table.show_table()
    table.play()

#show the last table of the game after game over
table.show_table()