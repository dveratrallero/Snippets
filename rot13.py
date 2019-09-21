import string
def rot13(message):
    #your code here
    stdn=string.ascii_lowercase
    stup=string.ascii_uppercase
    msg=""
    for l in message:
        if l.islower():
            msg+=stdn[(stdn.index(l)+13)%26]
        elif l.isupper():
            msg+=stup[(stup.index(l)+13)%26]
        else:
            msg+=l
    return msg
            
