class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> meow = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (meow.containsKey(comp)) {
                return new int[] {meow.get(comp), i + 1};
            }
            meow.put(nums[i], i + 1);
        }
        return new int[]{-1};
    }
}
