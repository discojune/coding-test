class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[idx] = v

                idx += 1
 
        return idx