class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = 0
        size = len(arr)
        max_num = arr[size - 1]
        r_ptr = size - 1

        while curr < size - 1:
            if arr[r_ptr] > max_num:
                max_num = arr[r_ptr]
            else:
                r_ptr -= 1
            if r_ptr == curr:
                arr[curr] = max_num
                max_num = arr[size - 1]
                r_ptr = size - 1
                curr += 1
        arr[size - 1] = -1

        return arr