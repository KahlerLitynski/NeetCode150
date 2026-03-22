# Saturday March 21, 2026
#
# Problem: Longest Consecutive sequence:
# Given an array of integers nums, return the length of the longest sequence of
# consecutive values that can be formed. A consecutive sequence means each number
# is exactly 1 greater than the number before it. The numbers do not need to appear
# next to each other in the original array. The solution must run in O(n) time.
#
# Thought Process:
# My first idea was to sort the array and then walk through it to count how long
# each consecutive run was. That approach would work, but sorting would make the
# time complexity O(n log n), which does not meet the O(n) requirement.
#
# I also considered using nested loops to compare each number with the others and
# try to build sequences manually, but that would be too slow at O(n^2).
#
# Because of that, I went with a set-based solution. Converting the list to a set
# gives O(1) average lookup time, which makes it much faster to check whether
# neighboring values exist.
#
# The main idea in this solution is that I only start counting when I find the
# beginning of a sequence. I know a number is the start if (num - 1) is not in
# the set. From there, I keep checking whether the next number in the sequence
# exists by using the while loop.
#
# This avoids doing extra work, because numbers in the middle of a sequence are
# skipped as starting points. For example, if 3 is already part of the sequence
# 1, 2, 3, 4, I do not start counting from 3 since 2 already exists.
#
# I track the length of each valid sequence and update longest whenever I find
# a bigger one. In the end, longest holds the length of the longest consecutive
# sequence in the array.
#
# This approach is efficient because each number is checked only a small number
# of times, giving an overall time complexity of O(n) on average.



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in nums:
                length = 1
                while (num + length) in nums:
                    length +=1
                longest = max(length, longest)
        return longest
        