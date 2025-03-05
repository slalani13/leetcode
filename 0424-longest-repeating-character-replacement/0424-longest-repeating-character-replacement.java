class Solution {
    public int characterReplacement(String s, int k) {
        int longest = 0;
        int[] freqs = new int[26];
        int maxFreq = 0;
        int l = 0;
        int r = 0;
        while (r < s.length()) {
            freqs[s.charAt(r)-'A'] += 1;
            maxFreq = Math.max(maxFreq, freqs[s.charAt(r)-'A']);
            while (r-l+1 - maxFreq > k ) {
                freqs[s.charAt(l)-'A'] -= 1;
                l++;
            }
            longest = Math.max(longest, r-l+1);
            r++;
        }
        return longest;
    }
}