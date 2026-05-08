class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for x in nums1:
            found = False
            result = -1

            # find x in nums2
            for i in range(len(nums2)):
                if nums2[i] == x:
                    # search to the right
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > x:
                            result = nums2[j]
                            found = True
                            break
                    break

            ans.append(result)

        return ans

