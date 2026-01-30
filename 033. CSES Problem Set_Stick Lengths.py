n = int(input())
sticks = list(map(int, input().split()))

sticks.sort()

median = sticks[n // 2]

total_cost = 0
for length in sticks:
    total_cost += abs(length - median)

print(total_cost)
