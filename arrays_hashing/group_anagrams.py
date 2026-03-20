# Thursday March 19th
#
# Problem: Group Anagrams
# Given an array of strings `strs`, group all anagrams together into sublists.
# You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another
# string, but the order of the characters can be different.
#
# Thought Process:
# I approached this problem by thinking about what makes two words anagrams.
# Even if the letters are in a different order, anagrams will contain the exact
# same characters. Because of that, I decided to sort each string so that all
# anagrams would produce the same normalized form. For example, "eat", "tea",
# and "ate" all become "aet" when sorted.
#
# From there, I used a dictionary to keep track of which group each sorted word
# belongs to. If I had already seen that sorted pattern before, I added the
# current string to the existing group. If I had not seen it before, I created
# a new group for it and stored its index in the dictionary.
#
# I liked this approach from the beginning because it is direct and efficient.
# It avoids comparing every word against every other word, and instead gives me
# a reliable way to group matches using the sorted version of each string as a key.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        cnt = 0
        anagrams = {}

        for string in strs:
            key = str(sorted(string))

            if key in anagrams:
                output[anagrams[key]].append(string)
            else:
                anagrams[key] = cnt
                output.append([string])
                cnt += 1

        return output