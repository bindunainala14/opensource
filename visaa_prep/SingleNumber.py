n = int(input())
a = map(int, input().split())
r = 0

for i in a:
    r ^= i
print(r)
