from typing import List 
boardcnt = 0
def IsBoardOk (chessboard : List, row : int, col : int) :
   for c in range(col) :
       if (chessboard[row][c] == 'Q') :
           return False
   for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)) :
       if (chessboard[r][c] == 'Q') :
           return False
   for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)) :
      if (chessboard[r][c] == 'Q') :
          return False
   return True
def DisplayBoard (chessboard : List) :
    for row in chessboard :
        print(row)
def PlaceNQueens (chessboard : List, col : int) :
    global boardcnt
    if (col >= len(chessboard)) :
        boardcnt += 1
        print("Board " + str(boardcnt))
        print("==========================")
        DisplayBoard(chessboard)
        print("==========================\n")
    else :
        for row in range(len(chessboard)) :
            chessboard[row][col] = 'Q'
            if (IsBoardOk(chessboard, row, col) == True) :
                PlaceNQueens(chessboard, col + 1)
            chessboard[row][col] = '.'; # As previously placed queen was not valid, restore '.'

def main() :
   chessboard = []
   N = int(input("Enter chessboard size : "))
   for i in range(N) :
       row = ["."] * N
       chessboard.append(row)
   PlaceNQueens(chessboard, 0)
if __name__ == "__main__" :
    main()
