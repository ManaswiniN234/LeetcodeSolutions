class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        ans = []

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            ans.append(first[i])
        return "".join(ans)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna