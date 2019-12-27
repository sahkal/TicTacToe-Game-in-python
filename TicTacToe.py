#board

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
#display
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

winner=None
#whos turn
current_player="X"
game_still_going = True
#play game
def playGame():
  display_board()
  while game_still_going:
    handle_turn(current_player)
    check_if_gameOver()
    flip_Player()
  if winner=="X" or winner=="O":
    print(winner + " Won.")
  if winner==None:
    print("Tie.")

#handle turn
def handle_turn(player):
  position=input(current_player+" choose a position from 1-9")
  valid=False
  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position=input("Invalid input, choose a position from 1-9")
    position=int(position)-1
    if board[position] =="-":
      valid=True
    else:
      print("You cant do that!")
  board[position]=player

  display_board()
#check_game_status 
def check_if_gameOver():
  check_game_winner()
  check_game_tie()
#check winner
def check_game_winner():
  global winner
   #rows
  row_winner=check_row()
  diagonal_winner=check_diagonals()   
  column_winner=check_colums()
    
  #diagonals
  if row_winner:
    winner=row_winner
  elif diagonal_winner:
    winner=diagonal_winner
  elif column_winner:
    winner=column_winner
  else:
    winner=None
  #column
  return 
#checking rows
def check_row():
  global game_still_going
  row_1=board[0]==board[1]==board[2] !="-"
  row_2=board[3]==board[4]==board[5] !="-"
  row_3=board[6]==board[7]==board[8] !="-"
  if row_1 or row_2 or row_3:
    game_still_going =False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
#checking colums
def check_colums():
  global game_still_going
  column_1=board[0]==board[3]==board[6] !="-"
  column_2=board[1]==board[4]==board[7] !="-"
  column_3=board[2]==board[5]==board[8] !="-"
  if column_1 or column_2 or column_3:
    game_still_going=False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
#checking diagonals
def check_diagonals():
  global game_still_going
  diag_1=board[0]==board[4]==board[8] !="-"
  diag_2=board[2]==board[4]==board[6] !="-"
  if diag_1 or diag_2:
    game_still_going=False
  if diag_1:
    return board[0]
  elif diag_2:
    return board[2]

#check tie
def check_game_tie():
  global game_still_going
  if "-" not in board:
    game_still_going= False
    #print ("Tie")
  
#flip players
def flip_Player():
  global current_player
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"
  return
playGame()

#coded with love sahkal <3
#PS: My first try with python as a language for development