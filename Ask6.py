# 6) Count and print each character in the string given in (1) in a new line per character. For example:
# H: 1
# E: 1
# L: 3
# O: 2
#  : 1
# W: 1
# R: 1
# D: 1

h = "HELLO WORLD"
text = {}
for i in h:
    if i in text:
        text[i] += 1
    else:
        text[i] = 1
# print(text["H"])
# print(text.keys())
for i in text:
    print(i,":",text[i])

#OR

h = "HELLO WORLD"
text = {}
for i in h:
    if i in text:
        text[i] += 1
    else:
        text[i] = 1
print (str(text))h = "HELLO WORLD”

for i in h:
    if i in "eoEO":
        print("",end="")
    else:
        print(i,end="")


#or


h = "HELLO WORLD"
text = {}
for i in h:
    if i in text:
        text[i] += 1
    else:
        text[i] = 1
# print(text["H"])
# print(text.keys())
for i in text.keys(): *for in text:*
    print(i,":",text[i])