

class Solution:
    def mergeArray(self, nums1, nums2):
        arr = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        while i < len(nums1):
            arr.append(nums1[i])
            i += 1

        while j < len(nums2):
            arr.append(nums2[j])
            j += 1

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        l = self.sortArray(left)
        r = self.sortArray(right)

        return self.mergeArray(l, r)