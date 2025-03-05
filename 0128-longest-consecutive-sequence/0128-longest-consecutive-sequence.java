class Solution {
    public int longestConsecutive(int[] nums) {
        // use set to store elements O(n)
        Set<Integer> s = new HashSet<>();
        int longest = 0;
        for (int num: nums) {
            s.add(num);
        }
        // find start of the sequence and obtain longest sequence O(n)
        for (int num: s) {
            if (!s.contains(num-1)) {
                int length = 1;
                while (s.contains(num+length)) {
                    length++;
                }
                longest = Math.max(longest, length);
            } 
        }
        return longest;
    }
}