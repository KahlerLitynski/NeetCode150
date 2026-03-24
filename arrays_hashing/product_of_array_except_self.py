# Monday March 23, 2026
#
# Problem: Products of Array Except Self
# Given an integer array nums, return an array output where each output[i]
# is equal to the product of every element in nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
#
# Thought Process:
# My first idea was to multiply all of the numbers together and then divide by
# the current number to get the product of every element except itself.
# That works fine at first, but the problem gets more complicated once zeros
# are involved.
#
# I then had to account for a single zero. If there is one zero in the array,
# every position except the zero's position should return 0, and the zero's
# position should return the product of all non-zero values.
#
# After that, I needed to account for multiple zeros. If there are two or more
# zeros, then every result must be 0 because every product will include at
# least one zero.
#
# I also had to handle the case where the array is made up of only zeros, which
# is covered by the multiple-zero logic since every output would still be 0.
#
# So the final approach was:
# 1. Loop through nums and multiply only the non-zero values together.
# 2. Count how many zeros appear in the array.
# 3. Build the result based on the zero count:
#    - More than one zero -> all outputs are 0
#    - Exactly one zero -> only the zero position gets the non-zero product
#    - No zeros -> divide the total product by nums[i]
#
# This let me keep the original idea while correctly handling all of the
# special zero cases.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zero_cnt = 0
        total = 0
        for num in nums:
            if num:
                if not total:
                    total = 1
                total *= num
            else:
                zero_cnt += 1
        for i in range(len(nums)):
            if zero_cnt >= 1 and nums[i] or zero_cnt > 1:
                output.append(0)
            elif not nums[i]:
                output.append(total)
            else:
                output.append(total // nums[i])

        return output
        