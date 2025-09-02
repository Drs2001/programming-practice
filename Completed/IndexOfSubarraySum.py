# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
# Author: Dylan Spence
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
