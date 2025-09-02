# Author: Dylan Spence

''' 
https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
Indexes of Subarray Sum:
Given an array arr[] containing only non-negative integers, your task is to find a continuous 
subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need 
to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need 
to find the first subarray whose sum is equal to the target.
'''

class Solution:
    def subarraySum(self, arr, target):
        i = 0
        j = 0
        count = 0
        while(i < len(arr)):
            count += arr[j]
            if count > target:
                i += 1
                j = i
                count = 0
            elif count == target:
                return [i+1, j+1]
            else:
                j += 1
                if j >= len(arr):
                    return [-1]
        return [-1]

arr = [10, 23, 18, 20, 26, 25]
target = 12
test = Solution()
print(test.subarraySum(arr, target))
