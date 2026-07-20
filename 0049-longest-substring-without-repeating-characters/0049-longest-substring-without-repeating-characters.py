class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        l = 0
        maxlen = 0

        for i in range(len(s)):
            if s[i] in freq and freq[s[i]] >= l:
                l = freq[s[i]] + 1
            freq[s[i]] = i
            maxlen = max(maxlen, i - l + 1)
        return maxlen

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna