class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ')':
                stack.append(c) # 
            else:
                reversed_word = ""
                while stack[-1] != '(':
                    reversed_word += stack[-1]
                    stack.pop()
                stack.pop()
                for w in reversed_word:
                    stack.append(w)
        return "".join(stack)
