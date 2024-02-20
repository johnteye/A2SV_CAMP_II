t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int,input().split()))
    
    bin_arr = []
    
    
    for num in arr:
        bin_num = bin(num)[2:]
        bin_arr.append(('0' * (31-len(bin_num)))+ bin_num)
        
    output= []
    for i in range(31):
        count = 0
            
        for num in bin_arr:
            if num[i] == '0':
                count +=1
        
        if count <=k:
            k -=count
            output.append(1)
        else:
            output.append(0)
                
    res = ''.join(map(str,output))   
        
    print(int(res,2))
