class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of size s1
        # iterate through and update a counts array and check if it matches with the s1Counts
        # continue until len(s2), return false
        # base checks
        if len(s1) > len(s2):
            return False
        
        s1Counts, counts = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Counts[ord(s1[i])-ord('a')] += 1
            counts[ord(s2[i])-ord('a')] += 1
        
        if s1Counts == counts:
            return True
        
        l=0
        for i in range(len(s1), len(s2)):
            counts[ord(s2[i])-ord('a')] += 1
            counts[ord(s2[l])-ord('a')] -= 1
            if s1Counts == counts:
                return True
            l += 1
        return False

