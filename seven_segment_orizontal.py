def seven_display(new):
    lis=[["###","# #","# #","# #","###"],
    ["  #","  #","  #","  #","  #"],
    ["###","  #","###","#  ","###"],
    ["###","  #","###","  #","###"],
    ["#  ","#  ","###","  #","  #"],
    ["###","#  ","###","  #","###"],
    ["#  ","#  ","###","# #","###"],
    ["###","  #","  #","  #","  #"],
    ["###","# #","###","# #","###"],
    ["###","# #","  #","###","  #","###"]]
    
    for i in range(0,5):
        for j in range (0,len(new)):
            print(lis[int(new[j])][i], end=' ')           
        print()
    return

x=input('Please enter some natural numbers:')
try: 
    int(x)
    seven_display(x)
except:
    print("Something went wrong")
