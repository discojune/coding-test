class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        num1_p = m - 1
        num2_p = n - 1

        num1_idx = m + n - 1

        while num2_p >= 0:
            if num1_p >= 0 and nums1[num1_p] >= nums2[num2_p]:
                nums1[num1_idx] = nums1[num1_p]

                num1_idx -= 1
                num1_p -= 1

            else:
                nums1[num1_idx] = nums2[num2_p]

                num1_idx -= 1
                num2_p -= 1
                
            

