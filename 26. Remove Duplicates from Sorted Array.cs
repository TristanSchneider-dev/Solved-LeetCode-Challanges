public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int counter = 0;

        for (int i; i < nums.Length; i++){
            int j = 1;
            while (nums[i] == nums[i+j]){
                j++;
            }
            nums[i+1] = nums[i+j+1];

        }
        
        return counter;
    }
}
