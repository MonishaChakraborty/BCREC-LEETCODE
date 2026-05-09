class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        # Sum of first window
        window_sum = sum(arr[:k])

        # Store maximum sum
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum
        