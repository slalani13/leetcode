class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;
        // create a hashmap with freq of each element <Int, Int> O(n)
        Map<Integer, Integer> mp = new HashMap<>(); // <num, freq>
        List<Integer>[] buckets = new List[nums.length+1]; // [[num], [num]] index is freq
        for (int num: nums) {
            mp.put(num, mp.getOrDefault(num, 0)+1);
        }
        for (Map.Entry<Integer, Integer> entry: mp.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }
        int[] res = new int[k];
        int index = 0;
        for (int i=buckets.length-1; i >= 0 && index < k; i--) {
            if (buckets[i] != null) {
                for (int num: buckets[i]) {
                    res[index] = num;
                    index++;
                    if (index == k) {
                        return res;
                    }
                }
            }
        }
        return res;
    }
}