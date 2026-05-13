class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        counter = 0
        size = len(nums)

        for i in range(size):
            if nums[i] == 1:
                counter += 1
            if counter > max_count:
                max_count = counter
            if nums[i] != 1:
                counter = 0

        return max_count