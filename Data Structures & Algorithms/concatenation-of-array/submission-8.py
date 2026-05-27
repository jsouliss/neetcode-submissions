from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = (2 * size) * [0] # twice size of nums
        ans_size = len(ans)

        for i in range(ans_size):
            if i < size: 
                ans[i] = nums[i]
            else:
                ans[i] = nums[i - size]
        return ans

def main():
    nums = [1,4,1,2]
    my_sol = Solution()
    my_sol.getConcatenation(nums)

if __name__ == '__main__':
    main()