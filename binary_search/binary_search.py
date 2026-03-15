# Sunday March 15th, 2026
#
# Problem: Binary Search:
# Given a sorted array of distinct integers `nums` and an integer `target`,
# return the index of `target` if it exists in the array.
# If `target` is not found, return -1.
# The solution must run in O(log n) time.
#
# Thought Process:
# Since the array is sorted, binary search is the most efficient approach.
# My first attempt was less polished because I tried to solve it using only
# a middle pointer instead of tracking both left and right pointers.
#
# To improve the solution, I added left and right variables so the search
# range is clear and easier to update each step.
# I also considered adding a "not in" check at the beginning, but that would
# increase the overall time complexity because it would require a linear scan.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle +1
        return -1