class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = [0] * 26
        for c in text:
            index = ord(c) - ord('a')
            letters[index] += 1
        
        balloon = "balloon"

        count = 0
        while True:
            for l in balloon:
                idx = ord(l) - ord('a')
                letters[idx] -= 1
                if letters[idx] < 0:
                    return count
            count += 1
