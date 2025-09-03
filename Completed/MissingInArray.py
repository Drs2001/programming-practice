# Author: Dylan Spence

'''
https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
Missing in Array:
You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). 
This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify 
and return the missing element.
'''

class Solution:
    def missingNum(self, arr):
        arr.sort()
        if arr[0] != 1:
            return 1
        
        if len(arr) == 1:
            return arr[0]+1

        i = 1
        for val in arr:
            if i >= len(arr):
                return arr[len(arr)-1] + 1
            elif (val+1) != arr[i]:
                return val + 1
            i += 1
        return -1


test = Solution()

arr = [1, 2, 3]
print(test.missingNum(arr))
