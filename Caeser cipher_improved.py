text = input("Enter your message: ")
step = input("Enter the crypting step (1-25):")
cipher = ''

try:
    step=int(step)
    for char in text:
        if ord(char)>=65 and ord(char)<=90:
            if ord(char)+step>90:
                code=64+ord(char)+step-90
            else:
                code = ord(char) + step
        elif ord(char)>=97 and ord(char)<=122:
            if ord(char)+step>122:
                code=96+ord(char)+step-122
            else:
                code = ord(char) + step
        else:
            code = ord(char)
        cipher += chr(code)
    print(cipher)
except ValueError:
    print("The step should be an integer value")
    
#Majuscule ASCII intre 65 = A si 90 =Z, se verifica daca este litera mare,
#adica ASCII este intre 65 si 90
#in caz pozitiv - se verifica daca ASCII + pas >90, ce este peste 90 se
#calculeaza 64+ (ASCII+pas-90)

#Litere mici ASCII 97=a si 122 = z, se verifica daca este litera mica,
#adica ASCII este intre 97 si 122
#in caz pozitiv se verfica daca ASCII + pass>122, ce este peste 122 se
#calculeaza 96+(ASCII+pas-122)

    
