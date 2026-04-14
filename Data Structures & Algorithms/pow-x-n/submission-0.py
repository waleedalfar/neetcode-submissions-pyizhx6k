class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n > 0:
            for i in range(0, n):
                res *= x
            return res
        for i in range(0, abs(n)):
            res *= x
        return 1/res