from IPython.display import clear_output

# Declare all variables
startGame = False
xpos = 0
opos = 0
winner = False
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", ""]

# Start Game
def welcome():
    global startGame
    print("Welcome to Tic Tac Toe. Please select User_1 (X) and User_2 (O)")
    print("Select Y to start game or N to exit")
    userChoice = ""
    while userChoice not in ["Y", "N"]:
        userChoice = input("Your choice (Y/N): ")
        if userChoice not in ["Y", "N"]:
            clear_output()
            print("Incorrect Choice! Please choose Y to start or N to quit")
    if userChoice == "Y":
        startGame = True
        return startGame
    elif userChoice == "N":
        quit()

# Displaying the 3x3 grid
def displayGrid():
    global row1, row2, row3
    print(row1)
    print(row2)
    print(row3)

# Defining X Position and input from User
def Xposition():
    global xpos
    print("Choose X position from\n1 2 3\n4 5 6\n7 8 9")
    while True:
        try:
            xpos = int(input("Enter X position (1-9): "))
            if xpos not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                raise ValueError("Position should be between 1 and 9.")
            if is_position_taken(xpos):
                raise ValueError("Position already taken. Choose a different position.")
            break
        except ValueError as e:
            clear_output()
            print(f"Incorrect choice! {e}")

# O position input from USER
def Oposition():
    global opos
    print("Choose O position from\n1 2 3\n4 5 6\n7 8 9")
    while True:
        try:
            opos = int(input("Enter O position (1-9): "))
            if opos not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                raise ValueError("Position should be between 1 and 9.")
            if is_position_taken(opos):
                raise ValueError("Position already taken. Choose a different position.")
            break
        except ValueError as e:
            clear_output()
            print(f"Incorrect choice! {e}")
    return opos

# Check if the position is already taken
def is_position_taken(pos):
    global row1, row2, row3
    if pos in [1, 2, 3] and row1[pos - 1] != " ":
        return True
    elif pos in [4, 5, 6] and row2[pos - 4] != " ":
        return True
    elif pos in [7, 8, 9] and row3[pos - 7] != " ":
        return True
    return False

# Placing the O at the desired position
def Oplacement():
    global row1, row2, row3, opos
    if opos in [1, 2, 3]:
        row1[opos - 1] = "O"
        return row1
    elif opos in [4, 5, 6]:
        row2[opos - 4] = "O"
        return row2
    elif opos in [7, 8, 9]:
        row3[opos - 7] = "O"
        return row3

# Placing the X at the desired position
def Xplacement():
    global xpos, row1, row2, row3
    if xpos in [1, 2, 3]:
        row1[xpos - 1] = "X"
        return row1
    elif xpos in [4, 5, 6]:
        row2[xpos - 4] = "X"
        return row2
    elif xpos in [7, 8, 9]:
        row3[xpos - 7] = "X"
        return row3

# Checking if there is a winner
def win():
    global row1, row2, row3, winner
    for row in [row1, row2, row3]:
        if all(cell == "X" for cell in row):
            print("X is the winner!")
            winner = True
            return winner
        elif all(cell == "O" for cell in row):
            print("O is the winner!")
            winner = True
            return winner

    for col in range(3):
        if all(row[col] == "X" for row in [row1, row2, row3]):
            print("X is the winner!")
            winner = True
            return winner
        elif all(row[col] == "O" for row in [row1, row2, row3]):
            print("O is the winner!")
            winner = True
            return winner

    if all(row[i] == "X" for i in range(3)) or all(row[i] == "O" for i in range(3)):
        print("X is the winner!") if row[0] == "X" else print("O is the winner!")
        winner = True
        return winner

    if all(row[i] == "X" for i in range(2, -1, -1)) or all(row[i] == "O" for i in range(2, -1, -1)):
        print("X is the winner!") if row[2] == "X" else print("O is the winner!")
        winner = True
        return winner

    return False

# Main code stitching all functions
def Main():
    global startGame, xpos, opos, winner, row1, row2, row3
    welcome()
    while not winner:
        xpos = 0
        opos = 0
        print("X User's Turn")
        Xposition()
        Xplacement()
        displayGrid()
        if win():
            break
        print("O User's Turn")
        Oposition()
        Oplacement()
        displayGrid()
        if win():
            break
    print("Thank you for playing! To play again run code again.")

Main()
