class Solution:
    def originalDigits(self, s: str) -> str:
        # s = "owoztneoer" -> "012"
        #0-9 zero, one, two, three, four, five, six, seven, eight, nine
        # z = zero, w = two, x = six, g = eight, u - four, v = five, seven, f = four, five, r = three
        # s' = "ozneoer"
        # s'' = "noe"
        # "fviefuro" -> ""
        # z, w, x, g, u / v, f, r
        # count(f) - count(u) = count(5)
        # count(v) - count(5) = count(7)
        # count(3) = count(r) - count(0) - count(4)
        # count(1) = count(o) - count(0) - count(2) - count(4)
        # count(9) = count(n) - count(7) - count(1) / 2
        res = ""
        counts = [0] * 26
        res1 = [0] * 10
        for c in s:
            idx = ord(c) - ord('a')
            counts[idx] += 1
        res1[0] = counts[25]
        res1[2] = counts[ord('w') - ord('a')]
        res1[6] = counts[ord('x') - ord('a')]
        res1[8] = counts[ord('g') - ord('a')]
        res1[4] = counts[ord('u') - ord('a')]
        res1[5] = counts[ord('f') - ord('a')] - res1[4]
        res1[7] = counts[ord('v') - ord('a')] - res1[5]
        res1[3] = counts[ord('r') - ord('a')] - res1[0] - res1[4]
        res1[1] = counts[ord('o') - ord('a')] - res1[0] - res1[2] - res1[4]
        res1[9] = (counts[ord('n') - ord('a')] - res1[1] - res1[7]) // 2
        output = ""
        for i in range(len(res1)):
            c = str(i)
            for j in range(res1[i]):
                output += c
        return output




        # for i in range(len(s)):
        #     if s[i] in dict1:
        #         stringToRemove = dict1[s[i]]



