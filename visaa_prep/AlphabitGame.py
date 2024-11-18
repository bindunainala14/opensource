s = input()
c = 0
v = 0
for i in s:
    if i.lower() in 'aeiou':
        v += 1
    elif i.isalpha():
        c += 1
print(f"{v},{c}")
        
