class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0 for _ in range(len(pref))]
        # arr = [pref[0]]

        def recursive(arr, i):
            bit_op_result = 0
            for j in range(i-1, -1, -1):
                bit_op_result ^= arr[j]

            return bit_op_result
        
        arr[0] = pref[0]
        for i in range(1, len(pref)):
            # print(pref[i], arr[i-1])
            # # arr[i] = pref[i] ^ pref[i-1]
            if i == 1:
                arr[i] = pref[1] ^ arr[0]
            else:
                arr[i] = pref[i] ^ pref[i-1]
            #     arr[i] = pref[i] ^ recursive(arr, i)

            # print(arr)
        return arr


        # # arr = [0 for _ in range(len(pref))]
        # arr = [pref[0]]

        # def recursive(arr, i):
        #     bit_op_result = 0
        #     for j in range(i-1, -1, -1):
        #         bit_op_result ^= arr[j]

        #     return bit_op_result
        
        # for i in range(1, len(pref)):
        #     if i == 1:
        #         # arr[i] = pref[1] ^ arr[0]
        #         arr.append(pref[1] ^ arr[0])
        #     else:
        #         # arr[i] = pref[i] ^ recursive(arr, i)
        #         arr.append(pref[i] ^ recursive(arr, i))

        # return arr


         
