
board =[]
def make_board(n):
    for i in range(n**2):
        board.append([])

def add_to_board(x,value):
    board [x].append(value)


def validBoardWithEmptyCells(n):
    flag=True
    for i in range(n**2):
        for j in range(n**2):
            flag=flag and int(board[i][j])<=n**2 and int(board[i][j])>=0
    
    for i in range(n**2):
        for j in range(n**2):
            for k in range(n**2):
                for l in range (n**2):
                    if (int(board[i][j])!=0):
                        if ((k==i and j == l)): 
                            flag= flag
                        elif(k==i and int(board[i][j])==int(board[k][l])):# rows
                            flag=False
                        elif (j== l and int(board[i][j])== int (board[k][l])):# columns
                            flag= False
                        elif(i//n==k//n and j//n==l//n and int(board[i][j])== int (board[k][l]) ):# blocks
                            flag= False
    
    return flag

def validBoard(n):
    flag=True
    for i in range(n**2):
        for j in range(n**2):
            flag=flag and int(board[i][j])<=n**2 and int(board[i][j])>0    # this will check domain
    
    for i in range(n**2):
        for j in range(n**2):
            for k in range(n**2):
                for l in range (n**2):
                    if (int(board[i][j])!=0):
                        if ((k==i and j == l)): 
                            flag= flag
                        elif(k==i and int(board[i][j])==int(board[k][l])): # this will check rows
                            flag=False
                        elif (j== l and int(board[i][j])== int (board[k][l])): # this will check columns
                            flag= False
                        elif(i//n==k//n and j//n==l//n and int(board[i][j])== int (board[k][l]) ):# this will check blocks
                            flag= False
    
    return flag 
def validSpot(i,j,value,n):
    flag=True
    temp=board[i][j]
    board[i][j]=value
    for k in range(n**2):
                for l in range (n**2):
                    if (int(board[i][j])!=0):
                        if ((k==i and j == l)): 
                            flag= flag
                        elif(k==i and int(board[i][j])==int(board[k][l])): # rows
                            flag=False
                        elif (j== l and int(board[i][j])== int (board[k][l])): # columns
                            flag= False
                        elif(i//n==k//n and j//n==l//n and int(board[i][j])== int (board[k][l]) ): # blocks
                            flag= False
    board[i][j]=temp
    return flag
def isEmptyCell(i,j):
    return int(board[i][j])==0

def findEmptyCells(n):          # this function will find empty cells from left to right top to buttom 
    for i in range(n**2):
        for j in range(n**2):
            if isEmptyCell(i,j):
                return i,j       
    return None

def backTracking(n):
    if  validBoard(n):              # check if this is a solution or not
        return True
    else:
        i,j=findEmptyCells(n)         # this will find the location of an empty cell
        for k in range(1,n**2+1):
            if validSpot(i,j,k,n): # this will test if the value going to make a valid state or not
                board[i][j]=k
                if backTracking(n):
                    return True
            
                board[i][j]=0
    return False
                     
def printBoard():
   for row in board:    
    for cell in row:    
        print(cell, end = " ")   
    print()  

def main():
    n= input("Enter the rank: ")
    n= int(n)
    make_board(n)

    for i in range(n**2):
        for j in range(n**2):
            x= input("Enter a value:")   # values to be enterd left to right top to buttom 
            add_to_board(i,x)            # note: 0 is to represent empty cells   
    if  backTracking(n):
        
        print("soulution is:")
        printBoard()
    else:
        print("unsolvable")
   
    
main()
