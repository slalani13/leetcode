class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hashmap = new HashMap<>();
        for (String word: strs) {
            int[] count = new int[26];
            for (char c : word.toCharArray()) {
                count[c-'a'] += 1;
            }
            String key = Arrays.toString(count);
            hashmap.putIfAbsent(key, new ArrayList<String>());
            hashmap.get(key).add(word);
        }
        return new ArrayList<>(hashmap.values());
    }
}