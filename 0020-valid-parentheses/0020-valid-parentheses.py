class Solution:
    def isValid(self, s: str) -> bool:
        #(){}[] valid
        #{{{}}}((())) valid
        #((()))) invalid
        #[)] invalid

        # Use stack to pop off valid pairs. Return true if stack is empty

        pairs = {"}": "{", ")":"(","]": "["}

        stack = []

        for c in s:
            # This can be an open or a close
            # if its a close
            if c in pairs:
                # if stack is not empty and top of stack is a pair
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                # either stack is empty or last element does not match
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        