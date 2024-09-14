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