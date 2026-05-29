# Priority queue deletion
'''import heapq
Q = []
heapq.heappush(Q, 11)
heapq.heappush(Q, 33)
heapq.heappush(Q, 22)
heapq.heappush(Q, 1)
print("Priority Queue: ", Q)
print("Removed: ", heapq.heappop(Q))
print("after removal Queue: ", Q)'''

'''import heapq
Q = []
heapq.heappush(Q, (1, "Emergency"))
heapq.heappush(Q, (3, "Follow-Up"))
heapq.heappush(Q, (2, "Consultation"))
print(Q)
while Q:
    print(heapq.heappop(Q))'''

# kth largest element using priority Q
import heapq
arr = list(map(int, input("Enter values: ").split()))
k = int(input("Enter number: "))
heap = []
for num in arr:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
print(f"{k}th largest element is: ", heap[0])