import pprint


def board_builder_function():
    board_dict = {}
    alphabetical = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for x in range(1, 9):
        for y in alphabetical:
            board_dict[str(x) + str(y)] = 0

    return board_dict


clean_board_dict = board_builder_function()
piece_names_list = ["pawn", "knight", "bishop", "rook", "queen", "king", ""]

# pprint.pprint(clean_board_dict)


def chessboard_validator(input_board):
    white_pieces = 0
    black_pieces = 0
    white_player_pieces = {}
    black_player_pieces = {}

    for key, value in input_board.items():
        print(str(key), str(value))
        # check if a piece is a valid piece on a valid space
        if key not in clean_board_dict:
            print(f"not a valid space - {key}")
            return False

        # check if piece starts with 'w' or 'b'
        if value != "":
            if value[0] == "b" or value[0] == "w":
                print(f"Valid color - {value[0]}")
            else:
                print(value[0])
                print(f"not a valid color - {value[0]}")
                return False

        # check if piece is a valid piece
        if value[1:] not in piece_names_list:
            print(f"not a valid piece - {value[1:]}")
            return False

        # count black and white pieces
        if value != "":
            if value[0] == "w":
                white_pieces += 1
            if value[0] == "b":
                black_pieces += 1

        # creating dicts for players with count of pieces
        if value[0] == "w":
            white_player_pieces.setdefault(value, 0)
            white_player_pieces[value] = white_player_pieces[value] + 1
        if value[0] == "b":
            black_player_pieces.setdefault(value, 0)
            black_player_pieces[value] = black_player_pieces[value] + 1

    print(f"white pieces total = {white_pieces}")
    print(f"black pieces total = {black_pieces}")

    # at most total 16 pieces per player

    # if white_pieces > 16 or black_pieces > 16:
    # print("too many pieces per player!")
    # return False


board = {
    "1a": "bking",
    "2a": "bqueen",
    "3a": "brook",
    "4a": "brook",
    "5a": "bknight",
    "6a": "bknight",
    "7a": "bbishop",
    "8a": "bbishop",
    "1b": "bpawn",
    "2b": "bpawn",
    "3b": "bpawn",
    "4b": "bpawn",
    "5b": "bpawn",
    "6b": "bpawn",
    "7b": "bpawn",
    "8b": "bpawn",
    "1c": "wking",
    "2c": "wqueen",
    "3c": "wrook",
    "4c": "wrook",
    "5c": "wbishop",
    "6c": "wbishop",
    "7c": "wknight",
    "8c": "wknight",
    "1e": "wpawn",
    "2e": "wpawn",
    "3e": "wpawn",
    "4e": "wpawn",
    "5e": "wpawn",
    "6e": "wpawn",
    "7e": "wpawn",
    "8e": "wpawn",
    "1f": "",
    "2f": "",
    "3f": "",
    "4f": "",
    "5f": "",
    "6f": "",
    "7f": "",
    "8f": "",
    "1g": "",
    "2g": "",
    "3g": "",
    "4g": "",
    "5g": "",
    "6g": "",
    "7g": "",
    "8g": "",
    "1h": "",
    "2h": "",
    "3h": "",
    "4h": "",
    "5h": "",
    "6h": "",
    "7h": "",
    "8h": "",
}

print(chessboard_validator(board))
