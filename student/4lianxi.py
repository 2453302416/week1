#1. 对一字符串进行翻转操作。（20分）

str= '1qwe'
str=list(str)
str.reverse()
str1=''
for i in str:
    str1+=i
print(str1)


# 创建一个列表，存储公司10个名单，
# 对这些名单进行排序，要求按姓名的字符多少来排。（30分

list1 =['赵玉玉', '二狗', '小猪']
list1.sort()
print(list1)


# 输入用户名密码进行注册，
# 要求用户名允许数字字母6-16位，密码6-16位，不允许出现*#!（30分）
arr1 = input('请输入用户名：')

try:
    if len(arr1)>6 and len(arr1)<16:
        print('用户名创建成功')
        print(len(arr1))
    else:
        print('您输入的长度不对')
except:
    print('不允许出现*#!')
arr2 = input('请输入密码：')
try:
    if len(arr2)>6 and len(arr2)<16:
        print('密码创建成功')
        print(len(arr2))
    else:
        print('您输入的长度不对')
except:
    print('不允许出现*#!')