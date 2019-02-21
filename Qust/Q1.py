phone = input('请输入手机号：')
list = [185,137,172,175,183,151]

try:
    #判断是否是纯数字
    int(phone)
    # 判断长度是否为11位
    if(len(phone)==11):
        ##截取前三位
        head = phone[0:3]
        ##位标
        bool=False
        # 利用循环和判断来比较list和head的值 是否存在
        for i in list:
            if(int(head)==i):
                #存在则 布尔类型则刚才true
                bool=True
                break
            # bool为true的时候为正确的手机号
        if(bool):
            print("有效手机号")
        else:
            print('无效手机号')
    else:
        print('输入的不是有效的手机号')
except:
    print('输入的不是有效手机号')