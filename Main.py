'''
Python Tic Tac Toe project
This is a two player game. Follow the instructions on the output to play the popular game: Tic Tac Toe

Designed by Akshaj
'''

from IPython.display import clear_output

# Declare all variables
startGame=False
xpos=0
opos=0
winner=False
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]

# Start Game
def welcome():
    global startGame
    print("Welcome to Tic Tac Toe. Please select User_1 (X) and User_2 (O)")
    print("Select Y to start game or N to exit")
    userChoice=""
    while userChoice not in ["Y","N"]:
        userChoice=input("Your choice (Y/N): ")
        if userChoice not in ["Y","N"]:
            clear_output()
            print("Incorrect Choice! Please choose Y to start or N to quit")
    if userChoice == "Y":
        startGame = True
        return startGame
    elif userChoice == "N":
        quit()

# Displaying the 3x3 grid
def displayGrid():
    global row1
    global row2
    global row3
    print(row1)
    print(row2)
    print(row3)

# Defining X Position and input from User
def Xposition():
    global xpos
    print("Choose X position from\n1 2 3\n4 5 6\n7 8 9")
    while xpos not in [1,2,3,4,5,6,7,8,9]:
        xpos=int(input("Enter X position (1-9): "))
        if xpos not in [1,2,3,4,5,6,7,8,9]:
            clear_output()
            print("Incorrect choice! Please choose from 1 to 9")


    return xpos

# O position input from USER
def Oposition():
    global opos
    print("Choose O position from\n1 2 3\n4 5 6\n7 8 9")
    while opos not in [1,2,3,4,5,6,7,8,9]:
        opos=int(input("Enter O position (1-9): "))
        if opos not in [1,2,3,4,5,6,7,8,9]:
            clear_output()
            print("Incorrect choice! Please choose from 1 to 9")
    return opos

# Placing the O at the desired position
def Oplacement():
    global row1
    global row2
    global row3
    global opos
    if opos in [1,2,3]:
        if opos==1:
            row1[0]="O"
            return row1
        elif opos==2:
            row1[1]="O"
            return row1
        elif opos==3:
            row1[2]="O"
            return row1
    elif opos in [4,5,6]:
        if opos==4:
            row2[0]="O"
            return row2
        elif opos==5:
            row2[1]="O"
            return row2
        elif opos==6:
            row2[2]="O"
            return row2
    elif opos in [7,8,9]:
        if opos == 7:
            row3[0] = "O"
            return row3
        elif opos == 8:
            row3[1] = "O"
            return row3
        elif opos == 9:
            row3[2] = "O"
            return row3


#Placing the X at the desired position
def Xplacement():
    global xpos
    global row1
    global row2
    global row3
    if xpos in [1,2,3]:
        if xpos==1:
            row1[0]="X"
            return row1
        elif xpos==2:
            row1[1]="X"
            return row1
        elif xpos==3:
            row1[2]="X"
            return row1
    elif xpos in [4,5,6]:
        if xpos==4:
            row2[0]="X"
            return row2
        elif xpos==5:
            row2[1]="X"
            return row2
        elif xpos==6:
            row2[2]="X"
            return row2
    elif xpos in [7, 8, 9]:
        if xpos == 7:
            row3[0] = "X"
            return row3
        elif xpos == 8:
            row3[1] = "X"
            return row3
        elif xpos == 9:
            row3[2] = "X"
            return row3

# Checking if there is a winner
def win():
    global row1
    global row2
    global row3
    global winner
    if (row1==["X","X","X"]) or (row2==["X","X","X"]) or (row3==["X","X","X"]) or (row1[0]==["X"] and
    row2[0]==["X"] and row3[0]==["X"]) or (row1[1]==["X"] and row2[1]==["X"] and row3[1]==["X"]) or (
    row1[2] == ["X"] and row2[2] == ["X"] and row3[2] == ["X"]) or (row1[0]==["X"] and row2[1]==["X"]
    and row3[2]==["X"]) or (row1[2]==["X"] and row2[1]==["X"] and row3[0]==["X"]):
        print("X is the winner!")
        winner=True
        return winner
    elif (row1==["O","O","O"]) or (row2==["O","O","O"]) or (row3==["O","O","O"]) or (row1[0]==["O"] and
    row2[0]==["O"] and row3[0]==["O"]) or (row1[1]==["O"] and row2[1]==["O"] and row3[1]==["O"]) or (
    row1[2] == ["O"] and row2[2] == ["O"] and row3[2] == ["O"]) or (row1[0]==["O"] and row2[1]==["O"]
    and row3[2]==["O"]) or (row1[2]==["O"] and row2[1]==["O"] and row3[0]==["O"]):
        print("O is the winner!")
        winner=True
        return winner
    else:
        pass

# Main code stiching all functions
def Main():
    global count
    global startGame
    global xpos
    global opos
    global winner
    global row1
    global row2
    global row3
    welcome()
    while winner==False:
        xpos=0
        opos=0
        print("X User's Turn")
        Xposition()
        Xplacement()
        displayGrid()
        win()
        print("O User's Turn")
        Oposition()
        Oplacement()
        displayGrid()
        win()
    print("Thank you for playing! To play again run code again.")

Main()