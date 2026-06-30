class Solution {
    public int longestConsecutive(int[] nums) {
        int max = Math.min(nums.length, 1);
        Arrays.sort(nums);
        Map<Integer, Integer> count = new HashMap<>();

        for (int num: nums) {
            if (count.containsKey(num-1)) {
                count.put(num, count.get(num-1)+1);
                max = Math.max(max, count.get(num));
            } else {
                count.put(num, 1);
            }
        }

        return max;
    }
}
