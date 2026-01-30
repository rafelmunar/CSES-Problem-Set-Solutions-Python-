class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][0] < self.heap[parent][0]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest != idx:
                self.heap[idx], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[idx],
                )
                idx = smallest
            else:
                break

    def __len__(self):
        return len(self.heap)


def main():
    n = int(input())
    customers = []

    for i in range(n):
        a, b = map(int, input().split())
        customers.append((a, b, i))

    customers.sort(key=lambda x: x[0])

    heap = MinHeap()
    room_assignments = [0] * n
    next_room = 1

    for a, b, idx in customers:
        if len(heap) > 0 and heap.peek()[0] < a:
            _, room = heap.pop()
            room_assignments[idx] = room
            heap.push((b, room))
        else:
            room_assignments[idx] = next_room
            heap.push((b, next_room))
            next_room += 1

    k = next_room - 1
    print(k)
    print(" ".join(map(str, room_assignments)))


if __name__ == "__main__":
    main()
