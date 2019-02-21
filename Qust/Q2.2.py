import random

list =[]

for i in range(50):
    sum=random.choice(range(-10,10))
    list.append(sum)
print('长度为:',len(list))

zheng=[]
fu=[]
for i in list:
    if i > 0:
        zheng.append(i)
    elif i<0:
        fu.append(i)
print(zheng)
print(fu)