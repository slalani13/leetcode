class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(strs) <= 1:
        #     return [strs]
        hashMap = {}
        res = []
        print(hashMap)
        for word in strs:
            wordCount = [0]*26
            for c in word:
                index = ord(c) - ord('a')
                wordCount[index] += 1
            key = tuple(wordCount)
            if key in hashMap:
                hashMap[key].append(word)
            else:
                hashMap[key] = [word]
        for val in hashMap.values():
            res.append(val)
        return res