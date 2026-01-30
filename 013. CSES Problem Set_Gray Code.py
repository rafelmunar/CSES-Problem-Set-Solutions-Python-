starting_number = int(input())


def graycode(n):

    if n == 1:
        return ["0", "1"]

    prevGrayCode = graycode(n - 1)
    reversedPrevGrayCode = prevGrayCode[::-1]

    prevSize = len(prevGrayCode)
    index = 0

    zeros_part = []
    ones_part = []

    while index < prevSize:

        appended_zero = "0" + prevGrayCode[index]
        zeros_part.append(appended_zero)

        appended_one = "1" + reversedPrevGrayCode[index]
        ones_part.append(appended_one)

        index += 1

    return zeros_part + ones_part


if __name__ == "__main__":
    n = starting_number
    res = graycode(n)
    for code in res:
        print(code)
