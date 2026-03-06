class Solution:
    def candy(self, ratings: List[int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i - 1] + 1
        for j in range(len(ratings) -2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                right2left[j] = right2left[j + 1] + 1
        candies = 0
        for i in range(len(ratings)):
            candies += max(left2right[i], right2left[i])
        return candies
        