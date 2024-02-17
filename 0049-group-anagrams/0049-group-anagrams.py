
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # treat anagram as a list of letters with a count
        

        result = defaultdict(list)

        for word in strs:
            count = [0] * 26 # for letters of the alphabet, this is the key
            # at the end of loop, count is updated for the word
            for l in word:
                # gets ascii value to find index of letter
                count[ord(l) - ord('a')] += 1 
            key = tuple(count)
            # appending value with same key, or adding new key
            result[key].append(word)
            # print(result)
        
        return result.values()

        