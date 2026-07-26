class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # turn into arr of pairs
        pair = [[p, s] for p, s in zip(position, speed)]

        fleets = [] # stack of fleets
        
        for p, s in sorted(pair)[::-1]:
            
            # time each car reaches target
            fleets.append((target - p) / s)

            # if destinationt times overlap
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop() # decrease num of car fleets, ^ 1 fleet 2 cars

        return len(fleets)




