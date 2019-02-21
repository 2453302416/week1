import random

str = 'abcd'
str2=''
for i in range(1000):
    str2 += random.choice(str)
print('长度为：',len(str2))
dict={}
for i in str2:
    key = dict.get(i)
    if key==None:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)