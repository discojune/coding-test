class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            num2 = nums2[i]

            if set(nums1) == {0}:
                nums1[0] = num2
            else:   
                num1_pointer = m + i - 1
                while num1_pointer >= 0:

                    num1 = nums1[num1_pointer]

                    

                    if num2 >= num1:
                        nums1.insert(num1_pointer + 1, num2)
                        del nums1[-1]

                        break
                    
                    elif num1_pointer == 0 and num2 < num1:
                        nums1.insert(num1_pointer, num2)
                        del nums1[-1]

                        break

                    num1_pointer -= 1
                
            

