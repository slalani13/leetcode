class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for word in strs:
            # each letter will be an index
            wordList = [0]*26
            for l in word:
                index=ord(l) - ord('a')
                wordList[index] +=1
            # wordTuple = tuple(wordList)
            maps[tuple(wordList)].append(word)
            # if wordTuple in maps:
            #     maps[wordTuple].append(word)
            # else:
            #     maps[wordTuple] = [word]
        
        return maps.values()
        