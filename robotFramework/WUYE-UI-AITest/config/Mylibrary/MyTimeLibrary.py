import time
import re

class MyString():
	def __init__(self):
		pass
	def Time_Random(self,str):
		t=time.gmtime()
		z=time.strftime("%Y%m%d%H%M%S",t)
		return (str+z)
	'''
     获取cookiename=nova_pms_auth_Default，保存cookie到文件中cookies.txt
    '''
	def save_Cookis(self,cookies):
		with open('D:/wuye/robotFramework-WuYe/robotFramework/WUYE-UI-AITest/cookies.txt', 'w') as fp:
			fp.write(cookies)	

					
	'''
          从文件中读取cookie
	'''
	def set_Cookie(self):
		with open("D:/wuye/robotFramework-WuYe/robotFramework/WUYE-UI-AITest/cookies.txt", 'r') as fp:
			# s = fp.read()
			cookies = fp.read()
			s=re.search(r'nova_pms_auth_Default=(.*);',cookies)
			cookie=s.group(1)
			#cookie=cookie.split("=")[1]
			print(cookie)
			return cookie


# if __name__=="__main__":
# 	s=MyString()
# 	s.set_Cookie()


