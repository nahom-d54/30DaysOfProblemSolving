from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            h[i] = h.get(i, 0) + 1
            if h[i] > 1:
                return True
        return False
