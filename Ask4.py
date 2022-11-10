ph=str(input("Give phrase:"))
let=str(input("Give letter:"))
i=0;f=0
if len(ph)==0:
    print("Nothing.")
else:
    while i<=len(ph)-1 :
        if ph[i]==let:
            f=f+1
        i=i+1    
    print('The letter',let,'exists',f,'times in this phrase.')
