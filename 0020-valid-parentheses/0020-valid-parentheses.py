class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        hashmap = {")": "(", "]":"[", "}":"{"}
        stack = []
        for i in range(len(s)):
            if not stack and s[i] in hashmap:
                return False
            elif stack and s[i] in hashmap:
                if stack[-1] != hashmap[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False
                
