# Week 1 Prove Developer: Tic-Tac-Toe 
# Author: Osagie Ohenhen
# Instructor: Brad Lythgoe

def main():
    player = turn("")
    board = create_board()
    while not winnerOptions(board):
        show_table(board)
        player_move(player, board)
        player = turn(player)
    show_table(board)
    player= turn(player)
    print(f"Game Over : Player {player} won!\n")
    startAgainOption()


def create_board():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return numbers


def show_table(table_numbers):
    print(f"\n{table_numbers[0]}|{table_numbers[1]}|{table_numbers[2]}\n-----\n{table_numbers[3]}|{table_numbers[4]}|{table_numbers[5]}\n-----\n{table_numbers[6]}|{table_numbers[7]}|{table_numbers[8]}\n")


def winnerOptions(options):
    return (options[0] == options[1] == options[2] or options[3] == options[4] == options[5] or 
            options[6] == options[7] == options[8] or options[0] == options[3] == options[6] or
            options[1] == options[4] == options[7] or options[2] == options[5] == options[8] or
            options[0] == options[4] == options[8] or
            options[2] == options[4] == options[6])


def player_move(player, table_numbers):
    choice = int(input(f"PLAYER {player}: Choose a square (1-9): "))
    if choice <= 0 or choice >=10:
        print("\nSelect a correct Number")
        player_move(player,table_numbers)
    else: 
        table_numbers[choice - 1] = player


def turn(player):
    if player == "" or player == "O":
        return "X"
    elif player == "X":
        return "O"


def startAgainOption():
    startAgain = input("Do you want to start again?(Y/N): ")
    if startAgain.capitalize() == "Y":
        main()
    elif startAgain.capitalize() == "N":
        print("\nThanks for using TicTacToe by Osagie. Come back soon! :)\n")
    else:
        print("\nSelect a correct letter")
        startAgainOption()


if __name__ == "__main__":
    main()