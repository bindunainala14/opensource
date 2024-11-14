x, y, z = map(int, input().split())
c = 0
z = z - y
while z > x:
    z = z - x
    c = c + 1
print(c)
    
