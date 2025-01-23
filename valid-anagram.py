class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        for j in t:
            k = h.get(j)
            if not k:
                return False
            h[j] = k - 1
        if sum(h.values()) != 0:
            return False
        return True
