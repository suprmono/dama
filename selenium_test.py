from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://kfb.bg114.cn')

#使用ID定位
username = find_element_by_id('id_username')

#输入事件send_keys
username.send_keys('123')

#清除事件clear
username.clear()
username.send_keys('zjk')

password = driver.find_element_by_id('id_password')
password.send_keys('123456')

#使用xpath定位登录按钮
btn = driver.find_element_by_xpath("//input[@type='submit' and @value='登录']")
btn.click()

#使用link text定位
status = driver.find_element_by_link_text('12. 查询需求单状态')
status.click()

filter = driver.find_element_by_xpath("//div[@id='changelist-filter']/h2[@style='cursor: pointer;']")
fileter.click()

version = driver.find_element_by_link_text('CMP/CMP2019-11-30')
version.click()