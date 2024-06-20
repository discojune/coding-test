class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        # Step 1: Count the frequencies
        count = Counter(nums)
        
        # Step 2: Use a heap to find the top k frequent elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract the results
        result = [num for freq, num in heap]
        return result