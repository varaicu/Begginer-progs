x=input("Please enter the numbers")
if x.isdigit():
    l=[x[y] for y in range(len(x))]
    print(l)
else:
    print("you did not enter numbers")


s = ['  x','x  ','x x','xxx']
for j in range(5):
    for i in range(len(x)):
        if j==0:
            if int(x[i])==1:
                print(s[0], end=' ')
            elif int(x[i]) in (2,3,5,6,7,8,9,0):
                print(s[3], end=' ')
            elif int(x[i])==4:
                print(s[1], end=' ')
        elif j==1:
            if int(x[i]) in (8,9,0):
                print(s[2], end=' ')
            elif int(x[i]) in (1,2,3,7):
                print(s[0], end=' ')
            elif int(x[i]) in (4,5,6):
                print(s[1], end=' ')
        elif j==2:
            if int(x[i]) in (1,7):
                print(s[0], end=' ')
            elif int(x[i]) in (2,3,4,5,6,8,9):
                print(s[3], end=' ')
            elif int(x[i])==0:
                print(s[2], end=' ')
        elif j==3:
            if int(x[i])in (1,3,4,5,7,9):
                print(s[0], end=' ')
            elif int(x[i])==2:
                print(s[1], end=' ')
            elif int(x[i]) in (6,8,0):
                print(s[2], end=' ')
        elif j==4:
            if int(x[i])in (1,4,7):
                print(s[0], end=' ')
            elif int(x[i]) in (2,3,5,6,8,9,0):
                print(s[3], end=' ')
                
    print()        

