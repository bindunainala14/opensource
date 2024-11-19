n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

for row in m:
    print(" ".join(map(str, row[::-1])))
