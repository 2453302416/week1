import random
list=[]
# 循环随机20个整数
for i in range(20):
    sum=random.choice(range(10))
    #添加到列表
    list.append(sum)
print('长度为：',len(list))
print('未排序的为：',list)
# 偶数下标 排序后 翻转
list[::2]=sorted(list[::2],reverse=True)
print('排序的为：',list)