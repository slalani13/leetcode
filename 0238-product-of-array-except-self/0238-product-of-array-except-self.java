class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answers = new int[nums.length]; // nums: [1, 2, 3, 4]
        int prefix = 1; // 24
        for (int i = 0; i < nums.length; i++) { // [1, 1, 2, 6]
            answers[i] = prefix;
            prefix *= nums[i];
        }
        int suffix = 1; // 12
        for (int i = nums.length-1; i >= 0; i--) { // [24 , 12 , 8 , 6 ]
            answers[i] *= suffix;
            suffix *= nums[i];
        }
        return answers;
    }
}