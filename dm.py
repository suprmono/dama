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

		self.login_url='https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'

		self.target_url='https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_6.1d3c23e1LaK3jr&id=610050554319'#购买页面地址

		self.pricelist = ['\'180元\'','\'380元\'','\'680元\'']#需要购买的票价，按优先级

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
					
	def get_cookie(self):
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
		
	def choose_ticket(self):
		element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,'buybtn')))
		#time.sleep(3)
		while self.again:					
			for i in self.pricelist:		
				try:
					ticket_path=self.driver.find_element_by_xpath("//div[contains(text(),"+i+")]/../span")#使用xpath通过父级查找子级的方法，用模糊票价抓取对应'缺货登记'状态
					#ticket_path=self.driver.findelement_by_xpath("//div[(text()="+i+")]")#票价精确查找
					if ticket_path.text == '缺货登记':
						print('###'+i+'的票没有了'+'###')
						
				except:
					self.again = False					
					print('###现在购买的是'+i+'的票###')
					ticket_path=self.driver.find_element_by_xpath("//div[contains(text(),"+i+")]")
					ticket_path.click()
					num = self.driver.find_element_by_xpath("//a[@class='cafe-c-input-number-handler cafe-c-input-number-handler-up']")
					num.click()#如果买两张票，就点击一下，买一张不需要执行
					buybtn = self.driver.find_element_by_xpath("//div[@class='buybtn']")
					buybtn.click()
					self.check_order()
					break
			

	def check_order(self):
		#time.sleep(3)
		element1 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,'next-checkbox-label')))#
		element2 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,"//div[@class='submit-wrapper']/button[@type='button']")))
		buyer_list = self.driver.find_elements_by_xpath("//span[@class='next-checkbox-label']")
		people = int(self.driver.find_element_by_xpath("//div[@class='ticket-buyer-title']/span/em").text)
		for i in range(people):
			buyer_list[i].click()
		subbtn = self.driver.find_element_by_xpath("//div[@class='submit-wrapper']/button[@type='button']")
		#subbtn.click()
		
		try:
			#element = WebDriverWait(self.driver, 5).until(EC.title_contains('支付宝'))#判断是否跳转到支付宝支付页面，如果不是，重新抢票
			print('###已经抢到票，可以支付宝扫码支付了###')
			print('经过%s轮努力，终于抢到票了'% self.s_times)
		except:
			self.s_times +=1
			self.driver.get(self.target_url)
			self.choose_ticket()
		
			
	def login(self):
		if not os.path.exists('cookies.pkl'):
			self.get_cookie()
		else:
			self.driver.get(self.damai_url)
			time.sleep(3)
			self.set_cookie()

	def countdown(self):
		try:
			while True:
				d = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='天']/../span[@class='digit']").text
				h = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='时']/../span[@class='digit']").text
				m = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='分']/../span[@class='digit']").text
				s = self.driver.find_element_by_xpath("//div[@class='item']/span[text()='秒']/../span[@class='digit']").text
				if d == '0' and h == '0' and m == '0' and s == '0':
					break
				else:
					self.driver.refresh()
					time.sleep(2)
		except:
			print('###该场次已经开售了###')
	
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