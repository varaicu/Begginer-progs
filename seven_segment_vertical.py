def zero():
    print("###","\n# #","\n# #","\n# #","\n###")
    return

def one():
    print("  #","\n  #","\n  #","\n  #","\n  #")
    return

def two():
    print("###","\n  #","\n###","\n#  ","\n###")
    return

def three():
    print("###","\n  #","\n###","\n  #","\n###")
    return

def four():
    print("#  ","\n#  ","\n###","\n  #","\n  #")
    return

def five():
    print("###","\n#  ","\n###","\n  #","\n###")
    return

def six():
    print("#  ","\n#  ","\n###","\n# #","\n###")
    return

def seven():
    print("###","\n  #","\n  #","\n  #","\n  #")
    return

def eight():
    print("###","\n# #","\n###","\n# #","\n###")
    return

def nine():
    print("###","\n# #","\n  #","\n###","\n  #","\n###")
    return
def seven_display(new):
    for i in range(0, len(new)):
        if new[i]=='0':
            zero()
        elif new[i]=='1':
            one()
        elif new[i]=='2':
            two()
        elif new[i]=='3':
            three()
        elif new[i]=='4':
            four()
        elif new[i]=='5':
            five()
        elif new[i]=='6':
            six()
        elif new[i]=='7':
            seven()
        elif new[i]=='8':
            eight()
        else:
            nine()            
    return

x=input('Please enter some natural numbers:')
try: 
    int(x)
    seven_display(x)
except:
    print("Something went wrong")
