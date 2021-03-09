cipher = input('Enter your cryptogram: ')
step = input("Enter the decrypting step (1-25):")
text = ''
try:
    step=int(step)
    for char in cipher:
        if ord(char)>=65 and ord(char)<=90:
            if ord(char)-step<65:
                code=ord(char)-64+90-step
            else:
                code = ord(char) - step
        elif ord(char)>=97 and ord(char)<=122:
            if ord(char)-step<97:
                code=ord(char)-96+122-step
            else:
                code = ord(char) - step
        else:
            code = ord(char)
        text += chr(code)
    print(text)
except ValueError:
    print("The step should be an integer value")

