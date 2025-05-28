class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "C":
                record.pop()
            elif op == "D":
                double = int(record[-1]) * 2
                record.append(double)
            elif op == "+":
                val = int(record[-1]) + int(record[-2])
                record.append(val)
            else:
                record.append(int(op))
        return sum(record)
