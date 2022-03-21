from grid import Grid


def get_player_name(player_number):
    if player_number == 0:
        return "Red"
    return "Yellow"


def get_player_colour(player_number):
    if player_number == 0:
        return "R"
    return "Y"


def main():
    grid = Grid(7, 5)
    player = 0
    while True:
        print(grid.get_display())
        column = int(input(f"Player {get_player_name(player)}, Enter column number to drop token: "))
        grid.drop_token(column - 1, get_player_colour(player))
        player = 1 - player


if __name__ == "__main__":
    main()
