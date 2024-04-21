class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"}":"{","]":"[",")":"("}
        stack = []
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        
        for c in s:
            # opening bracket
            if c not in mp:
                stack.append(c)
                continue
            # closing bracket at beginning
            elif not stack and c in mp:
                return False
            # closing bracket == opening bracket
            elif c in mp and stack[-1] == mp[c]:
                stack.pop(-1)
                continue
            # none of the above
            else:
                return False
        
        if not stack:
            return True
        else:
            return False