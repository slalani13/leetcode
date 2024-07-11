class Solution:
    def reverseParentheses(self, s: str) -> str:
        # create empty stack
        # if closing bracket:
        # pop from stack until opening bracket
        # readd reversed string
        stack = []
        for c in s:
            if c != ')': # [(ulove
                stack.append(c) # 
            else:
                reversed_word = "" #
                while stack[-1] != '(':
                    reversed_word += stack[-1] #evol
                    stack.pop()
                stack.pop()
                for w in reversed_word:
                    stack.append(w)
        return "".join(stack)
