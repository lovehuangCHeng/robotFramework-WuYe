# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
'''
数据库配置连接信息
sqlconfig="DRIVER='{SQL Server}',SERVER='WIN-E4I1KQ1IN70',DATABASE='pms_hualian_master_preview',UID='sa',PWD='Sa123456'"
'''	

'''
查询管理区数据
'''
guanliqu="select top 1 Name from OrganizationItem where Discriminator='管理区';"
guanliquID="select top 1 ID from OrganizationItem where Discriminator='管理区';"
'''
查询楼宇数据
'''
louyu="select Name,code from OrganizationItem where Discriminator='楼宇';"
#管理区下楼宇id
GLQLYID="select top 1 ID from OrganizationItem where Discriminator='楼宇' and parentid in(select top 1 ID from OrganizationItem where Discriminator='管理区')"
#查询有账单房间的管理区ID,楼宇ID，房间ID
BillOBHid="select top 1 o.RegionId,o.BuildingId,o.id from OrganizationItem o,bill b where o.id=b.OrganizationItemID"
#查询有账单房间的楼宇名称和管理区ID
BillBNameOid="select name,regionID from OrganizationItem where id=(select top 1 o.BuildingId from OrganizationItem o,bill b where o.id=b.OrganizationItemID and o.BuildingId is not null)"
'''
查询停车场数据
'''
tingchechang="select Name from OrganizationItem where Discriminator='停车场';"
'''
获取房间ID，用户名称，房间代码，房间存在账单和业主的情况。
'''
getcustomerbillcode="SELECT top 1 o.Id,c.Name,o.code FROM Bill b,OrganizationItem o,Customer c where Status=1 AND b.OrganizationItemId = o.Id and c.Id=o.HouseOwnerId and b.IsDelete=0"
#查询已经绑定了收费标准的房间名称\ID
BZFJCODEID="select top 1 code,id from OrganizationItem where ID IN(SELECT  OrganizationItemId from ChargeItemSetting)"

'''
获取有业主的房间代码。
'''
gethouseCode="select top 1 code from  OrganizationItem where HouseOwnerId is not null  AND RegionId =(select top 1 Id from OrganizationItem  where Discriminator='管理区')"
'''
获取当前月未抄表的仪表ID、仪表名称、仪表绑定房间名称
'''
GetHouseMeterID="select  top 1 HouseMeterReading.housemeterid from HouseMeter  left join HouseMeterReading on HouseMeter.ID=HouseMeterReading.ID where HouseMeter.isAvailable='1' AND HouseMeterReading.housemeterid is not null AND HouseMeter.LastReadDate < CONVERT(varchar(7), getdate() , 120) + '-1'"
GetHouseMeterName="select  top 1 HouseMeter.name from HouseMeter  left join HouseMeterReading on HouseMeter.ID=HouseMeterReading.ID where HouseMeter.isAvailable='1' AND HouseMeterReading.housemeterid is not null AND HouseMeter.LastReadDate < CONVERT(varchar(7), getdate() , 120) + '-1'"
GetMeterHouseCode="select top 1 Code FROM OrganizationItem WHERE id in (SELECT top 50 HouseMeter.HouseId from HouseMeter  left join HouseMeterReading on HouseMeter.ID=HouseMeterReading.ID where HouseMeter.isAvailable='1' AND HouseMeterReading.housemeterid is not null AND HouseMeter.LastReadDate < CONVERT(varchar(7), getdate() , 120) + '-1')"

'''
获取已出账单房间、账单应收日期
'''
#获取已出账单且已出账单没有交费的房间code\账单应收日期
GetBillYCodeAndDay="select  top 1  o.code,b.ShouldChargeDate from OrganizationItem o,PaymentTicketOrganizationItem p,bill b,PaymentTicket t where b.PaidAmount = 0 and b.status =1 and b.IsDelete=0 and b.OrganizationItemId is not null and o.id=b.OrganizationItemId and p.OrganizationItemId=o.Id and p.PaymentTicketId=t.Id and t.Status=1 "
#获取已出账单且已出账单且部分缴费的房间code\账单应收日期
##部分缴费且打印票据（未扎帐）
GetBillNCodeAndDayST2="select  top 1  o.code,b.ShouldChargeDate from OrganizationItem o,PaymentTicketOrganizationItem p,bill b,PaymentTicket t,Payment pt  where b.PaidAmount <> 0 and b.status =1 and b.IsDelete=0 and b.OrganizationItemId is not null and o.id=b.OrganizationItemId and p.OrganizationItemId=o.Id and p.PaymentTicketId=t.Id and t.Status=2 and pt.Status=0  and pt.CustomerId=b.CustomerId and pt.PaidMoney=b.PaidAmount"
##部分缴费且未打印票据（未扎帐）
GetBillNCodeAndDayST3="select  top 1 o.code,b.ShouldChargeDate from OrganizationItem o,PaymentTicketOrganizationItem p,bill b,PaymentTicket t,Payment pt  where b.PaidAmount <> 0 and b.status =1 and b.IsDelete=0 and b.OrganizationItemId is not null and o.id=b.OrganizationItemId and p.OrganizationItemId=o.Id and p.PaymentTicketId=t.Id and t.Status=1 and pt.Status=0  and pt.CustomerId=b.CustomerId and pt.PaidMoney=b.PaidAmount "
###部分缴费且未打印票据且(已扎帐)
GetBillNCodeAndDayST4="select  top 1  o.code,b.ShouldChargeDate from OrganizationItem o,PaymentTicketOrganizationItem p,bill b,PaymentTicket t,Payment pt where b.PaidAmount <> 0 and b.status =1 and b.IsDelete=0 and b.OrganizationItemId is not null and o.id=b.OrganizationItemId and p.OrganizationItemId=o.Id and p.PaymentTicketId=t.Id and t.Status=1 and pt.Status=2  and pt.CustomerId=b.CustomerId and pt.PaidMoney=b.PaidAmount"
##获取未退款票据号
GetNoRefunTID="select top 1 pt.TicketNumber from PaymentTicket pt,RefundTicket rt where pt.id<>rt.PaymentTicketId"

'''
获取已出账单房间、账单应收日期
'''
#获取权限为adminnistrator的账号数据