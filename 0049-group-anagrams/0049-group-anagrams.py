class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            key = sorted(word)
            key = tuple(key)
            hashmap[key].append(word)
        
        res = []
        for val in hashmap.values():
            res.append(val)

        return res