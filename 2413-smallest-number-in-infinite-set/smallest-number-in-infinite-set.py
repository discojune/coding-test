import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.infinite_set = list(range(1, 10000))
        self.infinite_dict = {v : 1 for v in self.infinite_set}

        heapq.heapify(self.infinite_set)

    def popSmallest(self) -> int:
        value = heapq.heappop(self.infinite_set)
        del self.infinite_dict[value]

        return value

    def addBack(self, num: int) -> None:
        if num in self.infinite_dict:
            pass
        else:
            heapq.heappush(self.infinite_set, num)
            self.infinite_dict.update({num : 1})
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)