class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapp = {}
        seen = set()
        for i, j in zip(s,t):
            if i in mapp:
                if mapp[i] != j:
                    return False
            else:
                if j in seen:
                    return False
                mapp[i] = j
                seen.add(j)
        return True

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna