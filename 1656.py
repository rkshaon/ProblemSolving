# 1656
# Design an Ordered Stream
# Easy
# https://leetcode.com/problems/design-an-ordered-stream/
# Array, Hash Table, Design, Data Stream

class OrderedStream:

    def __init__(self, n: int):
        self.list = [None] * n
        self.pointer = 0
        

    # def insert(self, idKey: int, value: str) -> List[str]:
    #     pass
    def insert(self, idKey: int, value: str) -> list[str]:
        self.list[idKey-1] = value

        result = []

        while self.pointer < len(self.list) and self.list[self.pointer] is not None:
            result.append(self.list[self.pointer])
            self.pointer += 1
        
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)