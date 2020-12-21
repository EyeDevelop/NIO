vowels = ['e', 'a', 'i', 'o', 'u']
s = input()

r = ""
for x in s:
    if x.lower() not in vowels:
        r += x
print(r)
