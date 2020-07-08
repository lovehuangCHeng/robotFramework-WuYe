baseURL="http://10.10.120.171:8082"
userName="testing"
passWord="123456"
connectDataBase="DRIVER='{SQL Server}',SERVER='WIN-E4I1KQ1IN70',DATABASE='pms_xinye',UID='sa',PWD='Sa123456'"
'''
登录接口
'''
login=baseURL+"/Login?ReturnUrl=%2F"
'''
收费模块
'''
#预存款
yuCun_getCustomerList=baseURL+"/Nova.Pms.PropertyManagementSystem/Customer/CustomerList" #获取客户列表
yuCun_getCurrentHouseId=baseURL+"/Nova.Pms.PropertyManagementSystem/DropdownList/GetHouseByCustomerId" #获取选择的客户房间列表
yuCun_getCurrentHouseArea=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/GetHouseAreaByHouseId" #获取选择的房间面积
yuCun_yujiao=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/CreatePreview"#预缴费用查看明细页面
yuCun_yujiaoRequement=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/Create"#预缴费用确认收费
yuCun_list=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/List"#列表数据
yuCun_chongDi=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/PayBillPostPreview"#冲抵欠费
yuCun_chongDiRequment=baseURL+"/Nova.Pms.PropertyManagementSystem/ChargeFeesWizard/AdvancePaymentPost"#冲抵欠费确认
yuCun_heXiaotiles=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/ViewBillDetail/50" #查看核销明细
yuCun_heXiaotiles=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/GetPrintTicket" #批量打印票据
yuCun_heXiaotiles=baseURL+"/Nova.Pms.PropertyManagementSystem/CustomerAccount/BatchPrintTicket" #批量打印确认

#前台收费

#经营性收费

#交款申请

#打印催费单

#收费历史记录

#零头账户

#基础信息
souyemeaue="/api/DynamicMenu/GetMenuWuYe"
KEHU_list="/api/v1.0/PROP/Customer/List"

