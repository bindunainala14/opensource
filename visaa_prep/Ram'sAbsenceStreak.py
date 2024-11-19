n = int(input())
a = map(int, input().split())
hc = 0
c = 0

for i in a:
    if i == 0:
        c += 1
        hc = max(c, hc)
    else:
        c = 0
print(hc)
