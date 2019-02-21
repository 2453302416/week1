phone = input('请输入你的手机号：')
list =[152,132,175,183,182,177]
try:
    #判断是否是数字
    int(phone)
    if len(phone)==11:
        head=phone[:3]
        flag=False
        for i in list:
            if int(head)==i:
                flag=True
        if flag:
            print('输入正确')
        else:
            print('字段不对')
    else:
        print('手机号码长度不够')
except:
    print('手机号为非数字')