class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return true if after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, reads the same forwards and backwards
        # create a new list with lowercase alnum characters - O(n) time and space, then check
        # use 2 pointers to check palindrome or check reverse
        # conditions: character is uppercase letter, alnum, or not alnum
        # if not alnum skip, else check lower
        l, r = 0, len(s)-1 # l = 2, r = 1
        while l < r:
            while l < r and  not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            
