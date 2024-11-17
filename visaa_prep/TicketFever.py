n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    if n - m > 0:
        print(n - m)
    else:
        print(0)
