import random
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '

print("原字符串",s)
s=s.replace(".","")
print("替换的字符串",s)
s=s.split(" ")

s.pop()
print("去空格",s)
dict={}

for i in s :
    key = dict.get(i)
    if key == None:
        dict[i]=1
    else:
        dict[i]+=1

dict1 ={}

sv= list(dict.values())
sv.sort()

#去除个数相同 减少循环

sv = set(sv)

sv=list(sv)

#实现单词的升序

for j in dict:
    if(dict[j]==i):
        dict1[j]=i

#打印结果
print(dict1)