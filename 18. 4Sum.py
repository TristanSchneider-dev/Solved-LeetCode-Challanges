public class Solution {
    public IList<IList<int>> FourSum(int[] nums, int target) {
        List<IList<int>> foundSums = new List<IList<int>>();

        Array.Sort(nums);

        for (int i = 0; i < nums.Length; i++) {
            for (int j = i+1; j < nums.Length; j++) {
                long partSum0 = (long)nums[i] + nums[j];
                int tail = j + 1;
                int head = nums.Length - 1;

                while (tail < head){
                    long partSum1 = (long)nums[tail] + nums[head];

                    if (partSum0 + partSum1 == target){
                        foundSums.Add(new List<int> { nums[i], nums[j], nums[tail], nums[head] });

                        while(tail < head && nums[tail] == nums[tail+1]) tail++;
                        while(tail < head && nums[head] == nums[head-1]) head--;

                        tail++;
                        head--;

                    } else if (partSum0 + partSum1 < target){
                        tail++; 
                    } else{
                        head--;
                    }
                }
                while(j < nums.Length-1 && nums[j] == nums[j+1]) j++;
            }
            while(i < nums.Length-1 && nums[i] == nums[i+1]) i++;
        }

        return foundSums;
    }
}
