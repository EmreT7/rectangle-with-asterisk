# rectangle with asterisk but it's simple coded.

w = int(input("Width: "))
h = int(input("Height: "))

print("*"*w)
for i in range(h - 2):
 print("*" + " "*(w - 2) + "*")
print("*"*w)