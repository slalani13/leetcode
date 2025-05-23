class Solution:
    def validPalindrome(self, s: str) -> bool:
        # palindrome can be found with 2 pointers or by reversing the array
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l, r-1) or isPalindrome(l+1, r)
            l+=1
            r-=1
        return True