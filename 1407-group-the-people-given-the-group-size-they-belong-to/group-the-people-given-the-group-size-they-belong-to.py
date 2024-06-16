class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import deque

        index_group = [i for i in range(0, len(groupSizes))]
        index_group = [(j, i) for j, i in sorted(zip(groupSizes, index_group))]
        
        queue = deque(index_group)
        print(queue)
        result = []
        temp = []
        while queue:
            group, person = queue.popleft()
            
            temp.append(person)

            if len(temp) >= group:
                result.append(temp)
                temp = []

        return result