from itertools import permutations

word = input()


def solve(S):
    S_sorted = sorted(S)

    unique_strings = set()

    for perm in permutations(S_sorted):
        unique_strings.add("".join(perm))

    return unique_strings


def main():
    S = word

    unique_strings = solve(S)

    print(len(unique_strings))

    for string in unique_strings:
        print(string)


if __name__ == "__main__":
    main()
