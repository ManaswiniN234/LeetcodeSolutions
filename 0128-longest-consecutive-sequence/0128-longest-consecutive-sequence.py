class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        l = 0

        for i in s:
            if i - 1 not in s:

                curr = i
                cl = 1

                while curr + 1 in s:
                    curr += 1
                    cl += 1
                l = max(l, cl)
        return l 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna