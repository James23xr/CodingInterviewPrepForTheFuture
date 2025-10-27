class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count = Counter(students)
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                res -=1
                count[sandwich] -=1
            else:
                break
        return res
        