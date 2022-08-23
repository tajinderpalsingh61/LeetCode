# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.s = 0        
        
        def process_element(nested_int, depth):
            int_value = nested_int.getInteger()
            if int_value != None:
                #print((int_value, depth))
                self.s = self.s+(int_value*depth)

            list_value = nested_int.getList()
            if list_value != None:
                process_list(list_value, depth+1)
                
        def process_list(l, depth):
            for elem in l:
                if(str(type(elem)) == "<class 'list'>"):
                    process_list(l, depth+1)
                else:
                    process_element(elem, depth)
                

        depth = 1     
        process_list(nestedList, depth)
            
        return self.s