# 1) String manipulation
# You are given the string: “HELLO WORLD”. You must print each character of the string in a new line. For example:
# H
# E
# L
# L
# O
#
# W
# O
# R
# L
# D

h = "HELLO WORLD"
# while i < len(h):
for i in h:
    print (i)

Or

h = "HELLO WORLD"
i = 0
while i < len(h):
    print (h[i])
    i += 1

Or

h = "HELLO WORLD"
i = 0
# while i < len(h):
for i in range(0,len(h)):
    print (h[i])
    i += 1

Or

h = "HELLO WORLD"
# while i < len(h):
for i in h:
    print (i)