import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
name = input('请输入电影名称:')
gbkmovie = name.encode('gbk')
url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+quote(gbkmovie)

try:
    res = requests.get(url)
    res.encoding ='gbk'
	#定义res的编码类型为gbk
    soup = BeautifulSoup(res.text,'html.parser')

    film_url = soup.find('tr',height='24').find('a')['href']

    down_url='https://www.ygdy8.com'
    film_res = requests.get(down_url+film_url)
    film_res.encoding ='gbk'
    film_soup = BeautifulSoup(film_res.text,'html.parser')

    download_url=film_soup.find('div',id='Zoom').find('td',style='WORD-WRAP: break-word').find('a')['href']

    print(download_url)

except:
    print('没有找到这部电影呢')