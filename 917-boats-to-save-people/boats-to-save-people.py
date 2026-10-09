class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1    
        boats = 0
        while l<=r:
            s = people[l] + people[r]
            if s <= limit:
                l+=1
                r-=1
                boats +=1
            elif s > limit:
                r-=1
                boats+=1
        return boats
        