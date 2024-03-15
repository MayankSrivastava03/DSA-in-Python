from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        mp = Counter(nums)
        # Step 2: Define a min heap
        pq = []
        # Step 3: Push elements into the min heap, maintaining size k
        for key, value in mp.items():
            heapq.heappush(pq, (value, key))
            if len(pq) > k:
                heapq.heappop(pq)
        
        # Step 4: Get the result
        result = [item[1] for item in pq]
        return result
