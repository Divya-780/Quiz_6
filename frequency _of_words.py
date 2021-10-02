text=input("enter a text for book::")
words=text.split(" ")
dict_={}

for i in words:
    if i in dict_:
        dict_[i]=dict_[i]+1
    else:
        dict_[i]=1
#print(dict)
a = sorted(dict_.values(),reverse=True)
print(a)
#for keys,a in dict_.items():
 # print(keys,"=",a)
