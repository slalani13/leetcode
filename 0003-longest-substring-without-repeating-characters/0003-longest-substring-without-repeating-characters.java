class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> hashmap = new HashMap<>();
        int l = 0;
        int r = 0;
        int longestWindow = 0;
        while (r < s.length()) {
            while (hashmap.containsKey(s.charAt(r)) && hashmap.get(s.charAt(r)) >= l) {
                l = hashmap.get(s.charAt(r)) + 1;
            }
            hashmap.put(s.charAt(r), r);
            longestWindow = Math.max(longestWindow, r-l+1);
            r++;
        }
        return longestWindow;
    }
}