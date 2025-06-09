class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums = [1, 3, 4, 2, 2]
        #         0  1. 2. 3. 4
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow] # nums[2] = 4
            fast = nums[nums[fast]] # nums[nums[4] = 2] = 4
            if slow == fast:
                break
        slow2 = 0

        while slow2 != slow:
            slow2 = nums[slow2] # nums[2] = 4
            slow = nums[slow] # nums[2] = 4
        return slow
        
