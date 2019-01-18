to_enc = input()
n = int(input())
res = ""

for i in to_enc:
    c_code = ord(i)

    if c_code + n > ord('Z'):
        c_code = ord('A') + (c_code + n - ord('Z') - 1)
    else:
        c_code = c_code + n

    res += chr(c_code)

print(res)
