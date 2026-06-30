class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l, r = 0, len(heights)-1

        while l < r:
            lh, rh = heights[l], heights[r]
            res = max(res, (r-l) * min(lh, rh))

            if lh < rh:
                l += 1
            else:
                r -= 1

        return res