class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        n = len(costs)/2
        a_count , b_count = 0, 0
        costs = sorted(costs, key = lambda x:abs(x[0] - x[1]), reverse = True)

    
        for place in costs:
            if  a_count < n and b_count < n:
                if  place[0] < place[1]:
                    total += place[0]
                    a_count += 1
                else:
                    total += place[1]
                    b_count += 1

            elif a_count == n:
                total += place[1]
                b_count += 1

            else:
                total += place[0]
                a_count += 1
        
        return total
