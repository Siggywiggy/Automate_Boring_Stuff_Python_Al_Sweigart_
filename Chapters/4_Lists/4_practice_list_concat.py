spam = ["apples", "bananas", "tofu", "cats"]
empty_list = []


def concat_list(list):
    if len(list) == 0:
        return "You entered an empty list!"

    else:
        new_list = []

        for word in list:
            new_list.append(word)
            new_list.append(", ")

        del new_list[-1]
        new_list[-2] = " and "
        new_string = ""
        for word in new_list:
            new_string += word
        return new_string


print(concat_list(spam))

print(concat_list(empty_list))
