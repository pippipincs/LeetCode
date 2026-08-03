class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        hottest = 0
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            if temp > hottest:
                hottest = temp
                continue
            days = 1
            while temperatures[i + days] <= temp:
                days += res[i + days]
            res[i] = days
        return res