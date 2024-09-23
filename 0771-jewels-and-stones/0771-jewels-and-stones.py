class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()
        count = 0
        for jewel in jewels:
            s.add(jewel)
        for stone in stones:
            if stone in s:
                count += 1
        return count