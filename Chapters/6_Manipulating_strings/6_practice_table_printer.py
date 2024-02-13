table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

# find longest string in each of the inner lists


def print_table(table_data):
    column_widths = [0] * len(table_data)

    # counting maximum lenght of string in a substring
    for i in range(len(table_data)):
        current_max = 0
        for item in table_data[i]:
            if len(item) > current_max:
                current_max = len(item)
        column_widths[i] = current_max
    print(f"Column widths are {column_widths}")

    for y in range(len(table_data[0])):  # y = 0, 1, 3, 4
        # print(y)
        concat_string = ""
        for i in range(len(table_data)):  # i = 0, 1, 2
            concat_string += table_data[i][y].rjust(column_widths[i], " ")
            concat_string += " "

        print(concat_string)
        # concat_string = table_data[0][0] + table_data[1][0] + table_data[2][0]
        # concat_string = apples + Alice + dogs
        # concat_string = table_data[0][1] + table_data[1][1] + table_data[2][1]
        # concat_string = oranges + Bob + cats
        # concat_string = table_data[0][2] + table_data[1][2] + table_data[2][2]
        # concat_string = cherries + Carol + moose
        # concat_string = table_data[0][3] + table_data[1][3] + table_data[2][3]
        # concat_string = banana + David + goose
    return


print_table(table_data)
