"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

from typing import List


class Solution:

    # Changed to static method
    @staticmethod
    def trap(height: List[int]) -> int:

        total_water = 0

        for i in range(len(height)):
            max_left = max(height[:i+1])
            max_right = max(height[i:])
            smallest_wall = min(max_left, max_right)
            total_water += smallest_wall - height[i]

        return total_water


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution.trap(height))
