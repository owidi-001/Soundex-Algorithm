# DUMMY_NAMES = ["Liang",
#                "Smythe",
#                "Smith",
#                "Davies",
#                "Davis",
#                "Johnson",
#                "Xiang",
#                "Domaratzki",
#                "Johanssen",
#                "Leung",
#                ]

"""
Reads user inputs and returns a list of names
"""


def read_input() -> list:
    print("Enter names, one on each line. Type DONE to quit entering names.")
    names = []
    name = input()
    while name.upper() != "DONE":
        names.append(name)
        name = input()

    return names


"""
STEP 3
Replaces letters with digits
"""


def letters_digits(name) -> str:
    letters = (
        ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w'],
        ['b', 'f', 'p', 'v'],
        ['c', 'g', 'j', 'k', 'q', 's', 'x', 'x'],
        ['d', 't'],
        ['l'],
        ['m', 'n'],
        ['r']
    )

    name_to_digits = ""
    for letter in name:
        for index in range(len(letters)):
            if letter in letters[index]:
                name_to_digits += str(index)

    return name_to_digits


"""
STEP 4
Replaces multiple digits with single digit
"""


def multi_single(name) -> str:
    new_name = ""

    for digit in name:
        if digit not in new_name:
            new_name += digit

    return new_name


"""
Remove all occurrences of 0 in D
"""


def remove_0(encoding) -> str:
    new_encoding = ''
    for letter in encoding:
        if letter != '0':
            new_encoding += letter

    return new_encoding


"""
STEP 7
Ensures the length of the encoding is 4
"""


def len_encoding(name_encod) -> str:
    if len(name_encod) == 4:
        pass
    elif len(name_encod) < 4:
        while len(name_encod) < 4:
            name_encod += "0"
    else:
        name_encod = name_encod[0:4]

    return name_encod


"""
Completes the overall soundex algorithm
"""


def soundex(name) -> str:
    name = name.lower()
    F = name[0]

    D = letters_digits(name[1:])

    D = multi_single(D)
    D = remove_0(D)

    if letters_digits(F) == D[0]:
        D = F + D[1:]
    else:
        D = F + D[0:]
    if len(D) == 0:
        D = letters_digits(F)

    D = len_encoding(D)

    return D


def main():
    """
    Uncommet this to test the functions
    :return:
    """
    # print(read_input())
    # print(letters_digits("Domaratzki"))
    # print(multi_single("2205033"))
    # print(remove_0("2205033"))
    # print(len_encoding("2003"))
    # print(len_encoding("22"))
    # print(len_encoding("2205033"))
    name1_name2_construct = []
    soundex_name_list = []

    names = read_input()
    # names = DUMMY_NAMES
    # names = [name.lower() for name in names] # Converts the names to begin with lowercase

    for name in names:
        soundex_name_list.append((soundex(name.lower()), name))
        # print(soundex(name), name)

    # for x in soundex_name_list:
    #     print(x)

    for i in range(len(soundex_name_list)):
        for j in range(len(soundex_name_list)):
            if i == j:
                # print(i, j, " equal")
                pass
            else:
                # print(i, j, " Not equal")
                if soundex_name_list[i][0] == soundex_name_list[j][0]:
                    name1 = min(soundex_name_list[i][1], soundex_name_list[j][1])
                    name2 = max(soundex_name_list[i][1], soundex_name_list[j][1])
                    construct = f"{name1} and {name2} have the same Soundex encoding."
                    if construct not in name1_name2_construct:
                        name1_name2_construct.append(construct)

    name1_name2_construct.sort()

    for construct in name1_name2_construct:
        print(construct)


if __name__ == '__main__':
    main()
