def main():
    n = int(input())
    cubes = list(map(int, input().split()))

    tops = []

    for cube in cubes:
        low, high = 0, len(tops)
        while low < high:
            mid = (low + high) // 2
            if tops[mid] > cube:
                high = mid
            else:
                low = mid + 1

        if low == len(tops):
            tops.append(cube)
        else:
            tops[low] = cube

    print(len(tops))


if __name__ == "__main__":
    main()
