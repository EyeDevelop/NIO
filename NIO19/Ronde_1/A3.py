import re


word = input()
numbers = ["TWEE", "DRIE", "VIER", "VIJF", "ZES", "ZEVEN", "ACHT", "NEGEN"]
patterns = dict(zip(numbers, [".*".join(list(x)) for x in numbers]))

match_found = False
for num in numbers:
    match = re.search(patterns[num], word)
    if match:
        match_found = True
        print(num)
        break

if not match_found:
    print("geen")
