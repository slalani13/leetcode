class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // create a hashmap with freq of each element <Int, Int> O(n)
        Map<Integer, Integer> mp = new HashMap<>();
        for (int num: nums) {
            mp.put(num, mp.getOrDefault(num, 0)+1);
        }
        // create a pq (minheap) in order of lowest to highest freq of size k O(nlogn)
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[1] - b[1]);
        // add and pop n pairs (freq, val) to pq O(n*logn)
        for (Map.Entry<Integer, Integer> entry: mp.entrySet()) {
            pq.offer(new int[]{entry.getKey(), entry.getValue()});
            if (pq.size() > k) {
                pq.poll();
            }
        }
        // return int[] of remaining elements
        int[] res = new int[k];
        for (int i=0; i<k;i++) {
            res[i] = pq.poll()[0];
        }
        return res;
    }
}