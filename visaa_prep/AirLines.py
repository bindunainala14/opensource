n, m = map(int, input().split())

d = m - (n * 100)
c = 0

while d > 0:
    c = c + 1
    d = d - 100
print(c)
