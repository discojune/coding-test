class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        p = 1

        # 왼쪽 곱셉
        for i in range(len(nums)):
            result.append(p)

            p = p * nums[i]

        p = 1

        # 왼쪽 곱셉 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            result[i] = result[i] * p

            p = p * nums[i]

        return result