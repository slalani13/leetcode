class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       # initial solution : sort the values and then find a count > n/2; O(nlogn + n)
       # use hashmap to count each number, if count > n//2 return number O(n) time and space
       # iterate through the array and choose candidate, when count hits 0, change candidate
       # O(n) time and O(1) space
        # [3, 2, 3] candidate = 2, count = 1
        candidate = nums[0]
        count = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1
        return candidate
            
    
