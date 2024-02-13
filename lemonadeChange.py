class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fives = 0
        twenty = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 5

            elif bill == 10 and fives >= 5:
                fives -= 5
                tens += 10

            elif bill == 20:
                if fives >= 5 and tens >= 10:
                    fives -= 5
                    tens -= 10
                    twenty += 20

                elif fives >= 15 :
                    fives -= 15
                    twenty += 20

                else:
                    return False


            else:
                return False

        return True





        
