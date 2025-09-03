# Author: Dylan Spence

'''
https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
Merge Without Extra Space:
Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order 
without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that 
it contains the last m elements.
'''

class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        combined = a + b
        combined.sort()
        a.clear()
        a.extend(combined[:n])

        b.clear()
        b.extend(combined[n:])
        return a,b
        

test = Solution()
arr = [2, 4, 7, 10]
arr2 = [2, 3]
print(test.mergeArrays(arr, arr2))