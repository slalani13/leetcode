class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # return an int which is the total number of good pairs
        set1 = set()
        count = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count +=1

        # return count
        my_dict = {}
        # k=1
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 0
                # print(set1)

        # each count value is actually i + i-1 ... until i=1 inclusive
        # if count is 2 = 2+1
        # if count is 3 = 3+2+1
        act_count = 0
        for k,v in my_dict.items():
            value = v
            for i in range(1,v+1):
                act_count += i
        
        return act_count


