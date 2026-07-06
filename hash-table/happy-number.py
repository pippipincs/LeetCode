class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(num):
            s = 0
            while num > 0:
                digit = num % 10
                s += digit * digit
                num = num // 10
            return s
        fast = getNext(n)
        slow = n
        while fast != 1 and fast != slow:
            fast = getNext(getNext(fast))
            slow = getNext(slow)
        return fast == 1