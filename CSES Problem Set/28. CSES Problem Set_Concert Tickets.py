n, m = map(int, input().split())
tickets = list(map(int, input().split()))
customers = list(map(int, input().split()))

tickets.sort()

result = []
for budget in customers:
    idx = -1
    for i in range(len(tickets)):
        if tickets[i] <= budget:
            idx = i
        else:
            break

    if idx != -1:
        result.append(tickets[idx])
        tickets.pop(idx)
    else:
        result.append(-1)

for res in result:
    print(res)
