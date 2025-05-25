class Solution:
    def validPalindrome(self, s: str) -> bool:
        # palindrome can be found with 2 pointers or by reversing the array
        listS = list(s)
        l, r = 0, len(listS)-1
        while l < r: # l = 1, r = 2
            if listS[l] != listS[r]:
                includeLeft = listS[l:r]
                includeRight = listS[l+1:r+1]
                return includeLeft == includeLeft[::-1] or includeRight == includeRight[::-1]
            l += 1
            r -= 1
        return True
        

