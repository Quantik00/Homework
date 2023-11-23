def heapify(heap, k):
	l = 2 * k + 1
	r = 2 * k + 2
	if l < len(heap) and heap[l] > heap[k]:
		largest = l
	else:
		largest = k
	if r < len(heap) and heap[r] > heap[largest]:
		largest = r
	if largest != k:
		heap[k], heap[largest] = heap[largest], heap[k]
		heapify(heap, largest)


def build_max_heap(heap):
	n = int((len(heap) // 2) - 1)
	for k in range(n, -1, -1):
		heapify(heap, k)


heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(heap)
build_max_heap(heap)
print(heap)
heap = heap[1:]
build_max_heap(heap)
print(heap)