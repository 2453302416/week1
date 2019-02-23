import os
import shutil
#创建文件夹
#os.mkdir('Spython')
import  random
f = open('py.txt','w')
f1= open('py.txt','r')


for i in range(30):
    sum= random.choice(range(20))
    f.write(str(sum))

f.close()
shutil.copy('py.txt','py22.txt')
print(f1.read(20))



