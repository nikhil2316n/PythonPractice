# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 


class Solution(object):
    def maximumLengthSubstring(self, s):

        count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):

            char = s[right]

            count[char] = count.get(char, 0) + 1

            # if any char frequency > 2
            while count[char] > 2:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    