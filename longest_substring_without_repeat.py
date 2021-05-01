class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        tem, res, ptr = {}, 0, 0
        for i, ch in enumerate(A):
            if ch in tem:
                ptr = max(ptr, tem[ch] + 1)
            tem[ch] = i
            res = i + 1 - ptr if i + 1 - ptr > res else res
        return res