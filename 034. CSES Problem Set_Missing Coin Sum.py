n = int(input())
coins = list(map(int, input().split()))

coins.sort()

current_sum = 0
for coin in coins:
    if coin > current_sum + 1:
        break
    current_sum += coin

print(current_sum + 1)
