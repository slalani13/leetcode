class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        fancy = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            if count == 3:
                count -= 1
                continue
            else:
                fancy += s[i]
        return fancy