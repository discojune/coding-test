class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0 for _ in range(len(pref))]

        arr[0] = pref[0]
        for i in range(1, len(pref)):
            if i == 1:
                arr[i] = pref[1] ^ arr[0]
            else:
                arr[i] = pref[i] ^ pref[i-1]

        return arr
