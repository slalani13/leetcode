class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();;
        // sort array
        Arrays.sort(nums);
        // iterate through the array and run 2 sum on pair of numbers
        for (int i=0; i<nums.length; i++) {
            if (nums[i] > 0) { // check for positive value
                break;
            }
            if (i > 0 && nums[i] == nums[i-1]) { // check for duplicate a values
                continue;
            }
            int a = nums[i];
            int left = i+1;
            int right = nums.length-1;
            while (left < right) {
                int ssum = a + nums[left] + nums[right];
                if (ssum == 0) {
                    res.add(Arrays.asList(a, nums[left], nums[right]));
                    left++;
                    right--;
                    // check for duplicate b values
                    while (left < right && nums[left] == nums[left-1]) {
                        left++;
                    }
                }
                else if (ssum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        return res;
    }
}