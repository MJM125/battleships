from random import randrange

ship_initial = ["B", "C", "F", "A", "S"]
ship_names = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Sub"]
map_size = 10


def get_username():
    """
    function getting username for welcome message
    """
    while True:
        user_name = input("Enter your name: ")
        if user_name:
            print(f"Welcome to the battleship game {user_name}!")
            return user_name
        else:
            print("Please enter your name.")


def create_battlefield(map_size):
    """
    function to create a map based on size
    """
    return [["_"] * map_size for _ in range(map_size)]


def display_battlefield(board):
    """
    function to display current state of the map
    """
    for row in board:
        print(" ".join(row))


def player_ship_coordinate(player_board, occupied):
    """
    function for player placement ship
    """
    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))
            if 0 <= row < 10 and 0 <= 10 and (row, col) not in occupied:
                player_board[row][col] = "B"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct value.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

    while True:
            try:
                row = int(input("Enter the row for Battleship: "))
                col = int(input("Enter the column for Battleship: "))

                if 0 <= row < 10 and 0 <= 10 and (row, col) not in occupied:
                    player_board[row][col] = "C"
                    occupied.add((row, col))
                    break
                else:
                    print("Invalid coordinates. Please enter correct value.")
            except ValueError:
                print("Invalid Input. Please enter a valid number.")

    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))

            if 0 <= row < 10 and 0 <= 10 and (row, col) not in occupied:
                player_board[row][col] = "F"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct value.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))

            if 0 <= row < 10 and 0 <= 10 and (row, col) not in occupied:
                player_board[row][col] = "A"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct value.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))
            if 0 <= row < 10 and 0 <= 10 and (row, col) not in occupied:
                player_board[row][col] = "S"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct value.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

    return player_board, occupied


def comp_ship_coordinate(comp_board):
    """
    function for computer opponent
    """
    for ship in ship_initial:
        while True:
            row = randrange(0, 10)
            col = randrange(0, 10)
            if comp_board[row][col] == "_":
                comp_board[row][col] = ship
                break
        
    return comp_board