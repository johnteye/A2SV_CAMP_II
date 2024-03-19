def solve():
    n = int(input())
    arr = list(map(str, input().split("#")))
    res = []
    for i in arr:
        if len(i) >= 3:
            return 2
        res.append(len(i))

    return sum(res)

t= int(input())
for _ in range(t):  
    print(solve())
