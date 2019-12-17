# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index


'''
下面模块通用的定位方式
'''
搜索框="//input[@placeholder='搜索...']"
搜索按钮="//span[@class='ant-input-suffix']/i"
管理区="id=regionId"
管理区数据="//ul[@role='listbox']/li[1]"
'''
巡更点
'''
新建巡更点="//button/span[text()='新建巡更点']"
导入Excel="//button/span[text()='导入Excel']"
下载模板="//button/span[text()='下载模板']"
编辑巡更点="//tbody/tr[1]/td[7]//a[1]"
删除巡更点="//tbody/tr[1]/td[7]//a[2]"
作废巡更点="//tbody/tr[1]/td[7]//a[3]"
查看二维码巡更点="//tbody/tr[1]/td[7]//a[4]"
巡更点名称="id=name"
巡更点编码="id=number"
检查要点="id=checkList"
