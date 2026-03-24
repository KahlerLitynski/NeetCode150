# Tuesday, March 24, 2026
#
# Problem: Two Integer Sum II
# Given an array of integers numbers sorted in non-decreasing order,
# return the 1-indexed positions of two numbers such that they add up
# to the target value.
#
# The returned answer should be in the form [index1, index2], where
# index1 < index2. You may not use the same element twice.
#
# There will always be exactly one valid solution.
#
# Thought Process:
# Since the array is already sorted, I went with the two-pointer approach
# from the beginning. My idea was to place one pointer at the start of the
# array and the other at the end, then check the sum of those two values.
#
# If the sum is greater than the target, I know I need a smaller number, so
# I move the right pointer to the left. If the sum is less than the target,
# I know I need a larger number, so I move the left pointer to the right.
#
# Because the array is sorted, each pointer movement is meaningful and helps
# narrow in on the correct pair without needing to check every combination.
# This makes the solution much more efficient than a brute-force approach.
#
# I keep moving the pointers until their sum matches the target, then return
# the indices as 1-indexed values to match the problem requirements.




class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while not numbers[index1] + numbers[index2] == target:
            if numbers[index1] + numbers [index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers [index2] < target:
                index1 += 1
        return sorted([index1 + 1, index2 + 1])