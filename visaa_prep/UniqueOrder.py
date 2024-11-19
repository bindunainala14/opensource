n = int(input())
m = map(int, input().split())
x = set()
res = []

for i in m:
    if i not in x:
        x.add(i)
        res.append(i)
print(" ".join(map(str, res)))
