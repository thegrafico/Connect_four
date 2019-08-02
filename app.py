"""
Tic tac toc game
Raul Pichardo
"""

class Board():
    def __init__(self, col, rows):
        self.board = [[ '0' for x in range(col)] for r in range(rows)]
        self.option = '1'
        self.toggle_player(True)
#---------------------------------------------------------------
    def toggle_player(self, player=False):
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
        for position, value in enumerate(self.board):
            if position == 0:
                print("SELECT POSITION:")
                for i in range(len(self.board[0])):
                    print( (i+1), end='     ')
                print("\n======================\n")
            print(value)
#---------------------------------------------------------------   
    def play(self):
        self.option = input("Enter position to play: ")       
        
        for i in range(len(self.board)-1, -1, -1):
            for j in range(len(self.board[0])):
                if int(self.option) == (j+1):
                    if self.board[i][j] == '0':
                        if self.player_red:
                            
                            #fill up the board
                            self.board[i][j] = 'R'
                            
                            #determine winning
                            self.winner(i, j, 'R','line')
                            self.winner(i, j, 'R','topline')
                            self.winner(i, j, 'R','upstair')
                            self.winner(i, j, 'R','downstair')
                            
                            #toggle user
                            self.toggle_player()
                        else:
                            #fill up the board
                            self.board[i][j] = 'Y'

                            #determine winner
                            self.winner(i, j,'Y', 'line')
                            self.winner(i, j, 'Y','topline')
                            self.winner(i, j, 'Y','upstair')
                            self.winner(i, j, 'Y','downstair')

                            #toggle user
                            self.toggle_player(True)
                    else:
                        #evaluate column
                        self.evaluate_column(j)
                    return

#---------------------------------------------------------------
    def winner(self, i, j, player,method):
        #normal line
        if method == 'line':
            count = 1
            for value in range(1, len(self.board[i]) ):
                if self.board[i][value] == player:
                    # print(value)
                    if self.board[i][value-1] == self.board[i][value]:
                        count+=1
                        # print(count)
                        if count==4:
                            print('Winner is', player,count)
                    else:
                        count = 1
                        # print('count to zero', count)
                else:
                    count = 1
                    # print('Reset to zero', count)
        #Top line
        elif method == 'topline':
            count = 1
            for value in range(1, len(self.board) ):
                if self.board[value][j] == player:
                    # print(value)
                    if self.board[value-1][j] == self.board[value][j]:
                        count+=1
                        # print(count)
                        if count==4:
                            print('Winner is', player,count)
                    else:
                        count = 1
                        # print('count to zero', count)
                else:
                    count = 1
                    # print('Reset to zero', count)
        #up stair
        elif method == 'upstair':
            count = 1
            plus = 0
            for pos in range(len(self.board)):
                try:
                    if self.board[pos][j-plus] == player:
                        # print('Value', self.board[pos][j-plus], "Position {} {}".format(pos, j-plus))
                        count +=1
                        plus +=1 

                        if count==4:
                            print('Winner is', player,count)
                    else:
                        # print('reset')
                        count=0
                        plus=0
                except:
                    pass
        elif method == 'downstair':
            count = 1
            plus = 0
            for pos in range(len(self.board)):
                try:
                    if self.board[pos][j+plus] == player:
                        # print('Value', self.board[pos][j+plus], "Position {} {}".format(pos, j+plus))
                        count +=1
                        plus +=1 

                        if count==4:
                            print('Winner is', player,count)
                    else:
                        # print('reset')
                        count=0
                        plus=0
                except:
                    print('out of range')
                    pass
#---------------------------------------------------------------
    def evaluate_column(self, col_position):
        # print("evaluating the game")
        for i in range(len(self.board)-1, -1, -1):
            if self.board[i][col_position] == '0':
                # print('row', i, 'col', col_position, 'Value', self.board[i][col_position])
                if self.player_red:
                    self.board[i][col_position] = 'R'
                    self.winner(i, col_position, 'R','line')
                    self.winner(i, col_position, 'R','topline')
                    self.winner(i, col_position, 'R','upstair')
                    self.winner(i, col_position, 'R','downstair')

                    self.toggle_player()
                else:
                    self.board[i][col_position] = 'Y'
                    self.winner(i, col_position,'Y', 'line')
                    self.winner(i, col_position, 'Y','topline')
                    self.winner(i, col_position, 'Y','upstair')
                    self.winner(i, col_position, 'Y','downstair')

                    self.toggle_player(True)
                break
#---------------------------------------------------------------

table = Board(6,5)

while table.option != '0':
    table.show_table()
    table.play()