#heap push
'''import heapq
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heapify(heap)
print(heap)
print(heapq.heapreplace(heap, 8))
print(heapq.heappop(heap))
print(heapq.heappushpop(heap, 7))
print(heap)'''

#insert operation in heap
'''import heapq
heap = []
n = int(input("Enter number of nodes in the tree: "))
for i in range(n):
    val = int(input("Enter the val: "))
    heapq.heappush(heap, val)
heapq.heapify(heap)
print("Heap after insertion: ", heap)'''

#max element in a heap using insert iperation in heap
'''import heapq
heap = []
n = int(input("Enter number of nodes in the tree: "))
for i in range(n):
    val = int(input("Enter the value: "))
    heapq.heappush(heap, -val)
heapq.heapify(heap)
print("Max Heap internal value: ", heap)
print("Max element removed: ", -heapq.heappop(heap))
print("Heap after deletion: ", [-x for x in heap])'''

#sort the elements in a heap using insert operation in heap
'''import heapq
heap = []
n = int(input("Enter number of nodes in the tree: "))
for i in range(n):
    val = int(input("Enter the value: "))
    heapq.heappush(heap, val)
heapq.heapify(heap)
sorted_list = []
while heap:
    sorted_list.append(heapq.heappop(heap))
print("Sorted elements in the tree: ", sorted_list)'''

# max heap
'''def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left<n and arr[left] > arr[largest]:
        largest = left
    if right<n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)
for i in range(n/2 - 1, -1, -1):
    heapify(arr, n, i)
print(arr)'''

# min heap
'''def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left<n and arr[left] < arr[smallest]:
        smallest = left
    if right<n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)
for i in range(n/2 - 1, -1, -1):
    heapify(arr, n, i)
print(arr)'''