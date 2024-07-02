import heapq

def findKthLargest(nums, k):
    heapq.heapify(nums)
    for i in range(len(nums)-k):
        heapq.heappop(nums)
    return heapq.heappop(nums)