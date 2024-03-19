t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = [(n - i)+1 for i in arr]
    print(*res)
