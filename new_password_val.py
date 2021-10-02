#import regular expression
import re  
#taking password from user
pwd=input("Please enter your password here:")
pwd_len=len(pwd)
flag=0
while True:
    if pwd_len>=8:
        if not re.search("[a-z]",pwd):
            flag=0
            break
        elif not re.search("[A-Z]",pwd):
            flag=0
            break
        elif not re.search("[0-9]",pwd):
            flag=0
            break
        elif not re.search("[$#@]",pwd):
            flag=0
            break
        else:
            flag=1
            print("given password is valid")
            break
    else:
        print("entered pswd lengthmust be greater than 8")
        break
if flag==0:
    print("not a valid password")





