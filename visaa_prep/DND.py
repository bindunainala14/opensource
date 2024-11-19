n, m = map(int, input().split())
a = 0
b = 0


d = map(int, input().split())
for x in d:
    if x % m == 0:
        a += x
    else:
        b += x
            
print(a - b)
