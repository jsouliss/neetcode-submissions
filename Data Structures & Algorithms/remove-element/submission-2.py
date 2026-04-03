class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        l = 0
        temp = 0
        for r in range(0, len(nums)):
            if nums[r] != val:
                k += 1
            if nums[r] != val and nums[l] == val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            elif nums[l] != val:  # val detected
                l = r

        return k