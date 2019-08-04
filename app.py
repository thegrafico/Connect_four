"""
Tic tac toc game
Raul Pichardo
"""

class Board():
    def __init__(self, col, rows):
        self.board_bx_style = '0'
        self.board = [[ self.board_bx_style for x in range(col)] for r in range(rows)]
        self.option = '1'
        self.toggle_player(True)
        self.win = False
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
                    if self.board[i][j] == self.board_bx_style:
                        if self.player_red:
                            
                            #fill up the board
                            self.board[i][j] = 'R'
                            
                            #determine winning
                            self.winner(i, j, 'R','line')
                            self.winner(i, j, 'R','topline')
                            self.winner_stair(j, 'R','up')
                            # self.winner_stair(j, 'R','down')
                            
                            #toggle user
                            self.toggle_player()
                        else:
                            #fill up the board
                            self.board[i][j] = 'Y'

                            #determine winner
                            self.winner(i, j,'Y', 'line')
                            self.winner(i, j, 'Y','topline')
                            self.winner_stair(j, 'Y','up')
                            # self.winner_stair(j, 'Y','down')

                            #toggle user
                            self.toggle_player(True)
                    else:
                        #evaluate column
                        self.evaluate_column(j)
                    return
#---------------------------------------------------------------
    def evaluate_column(self, col_position):
        # print("evaluating the game")
        for i in range(len(self.board)-1, -1, -1):
            if self.board[i][col_position] == self.board_bx_style:
                # print('row', i, 'col', col_position, 'Value', self.board[i][col_position])
                if self.player_red:
                    #fill the board
                    self.board[i][col_position] = 'R'
                    
                    #verify is there is a winner
                    self.winner(i, col_position, 'R','line')
                    self.winner(i, col_position, 'R','topline')
                    self.winner_stair(col_position, 'R','up')
                    # self.winner_stair(col_position, 'R','down')

                    #change the player
                    self.toggle_player()
                else:
                    #fill the board with the Y
                    self.board[i][col_position] = 'Y'

                    #verify is there is a winner
                    self.winner(i, col_position,'Y', 'line')
                    self.winner(i, col_position, 'Y','topline')
                    self.winner_stair(col_position, 'Y','up')
                    # self.winner_stair(col_position, 'Y','down')
                    
                    #change the player
                    self.toggle_player(True)
                break

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
                            self.win = True
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
                            self.win = True
                    else:
                        count = 1
                        # print('count to zero', count)
                else:
                    count = 1
                    # print('Reset to zero', count)
#---------------------------------------------------------------
    def winner_stair(self, j, player, method):
        print('EVALUATING UP')
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == player:
                    print('Input: {}, i:{}, j:{}'.format(player, row, col))
                    self.up(row, col, player)
#---------------------------------------------------------------
    def up(self, i, j, player):
        count = 0
        plus = 0
        print('=======UP=========')
        for row in range(i, len(self.board)):
            if self.board[row][j-plus] == player:
                print("Value:{}, i:{}, j:{}, plus:{}".format(player, row, j-plus, plus))
                plus+=1
                count +=1

                if count == 4:
                    print("Winner is {} with {} in a row".format(player, count))
                    self.win = True
        print('=======UP=========')
#---------------------------------------------------------------

table = Board(6,5)

while table.option != '0' or not table.win:
    table.show_table()
    table.play()