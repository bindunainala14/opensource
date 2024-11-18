s = input()
if s[:3] == "+91" and s[3] == " " and len(s[4:]) == 10 and s[4:].isdigit():
    print("Correct")
else:
    print("Incorrect")
