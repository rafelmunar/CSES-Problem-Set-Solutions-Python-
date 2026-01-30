n = int(input())
events = []

for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, 1))
    events.append((b, -1))

events.sort(key=lambda x: (x[0], x[1]))

max_customers = 0
current_customers = 0

for time, change in events:
    current_customers += change
    max_customers = max(max_customers, current_customers)

print(max_customers)
