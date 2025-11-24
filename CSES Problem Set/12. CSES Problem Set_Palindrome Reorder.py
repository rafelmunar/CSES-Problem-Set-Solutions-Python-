s = input()

pairs = []
single = []

for char in s:
    if char in single:
        single.remove(char)
        pairs.append(char)
    else:
        single.append(char)

res = "".join(pairs) + "".join(single) + "".join(pairs)[::-1]

if res == res[::-1]:
    print(res)
else:
    print("NO SOLUTION")
