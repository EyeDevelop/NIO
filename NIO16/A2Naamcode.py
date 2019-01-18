__author__ = 'eyedevelop'

naam = input()
naam_a = naam.split()
namen = []

for i in range(len(naam_a)):
    if naam_a[i][0:1].isupper():
        namen.append(naam_a[i])

voornaam = namen[0]
achternaam = namen[len(namen) - 1]
afkorting = achternaam[0:1].upper() + achternaam[len(achternaam) - 1].upper() + voornaam[0:1].upper()

print(afkorting)