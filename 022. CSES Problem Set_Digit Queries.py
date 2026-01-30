q = int(input())
for _ in range(q):
    k = int(input())

    length = 1
    start = 1
    count = 9

    while k > length * count:
        k -= length * count
        length += 1
        start *= 10
        count *= 10

    num = start + (k - 1) // length

    num_str = ""
    temp = num
    while temp > 0:
        num_str = chr(ord("0") + temp % 10) + num_str
        temp //= 10

    digit_index = (k - 1) % length
    print(num_str[digit_index])
