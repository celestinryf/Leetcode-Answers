class Solution {
    public int[] productExceptSelf(int[] nums) {

        int[] answer = new int[nums.length];

        for(int i = 0, temp = 1; i < nums.length; i++){
           answer[i] = temp;
            temp *= nums[i];

        }

        for(int j=nums.length - 1, temp=1; j>= 0; j--){
            answer[j] *= temp;
            temp *= nums[j];
        }
        return answer;
    }
}
