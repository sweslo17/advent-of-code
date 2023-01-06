cur = 0
top_three_heap = [0, 0, 0]


def insert_to_heap(heap, current):
    for i in range(3):
        if current > heap[i]:
            if i - 1 >= 0:
                heap[i - 1] = heap[i]
            heap[i] = current
    return heap


with open("../day2/input.txt", "r") as f:
    for line in f.readlines():
        if len(line.strip()) == 0:
            top_three_heap = insert_to_heap(top_three_heap, cur)
            cur = 0
            continue
        cur += int(line.strip())
    top_three_heap = insert_to_heap(top_three_heap, cur)
print(sum(top_three_heap))
