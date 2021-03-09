x=input("Please enter the numbers")
if x.isdigit():
    l=[x[y] for y in range(len(x))]
    print(l)
else:
    print("you did not enter numbers")


for i in range(len(x)):
    if int(l[i])==1:
        for j in range(5):
            print("  #")
                
    elif int(l[i])==2:
        for j in range(5):
            if j%2==0:
                print("###")
            else:
                if int(j//2)==0:
                    print("  #")
                else:
                    print("#  ")
    elif int(l[i])==3:
        for j in range(5):
            if j%2==0:
                print("###")
            else:
                print("  #")
    elif int(l[i])==4:
        for j in range(2):
            print("#  ")
        print("###")
        for j in range(2):
            print("  #")
    elif int(l[i])==5:
        for j in range(5):
            if j%2==0:
                print("###")
            else:
                if int(j//2)==1:
                    print("  #")
                else:
                    print("#  ")
    elif int(l[i])==6:
        for j in range(2):
            print("  #")
        for j in range(3):
            if j%2==0:
                print("###")
            else:
                print("# #")
    elif int(l[i])==7:
        for j in range(5):
            if j==0:
                print("###")
            else:
                print("  #")
    elif int(l[i])==8:
        for j in range(5):
            if j%2==0:
                print("###")
            else:
                print("# #")
    elif int(l[i])==9:
        for j in range(3):
            if j%2==0:
                print("###")
            else:
                print("# #")
        for j in range(2):
            print("  #")
    else:
        for j in range(5):
            if j%2==0 and j!=2:
                print("###")
            else:
                print("# #")        

