x, y, z = map(int, input().split())

if x > z:
    print("0")
if x + y > z:
    print("1")
if x + y <= z:
    print("2")
