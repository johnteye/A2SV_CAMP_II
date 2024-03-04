def solution(num):
    if num == 1:
        return 3
    
    if bin(num).count("1") == 1:
        return num + 1
    
    i = 0
    while num & (1 << i) == 0:
        i += 1

    return 1 << i

t = int(input())

for _ in range(t):
    num = int(input())

    print(solution(num))

    


