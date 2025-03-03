class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indexes = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            int val = target - nums[i];
            if (indexes.containsKey(val)) {
                return new int[]{i, indexes.get(val)};
            }
            indexes.put(nums[i], i);
        }
        return new int[] {};
    }
}