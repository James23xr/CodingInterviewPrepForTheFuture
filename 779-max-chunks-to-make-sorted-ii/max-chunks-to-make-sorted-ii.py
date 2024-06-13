class Solution:
    def getMinValueFromRight(self, arr):
        res = []
        currMin = float('inf')
        for el in reversed(arr):
            currMin = min(el, currMin)
            res.append(currMin)

        return list(reversed(res))
        
    def maxChunksToSorted(self, arr):
        minValueFromRight = self.getMinValueFromRight(arr)
        currMax = 0
        maxChunks = 1

        for i in range(len(arr)-1):
            currMax = max(currMax, arr[i])
            if currMax <= minValueFromRight[i+1]:
                maxChunks += 1

        return maxChunks

