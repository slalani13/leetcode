class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # utilize 2 pointers
        # 2 pointers at both ends and swap
        # use recursion
        def reverse(l, r, s):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            reverse(l+1, r-1, s)
            return
        reverse(0, len(s)-1, s)
        # reverse(0, 5, hello)
        # reverse(1, 4, oellh)
        # reverse(2, 3, olleh)
        # reverse(3, 2, olleh)

        
        