diskNumber = int(input())


def moveDisk(diskNumber, moves, sourceStack, destinationStack, auxiliaryStack):
    if diskNumber == 1:
        moves.append([sourceStack, destinationStack])
        return

    moveDisk(diskNumber - 1, moves, sourceStack, auxiliaryStack, destinationStack)

    moves.append([sourceStack, destinationStack])

    moveDisk(diskNumber - 1, moves, auxiliaryStack, destinationStack, sourceStack)


def towerOfHanoi(numberOfDisks):
    moves = []
    sourceStack, destinationStack, auxiliaryStack = 1, 3, 2
    moveDisk(numberOfDisks, moves, sourceStack, destinationStack, auxiliaryStack)

    print(len(moves))

    for move in moves:
        print(move[0], move[1])


if __name__ == "__main__":
    numberOfDisks = diskNumber
    towerOfHanoi(numberOfDisks)
