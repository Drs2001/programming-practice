# Author: Dylan Spence

'''
https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
Kadane's Algorithm:

You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

Note : A subarray is a continuous part of an array.
'''

class Solution:
    def maxSubarraySum(self, arr):
        if arr:
            res = arr[0]
            maxEnding = arr[0]
            for i in range(1, len(arr)):
                maxEnding = max(maxEnding + arr[i], arr[i])
                res = max(res, maxEnding)
            return res
        return 0

test = Solution()
arr = [5, 4, 1, 7, 8]
print(test.maxSubarraySum(arr))
