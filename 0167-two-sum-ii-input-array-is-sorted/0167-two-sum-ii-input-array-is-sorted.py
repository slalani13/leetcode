class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg = 0
        end = len(numbers)-1
        while (beg <= end):
            if numbers[beg] + numbers[end] == target:
                return [beg+1,end+1]
            elif numbers[beg] + numbers[end] < target:
                beg+=1
            else:
                end-=1

