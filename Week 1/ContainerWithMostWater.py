class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = -1
        l, r = 0, len(height)-1
        while l<r:
            t = (r-l) * min([height[l],height[r]])
            if t>water:
                water = t
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water
