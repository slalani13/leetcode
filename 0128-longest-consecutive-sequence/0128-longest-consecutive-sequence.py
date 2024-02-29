class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        streak = 0

        for n in nums:
            if n-1 not in s:
                curr_streak = 1
                current_num = n
                while current_num+1 in s:
                    curr_streak +=1
                    current_num +=1
                streak = max(streak,curr_streak)
        
        return streak