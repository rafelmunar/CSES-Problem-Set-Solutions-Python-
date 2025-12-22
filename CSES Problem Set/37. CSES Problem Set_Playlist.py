n = int(input())
songs = list(map(int, input().split()))

count = {}
max_len = 0
left = 0

for right in range(n):
    current_song = songs[right]
    count[current_song] = count.get(current_song, 0) + 1

    while count[current_song] > 1:
        left_song = songs[left]
        count[left_song] -= 1
        if count[left_song] == 0:
            del count[left_song]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)
