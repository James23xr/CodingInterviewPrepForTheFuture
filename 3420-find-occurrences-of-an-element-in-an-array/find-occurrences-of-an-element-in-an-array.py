class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurences = [-1] * len(nums)
        res = []
        curr_point = 0
        for i in range(len(nums)):
            if nums[i] == x:
                occurences[curr_point] = i
                curr_point +=1
        for i in range(len(queries)):
            point = queries[i] -1
            if point >= len(occurences):
                res.append(-1)
            else:
                res.append(occurences[point])
        return res


        