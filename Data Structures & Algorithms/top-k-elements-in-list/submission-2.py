class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(Counter(nums).items())
        heap = [(-k[1], k[0]) for k in count]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res