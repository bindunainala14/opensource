a, b, c, n = map(int, input().split())

if a + b >= n or b + c >= n or a + c >= n:
    print("YES")
else:
    print("NO")
