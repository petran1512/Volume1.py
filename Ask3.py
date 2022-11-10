# 3) Given the string in (1), lowercase first and last character of each word.
# For example: hELLo wORLd

h = "HELLO WORLD"
h = h[0].lower() + h[1:4].upper() + h[4:7].lower() +h[7:10].upper() +  h[-1].lower()
print(h)