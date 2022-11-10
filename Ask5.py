# 5) Given the string in (1) remove (hint: replace) all vowels. For example: HLL WRLD

h =input("wright:")
v=("a","e","i","o","u","A","E","I","O","U")
x = ""
for i in h:
    if i  in v:
        pass
    else:
        x += i

print(x)

Or

h = "HELLO WORLD"
for i in h:
    if i in "EO":
        print("",end="")
    else:
        print(i,end=“”)

Or

h =input("wright:")
v=("a","e","i","o","u","A","E","I","O","U")
x = ""
for i in h:
    if i  in v:
        pass
    else:
        x += i

print(x)

*try replace*