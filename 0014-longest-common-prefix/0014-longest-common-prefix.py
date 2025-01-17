class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_length = float("inf")
        for i in range(len(strs)):
            min_length = min(min_length, len(strs[i]))
        # for i in range(min_length):
        #     for j in range(len(strs)-1):
        #         if strs[j][i] == strs[j+1][i]:
        #             continue
        #         else:
        #             return prefix
        #     prefix += strs[0][i]
        # return prefix
        
        def rec(i, min_length, prefix):
            # check at each recursive call
            if (i > min_length-1):
                return prefix
            for j in range(len(strs)-1):
                if strs[j][i] == strs[j+1][i]:
                    continue
                else:
                    return prefix
            
            prefix += strs[0][i]
            return rec(i+1, min_length, prefix)
        
        return rec(0, min_length, "")
            