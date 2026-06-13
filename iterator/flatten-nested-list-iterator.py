# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    
    def next(self) -> int:
        self.makeTopInteger()
        res = self.stack.pop().getInteger()
        return res
    
    def hasNext(self) -> bool:
        self.makeTopInteger()
        if self.stack:
            return True
        else:
            return False
    def makeTopInteger(self):
        while self.stack and not self.stack[-1].isInteger():
            l = self.stack.pop().getList()
            self.stack.extend(list(reversed(l)))


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())