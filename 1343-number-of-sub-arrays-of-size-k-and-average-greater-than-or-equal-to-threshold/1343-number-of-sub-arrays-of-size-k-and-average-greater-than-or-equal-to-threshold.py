class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # create a window of size k, check the average and update the res
        numSubarray = 0
        l = 0
        curSum = 0
        for i in range(k):
            curSum += arr[i]
        if threshold == 0 or curSum / k >= threshold :
            numSubarray += 1
        for r in range(k, len(arr)):
            curSum += arr[r]
            curSum -= arr[l]
            l += 1
            if r-l+1 == k:
                if threshold == 0 or curSum / k >= threshold:
                    numSubarray += 1
        return numSubarray
        #[2, 2, 2, 2, 5, 5, 5, 8] l=0, r=2, curSum=18, res=0, k -3
                        #  L
                        #        R