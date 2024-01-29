class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = collections.defaultdict(list)

        for word in strs:
            anagram_groups[''.join(sorted(word))].append(word)
        
        return list(anagram_groups.values())

