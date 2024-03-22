def count(n):
    if n <= 0: 
        return 0
    if n % 2 != 0:
        return 0
    
    return 1 + count(n/2)

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for val in arr:
        ans += count(val)

    if ans >= n:
        return 0
    
    res = []
    for i in range(1, n+1):
        if count(i):
            res.append(count(i))
        
    res = sorted(res, reverse = True)
    sum_ , step = 0 ,0
    for val in res:
        sum_ += val
        step += 1
        if sum_ >= (n - ans):
            return step
        
    return -1


t = int(input())
for _ in range(t): 
    print(solve())
