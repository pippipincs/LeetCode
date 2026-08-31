class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num = str(n)
        digits = list(num)
        for i in range(len(digits) - 1, 0, -1):
            if int(digits[i - 1]) > int(digits[i]):
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                digits[i] = '9'
        if digits[0] == '0':
            digits = digits[1:]
        return int("".join(digits))