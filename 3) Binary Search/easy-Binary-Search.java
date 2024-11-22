class Solution {
    public int search(int[] nums, int t) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            int mid = (start + end) / 2;
            if (nums[mid] < t) {
                start = mid + 1;
            } else if (nums[mid] > t) {
                end = mid;
            } else {
                return mid;
            }
        }
        if (t == nums[start]) {
            return start;
        } else {
            return -1;
        }

        // int l = 0
        // r = nums.length - 1;
        // while (l <= r) {
        //     int m = l + ((r - l) / 2);
        //     if (nums[m] > target) {
        //         r = m - 1;
        //     } else if (nums[m] < target) {
        //         l = m + 1;
        //     } else {
        //         return m;
        //     }
        // }
        // return -1;
    }
}
