n = int(input())
a = list(map(int, input().split()))
m = int(input())

found = False

for i in range(0, n):
    for j in range(i + 1, n):
        if a[i] + a[j] == m:
            print("true")
            found = True
            break
    if found:
        break

if not found:
    print("false")
