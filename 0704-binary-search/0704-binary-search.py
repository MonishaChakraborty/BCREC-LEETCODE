class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        Low,High = 0,n-1
        while Low <= High:
            mid = (Low+High)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                High = mid-1
            else:
                Low = mid+1
        return -1
        