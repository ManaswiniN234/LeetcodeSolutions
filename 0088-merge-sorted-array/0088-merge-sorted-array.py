class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m1 = nums1[:m]
        n1 = nums2[:n]

        ans = []
        i = 0
        j = 0
        while i < m and j < n:
            if m1[i] <= n1[j]:
                ans.append(m1[i])
                i += 1
            else:
                ans.append(n1[j])
                j += 1
        while i < m:
            ans.append(m1[i])
            i += 1
        while j < n:
            ans.append(n1[j])
            j += 1
        nums1[:] = ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna