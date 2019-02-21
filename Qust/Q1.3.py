phone=input('请输入你的手机号：')
list= [175,132,182,183,169]
try:
    #确定为由数字组成
    int(phone)
    #判断手机号为11位
    if len(phone) == 11:
        #取出手机号前三位
        head=phone[:3]
        #位标
        flag = False
        # 循环 判断 前三位和list中相等
        for i in list:
            if int(head)==i:
                flag=True
        if flag:
            print('输入正确')
        else:
            print('号段不对')
    else:
        print('手机长度不对')

except:
    print('手机非数字')