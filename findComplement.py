class Solution:
    def findComplement(self, num: int) -> int:
        bit_num = []
        while num > 0:
            bit_num.append(num % 2)
            num = num // 2
        bit_num.reverse()

        print(bit_num)
        for i in range(len(bit_num)):
            bit_num[i] ^= 1
        print(bit_num)

        return int ( "".join(map(str, bit_num)) , 2)
       
        
        

