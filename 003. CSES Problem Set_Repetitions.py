n = input()

cur = ""
cnt = 0
max_cnt = 0

for i in n:
    if i == cur:
        cnt += 1
    if i != cur:
        max_cnt = max(cnt, max_cnt)
        cnt = 1
        cur = i

max_cnt = max(cnt, max_cnt)

print(max_cnt)
