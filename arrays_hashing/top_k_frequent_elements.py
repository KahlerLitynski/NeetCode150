# Friday March 20th, 2026
#
# Problem: Top K Frequent Elements
# Given an integer array `nums` and an integer `k`, return the `k` most
# frequent elements within the array.
#
# The test cases are generated such that the answer is always unique.
#
# You may return the output in any order.
#
# Thought Process:
# My first thought was to use a double for loop and compare numbers repeatedly
# to count how many times each one appeared. While that would work, it would not
# be very efficient because I would be rechecking the same values over and over.
#
# I then thought about using some kind of structure where the index represented
# the number itself and the value at that index represented how many times it
# appeared. The problem with that idea is that the input values are not guaranteed
# to be small, ordered, or even convenient to map directly to indexes, so that
# approach did not feel clean or efficient.
#
# That led me to this solution, which uses both a dictionary and a frequency
# bucket list. First, I use the dictionary `count` to store how many times each
# number appears in the array. This gives me a fast and simple way to track
# occurrences.
#
# Next, I create `freq`, which is a list of empty lists. In this structure, the
# index represents a frequency count, and the value at each index is a list of
# numbers that appear that many times. For example, if the number 5 appears three
# times, then 5 gets placed into `freq[3]`.
#
# After building that structure, I loop backward through `freq` starting from the
# highest possible frequency down to 1. This lets me check the most frequent
# numbers first. As I go, I add numbers into the output list until I have exactly
# `k` elements.
#
# I liked this approach because it avoids unnecessary repeated comparisons and
# gives an efficient way to group numbers by how often they appear, then collect
# the most frequent ones in order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        print(count)
        print(freq)
        
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output



        