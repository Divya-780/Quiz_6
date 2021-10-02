text=input("enter a text for book::")
words=text.split(" ")
dict_={}

for i in words:
    if i in dict_:
        dict_[i]=dict_[i]+1
    else:
        dict_[i]=1

print(sorted(dict_.items()))
