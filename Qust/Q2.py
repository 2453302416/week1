import random

list=[]

for i in range(50):
    num = random.choice(range(-10,11))
    list.append(num)
print('list的长度为:',len(list))

zheng=[]
fu=[]
for i in list:
    if i>0:
        zheng.append(i)
    elif i<0:
        fu.append(i)
print('正为：',zheng)
print('负为：',fu)