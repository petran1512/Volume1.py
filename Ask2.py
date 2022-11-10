s=0
n=0
print("Calculator...")
print("To end the process type in symbol n.\n")
while s!="n":
    f=float(input("Give first number:"))
    s=input("Give symbol:")
    l=float(input("Give second number:"))
    if s=="+":
        n=f+l
    elif s=="-":
        n=f-l
    elif s=="*":
        n=f*l
    elif s=="/":
        n=f/l
    else:
        print(n)
    print(n)
print("Process end!")
