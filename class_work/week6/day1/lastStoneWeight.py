import heapq

def lastStoneWeight(stones):
    stones_max_heap = [-stone for stone in stones]
    heapq.heapify(stones_max_heap)

    while len(stones_max_heap)>1:
        y=heapq.heappop(stones_max_heap)
        x=heapq.heappop(stones_max_heap)

        if y!=x:
            heapq.heappush(stones_max_heap, y-x)

    return -1*heapq.heappop(stones_max_heap) if stones_max_heap else 0 

