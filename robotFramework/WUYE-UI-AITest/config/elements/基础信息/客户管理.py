# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index

'''
客户档案页面
'''
客户新建="id=btnAdd"
客户编辑="id=btnEdit"
客户删除="id=btnDelete"
合并重名客户="id=renameCustomerMerge"
客户档案导出Excel="id=btnExport"
客户档案搜索框="id=searchTerm"
客户档案搜索按钮="id=btnFilter"
客户向下展开按钮="xpath=//div[@class='input-group-btn']/button[2]"
客户向上展开按钮="//div[@class='form-horizontal']//button[3]"
高级搜索按钮="id=btnFilterDetail"
高级搜索重置="id=btnReset"
选择管理区="id=RegionId"
管理区数据="xpath=//select[@id='RegionId']/option[last()]"
客户名称="id=Name"
客户档案保存="id=btnSave"
表格中管理区数据="xpath=//tbody/tr[1]/td[4]"
确认删除按钮="xpath=//div[@class='popover-content']/a[1]"
合并同名客户title="xpath=//h4"
关闭合并同名客户="xpath=//div[@class='ant-modal-content']/button"
电话号码="id=Phone"
客户档案列表名称="xpath=//tbody/tr[1]/td[6]"
弹框确定="xpath=//div[@class='modal-footer']/button"

'''
委员会成员
'''
新增成员="xpath=//div[@class='ListButton___2jlS-']/div/div/button"
委员会批量删除="xpath=//div[@class='ListButton___2jlS-']/div/div/span"
委员会选择管理区="xpath=//div[@class='ListButton___2jlS-']/div/div[2]//i"
委员会管理区数据="xpath=//ul[@role='listbox']/li[last()]"
委会会查看="xpath=//tbody/tr[1]/td[10]//a[1]"
委会会编辑="xpath=//tbody/tr[1]/td[10]//a[2]"
委会会删除="xpath=//tbody/tr[1]/td[10]//a[3]"
#委员会新建页面元素
委员会编号="id=number"
委员会管理区="id=organizationItemId"
委员会确定="//div[@class='ant-modal-footer']//button[2]"
委员会取消="//div[@class='ant-modal-footer']//button[1]"


