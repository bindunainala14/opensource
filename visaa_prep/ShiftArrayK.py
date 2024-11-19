n = int(input())
a = list(map(int, input().split()))
m = int(input())

m = m % n
res = a[-m:] + a[:-m]
print(" ".join(map(str, res)))
