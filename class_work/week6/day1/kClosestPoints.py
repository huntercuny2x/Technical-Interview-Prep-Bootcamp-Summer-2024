import heapq

def kClosest(points, k):
    pts_heap=[ [pt[0]**2+pt[1]**2,i] for i,pt in enumerate(points) ]
    heapq.heapify(pts_heap)
    return [ points[heapq.heappop(pts_heap)[1]] for i in range(k) ]