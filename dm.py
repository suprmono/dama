from selenium import webdriver
import pickle
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class concert():
	def __init__(self):
		self.damai_url='https://www.damai.cn'

		self.login_url='https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'#登录地址

		self.target_url='https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.5d8228dfOM2jJu&id=611160757855&clicktitle=%E5%91%A8%E6%9D%B0%E4%BC%A6%E3%80%90%E5%98%89%E5%B9%B4%E5%8D%8E%E3%80%91%E4%B8%96%E7%95%8C%E5%B7%A1%E5%9B%9E%E6%BC%94%E5%94%B1%E4%BC%9A%20%E5%A4%A9%E6%B4%A5%E7%AB%99'#购买页面地址

		self.pricelist = ['\'500元\'','\'700元\'','\'900元\'']#需要购买的票价，按优先级

		self.s_times=1
		
		self.again = True
	
	def set_cookie(self):
		cookies = pickle.load(open("cookies.pkl", "rb"))#载入cookie
		for cookie in cookies:
			cookie_dict = {
			'domain':'.damai.cn',
			'name': cookie.get('name'),
			'value': cookie.get('value'),
			"expires": "",
			'path': '/',
			'httpOnly': False,
			'HostOnly': False,
			'Secure': False}
			self.driver.add_cookie(cookie_dict)
					
	def get_cookie(self):#先扫码登录获取cookie并保存
		self.driver.get(self.damai_url)
		print("###请点击登录###")
		time.sleep(2)
		while self.driver.title == '大麦登录':
			print("###请扫码登录###")
		locator = (By.XPATH,"//div[@class='span-box-header name-user show']")
		element = WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(locator,'spermono'))
		print('###登录成功###')
		pickle.dump(self.driver.get_cookies(),open('cookies.pkl','wb'))
		print('###cookie保存成功###')
	
	def countdown(self):
		try:
			while True:
				
				d = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='天']/../span[@class='digit']").text
				h = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='时']/../span[@class='digit']").text
				m = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='分']/../span[@class='digit']").text
				s = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='秒']/../span[@class='digit']").text
				print('还有%s天%s时%s分%s秒' % (d,h,m,s))
				time.sleep(1)
				if d == '0' and h == '0' and m == '0' and s == '0':
					break
				'''
				else:			
					self.driver.refresh()
					time.sleep(2)
				'''
		except:
			print('###该场次已经开售了###')
	
	def choose_ticket(self):
		
		#scene = self.driver.find_element_by_xpath("//span[contain(text(),'2020-04-11')]")
		#time.sleep(3)
		while self.again:
			
			for i in self.pricelist:
				element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,'buybtn')))
				try:
					ticket_path=self.driver.find_element_by_xpath("//div[contains(text(),"+i+")]/../span")#使用xpath通过父级查找子级的方法，用模糊票价抓取对应'缺货登记'状态
					#ticket_path=self.driver.findelement_by_xpath("//div[(text()="+i+")]")#票价精确查找
					if ticket_path.text == '缺货登记':
						print('###'+i+'的票没有了'+'###')
						self.driver.refresh()
						
				except:#找不到'缺货登记'的元素会报错，则执行有余票的逻辑
										
					print('###现在购买的是'+i+'的票###')
					ticket_path=self.driver.find_element_by_xpath("//div[contains(text(),"+i+")]")
					ticket_path.click()
					limit = self.driver.find_element_by_xpath("//span[@class='number_right_limit']")
					if limit.text != '每笔订单限购1张':				
						num = self.driver.find_element_by_class_name('cafe-c-input-number-handler-up')
						num.click()#如果买两张票，就点击一下，买一张不需要执行.有限制每笔订单限购一张则不点击
					buybtn = self.driver.find_element_by_xpath("//div[@class='buybtn']")
					buybtn.click()#立即购买/立即预订(备注：此处点击购买按钮之后有可能弹出提示框，仍需测试)
					time.sleep(1)
					try:					
						buyer_list = self.driver.find_element_by_xpath("//span[@class='next-checkbox-label']")
						print('进入确认订单界面')
						self.check_order()
						self.again = False
						break
					except:
						print('无法进入确认订单界面，再次刷新选票')
						self.driver.get(self.target_url)
						self.driver.refresh()
					
	def check_order(self):
		#time.sleep(3)
		#element1 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'next-checkbox-label')))#等待观演人元素加载
		#element2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='submit-wrapper']/button[@type='button']")))#等待提交订单按钮加载
		
		retry_time = 1		
		#'''1、
		while retry_time <= 10:
			buyer_list = self.driver.find_elements_by_xpath("//span[@class='next-checkbox-label']")
			people = int(self.driver.find_element_by_xpath("//div[@class='ticket-buyer-title']/span/em").text)
			for i in range(people):
				buyer_list[i].click()
			subbtn = self.driver.find_element_by_xpath("//div[@class='submit-wrapper']/button[@type='button']")
			subbtn.click()
			time.sleep(2)
			alert_xpath="//div[@class='next-feedback-title']"#提示框的xpath
			if self.isElementExist(alert_xpath):#如果提示框存在，则刷新，重新点击观影人和提交订单。
				tips = self.driver.find_element_by_xpath(alert_xpath)
				print(tips.text)#打印提示
				self.driver.refresh()
				retry_time += 1
			else:
				break
		
		if retry_time > 10:#刷新提交次数为10次，超过10次则重新选票
			self.s_times +=1
			self.driver.get(self.target_url)
			self.again = True
			self.choose_ticket()
		#'''
		'''
		buyer_list = self.driver.find_elements_by_xpath("//span[@class='next-checkbox-label']")
		people = int(self.driver.find_element_by_xpath("//div[@class='ticket-buyer-title']/span/em").text)
		for i in range(people):
				buyer_list[i].click()
		subbtn = self.driver.find_element_by_xpath("//div[@class='submit-wrapper']/button[@type='button']")
		subbtn.click()
		alert_xpath="//div[@class='next-feedback-title']"#提示框的xpath
		if self.isElementExist(alert_xpath):
			driver.find_element_by_xpath("//div[@id='dialog-footer-2']/button").click()
			self.again = True
			self.choose_ticket()
		'''	
		try:
			element = WebDriverWait(self.driver, 5).until(EC.title_contains('支付宝'))#判断是否跳转到支付宝支付页面，如果不是，重新抢票
			print('###已经抢到票，可以支付宝扫码支付了###')
			print('经过%s轮努力，终于抢到票了'% self.s_times)
		except:
			driver.get_screenshot_as_file("Error.jpg")
			self.s_times +=1
			self.driver.get(self.target_url)
			self.again = True
			self.choose_ticket()
		
	def isElementExist(self,element):
		flag = True
		driver = self.driver
		try:
			driver.find_element_by_xpath(element)
			return flag
		except:
			flag=False
			return flag
	
	def login(self):
		if not os.path.exists('cookies.pkl'):
			self.get_cookie()
		else:
			self.driver.get(self.damai_url)
			time.sleep(3)
			self.set_cookie()


	
	def main(self):
		options=webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		
		print('###打开浏览器，进入大麦网###')		
		self.driver = webdriver.Chrome(options=options)
		self.login()#登录
		self.driver.refresh()#载入cookie之后刷新界面
		#time.sleep(3)
		locator = (By.XPATH,"//div[@class='span-box-header name-user show']")
		element = WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(locator,'spermono'))
		self.driver.get(self.target_url)#直接跳转到购票界面
		self.countdown()
		self.choose_ticket()
		
		
if __name__ == '__main__':
	super = concert()
	super.main()