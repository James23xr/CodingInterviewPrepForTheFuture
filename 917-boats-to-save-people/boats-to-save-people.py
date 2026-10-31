class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        boats = 0
        while l <= r:
            total = people[l] + people[r]
            if total <= limit:
                l+=1
                r-=1
                boats+=1
            else:
                r-=1
                boats+=1
        return boats

        