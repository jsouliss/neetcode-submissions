public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int curr = 0;
        for (int next = 1; next < nums.Length; ++next)
        {
            if (nums[curr] != nums[next])
            {
               curr++;
               nums[curr] = nums[next];
            }
        }
        return curr + 1;
    }
}