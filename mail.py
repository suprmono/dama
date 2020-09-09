# smtplib 用于邮件的发信动作
import smtplib

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

#### 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = ''
password = ''

#from_addr = input('请输入登录邮箱：')#''
#password = input('请输入邮箱密码：')#''

#### 发信服务器
smtp_server = 'smtp.exmail.qq.com' 

#### 收信方邮箱
'''
to_addrs=[]
while True:
	a = input('请输入收件人邮箱：')
	to_addrs.append(a)
	b = input('是否继续输入，n退出，任意键继续：')
	if b == 'n':
		break
print(to_addrs)
'''

to_addrs = ['635069882@qq.com']
#to_addr = input('请输入收件邮箱：')#'635069882@qq.com'


####邮件头信息
msg = MIMEMultipart() #创建一个MIMEMulipart实例

msg['From'] = Header(from_addr)
msg['To'] = Header(','.join(to_addrs))
msg['Subject'] = Header('python test')

####邮件正文
text = '''这是一段很长很长的文字
		非常非常的长
		超级无敌长
		长~~~~~~~~~~~~~
		'''

html = '''
<p>Dear All:</p>
<p style="text-indent:2em;">大家好！</p>
<p style="text-indent:2em;">CMP最新的程序包：CIS_Beta1.0_2019-11-30version-20200102.zip，已上传到 ：http://www.bsw.com.cn/whb/cis/  ，请大家自行前往下载。</p>
<img src="cid:0">
<p> Chrome 浏览器下载地址：
（64位）http://www.bsw.com.cn/whb/TOOL/chrome_installer_64.exe
（32位）http://www.bsw.com.cn/whb/TOOL/chrome_installer_x86.exe</p>
<p>本次更新，已经完成的需求单共计247单。</br>具体需求单内容，请下载附件中的CMP软件20191130版本升级内容说明_20191230查看。</p>
'''
#msg.attach(MIMEText(text,'plain','utf-8'))
msg.attach(MIMEText(html,'html','utf-8'))

#### 邮件图片附件
img_file  = open('picture.jpg','rb').read()
msg_img = MIMEImage(img_file)
msg_img.add_header('Content-Disposition','attachment', filename = "picture.jpg")
msg_img.add_header('Content-ID', '<0>')
msg.attach(msg_img)

#### 邮件文件附件
txt_file = MIMEText(open('EXCEL.xls','rb').read(),'base64','utf-8')
txt_file["Content-Type"] = 'application/octet-stream'
#txt_file.add_header('Content-Disposition','attachment', filename = ('utf-8','','中文.xls'))
txt_file["Content-Disposition"] = 'attachment; filename = "EXCEL.xls" '
msg.attach(txt_file)



#### 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)

#### 登录发信邮箱
server.login(from_addr,password)

#### 发送邮件
try:
	server.sendmail(from_addr,to_addr,msg.as_string())
	print('恭喜，发送成功')
	
except:
	print('发送失败，请重试')
#### 关闭服务器
server.quit()



