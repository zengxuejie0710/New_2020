# Author xuejie zeng
# encoding utf-8

#注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。

def test_case(cmdoption):

    myenv,datas = cmdoption

    print(f"环境:{myenv},数据:{datas}")
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = 'http://'+str(ip)+str(port)
    print(url)