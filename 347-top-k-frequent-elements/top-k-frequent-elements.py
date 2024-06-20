class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        nums_count = Counter(nums)

        nums_sorted = sorted(nums_count.items(), key=lambda x : x[1], reverse=True)

        topk_nums = [n for n, _ in nums_sorted[:k]]

        return topk_nums