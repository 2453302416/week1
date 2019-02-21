import random
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '

print("原字符串",s)
s=s.replace(".","")
print("替换后的字符串为：",s)
#单词切割出来
s=s.split(" ")
s.pop()
print("去除空白字符列表",s)
dict={}
for i in s:
    key = dict.get(i)
    # 每个单词的数量
    if(key==None):
        dict[i]=1
    else:
        dict[i]+=1

dict1={}

sv = list(dict.values())
sv.sort()

sv=set(sv)
sv=list(sv)

for i in sv:
    for j in dict:
        if (dict[j]==i):
            dict1[j]=i

print(dict1)