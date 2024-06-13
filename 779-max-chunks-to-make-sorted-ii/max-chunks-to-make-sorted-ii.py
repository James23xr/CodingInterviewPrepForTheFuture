class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        acc = zip(accumulate(arr), accumulate(sorted(arr)))

        return len(tuple(filter(lambda x: x[0] == x[1],acc)))