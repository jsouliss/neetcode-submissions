class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        size = len(nums)
        for r_ptr in range(size):
            if nums[r_ptr] != val:
                nums[k] = nums[r_ptr]
                k += 1
        return k