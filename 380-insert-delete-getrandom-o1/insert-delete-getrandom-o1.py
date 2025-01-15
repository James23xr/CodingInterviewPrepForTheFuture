import random
class RandomizedSet:
    def __init__(self):
        self.numMap = {}
        self.numList = []
    def insert(self,val):
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res
    def remove(self,val):
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numMap[lastVal] = idx
            self.numList.pop()
            del self.numMap[val]
        return res
    def getRandom(self):
        return random.choice(self.numList)
