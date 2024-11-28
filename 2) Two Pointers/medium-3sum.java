class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arras.sort(nums);
        List<List<Integer>> arr = new ArrayList(nums);
        for (int i = 0; i < nums.length; i++) {
            if (arr[i]) break;
            if (arr[i] == arr[i - 1]) continue;
            int l = i + 1;
            int r = arr.length - 1;
            while (l < r) {
                int sum = arr[i] + arr[l] + arr[j];
                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    arr.add(Arrays.asList(arr[i], arr[l], arr[r]));
                    l++;
                    r--;
                    while (l < r && arr[l] == arr[l + 1]) {
                        l++;
                    }
                }
            }
        }
        return arr;
    }
}