t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().lstrip("0 ").split()))
    sum_ = sum(arr[:-1]) + arr[:-1].count(0)
    print(sum_)
