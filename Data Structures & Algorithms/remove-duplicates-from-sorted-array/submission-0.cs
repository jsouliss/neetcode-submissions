public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int k = 0;
        int num_size = nums.Length;
        int l = 1;

        for(int r = 1; r < num_size; ++r) {
            if (nums[r] != nums[r - 1]) {
                nums[l] = nums[r];
                l++;
            }
        }

        return l;
    }
}