class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for op in operations:
            if op == "C":
                stk.pop()
            elif op == "D":
                stk.append(2*stk[-1])
            elif op == "+":
                stk.append(stk[-1] + stk[-2])
            else:
                stk.append(int(op))
        return sum(stk)