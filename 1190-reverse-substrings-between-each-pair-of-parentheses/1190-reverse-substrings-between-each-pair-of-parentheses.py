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
                # print(stack)
            else:
                reversed_word = "" #
                #print(stack[-1]) #e, v, o, l, i
                while stack[-1] != '(':
                    reversed_word += stack[-1] #evol
                    # print("r", reversed_word)
                    stack.pop()
                    print("v", stack[-1])
                # print("reversedWord: ", reversed_word) 
                stack.pop()
                # print("current stack", stack)
                for w in reversed_word:
                    stack.append(w)
                # print("new_stack", stack)
        return "".join(stack)
