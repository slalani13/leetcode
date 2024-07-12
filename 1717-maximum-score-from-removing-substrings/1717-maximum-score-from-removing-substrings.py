class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s) < 2:
            return 0
        if x >= y:
            high, low = ["ab", x], ["ba", y]
        else:
            high, low = ["ba", y], ["ab", x]
        
        stack = []
        score = 0
        for i in range(len(s)):
            if s[i] == high[0][-1] and len(stack) >= 1:
                if stack[-1] == high[0][0]:
                    stack.pop()
                    score += high[1]
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        s = "".join(stack)
        stack = []
        for i in range(len(s)):
            if s[i] == low[0][-1] and len(stack) >= 1:
                if stack[-1] == low[0][0]:
                    stack.pop()
                    score += low[1]
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return score
