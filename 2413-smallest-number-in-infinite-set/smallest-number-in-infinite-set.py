import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.infinite_set = []
        heapq.heapify(self.infinite_set)
        self._set = set()
        self.curr = 1

    def popSmallest(self) -> int:
        if self.infinite_set:
            value = heapq.heappop(self.infinite_set)
            self._set.remove(value)
            
            return value
        
        self.curr += 1
        return self.curr - 1

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self._set:
            heapq.heappush(self.infinite_set, num)
            self._set.add(num)
    

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)