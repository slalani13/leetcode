class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, sign, res = 0, 1, "", 1

        while r < len(arr):
            if arr[r-1] < arr[r] and sign != "<":
                res = max(res, r-l+1) # valid window, update res
                r += 1
                sign = "<"
            elif arr[r-1] > arr[r] and sign != ">":
                res = max(res, r-l+1)
                r += 1
                sign = ">"
            else: # case with = or starting case
                if arr[r-1] == arr[r]:
                    l = r
                    r += 1
                else:
                    l = r-1
                sign = ""
        return res