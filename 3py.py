sen = input()
l = 0
d = 0
for i in sen:
    if i.isalpha():
        l += 1
    elif i.isdigit():
        d += 1
print("LETTERS", l)
print("DIGITS", d)
