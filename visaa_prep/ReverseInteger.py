n = int(input())
n = int(str(n)[::-1])
b = bin(n)
if len(b) <= 32:
    print(n)
else:
    print("0")
