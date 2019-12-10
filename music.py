
import requests
# 引用requests库
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 调用get方法，下载这个字典
json_music = res_music.json()
# 使用json()方法，将response对象，转为列表/字典
list_music = json_music['data']['song']['list']
# 一层一层地取字典，获取歌单列表

#print(list_music)

for music in list_music:
# list_music是一个列表，music是它里面的元素
    print(music['name'])
    print('歌曲链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html')


'''
import json
# 引入json模块
a = [1,2,3,4]
# 创建一个列表a。
b = json.dumps(a)
# 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b。
print(b)
# 打印b。
print(type(b))
# 打印b的数据类型。
c = json.loads(b)
# 使用loads()函数，将json格式的字符串b转为列表，赋值给c。
print(c)
# 打印c。
print(type(c)) 
# 打印c的数据类型。
'''