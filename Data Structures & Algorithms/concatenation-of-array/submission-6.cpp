class Solution {
public:
    std::vector<int> getConcatenation(std::vector<int>& nums) {
        int size = static_cast<int>(nums.size());
        std::vector<int>ans;
        if (size >= 1 && size <= 1000) {
            int k = 0;
            size *= 2;
            for (int i = 0; i < size; ++i, ++k) {
                if (i == size / 2 ) {
                    k = 0;
                }
                ans.push_back(nums[k]);
            }
            return ans;
        }
        return nums;
    }
};