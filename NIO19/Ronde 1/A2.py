# (GESLOTEN, UITEINDES)
char_properties = {
    "A": (1, 2),
    "B": (2, 0),
    "C": (0, 2),
    "D": (1, 0),
    "E": (0, 3),
    "F": (0, 3),
    "G": (0, 2),
    "H": (0, 4),
    "I": (0, 2),
    "J": (0, 2),
    "K": (0, 4),
    "L": (0, 2),
    "M": (0, 2),
    "N": (0, 2),
    "O": (1, 0),
    "P": (1, 1),
    "Q": (1, 2),
    "R": (1, 2),
    "S": (0, 2),
    "T": (0, 3),
    "U": (0, 2),
    "V": (0, 2),
    "W": (0, 2),
    "X": (0, 4),
    "Y": (0, 3),
    "Z": (0, 2),
}


word = input()
res = [0, 0]
for char in word:
    char_property = char_properties[char]
    res[0] += char_property[0]
    res[1] += char_property[1]

print(res[0])
print(res[1])
