class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for n in arr:
            if n % 2 != 0:
                print("Here")
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        # print(count)
        return False