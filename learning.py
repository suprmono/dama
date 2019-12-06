'''
print('成绩提升计算器')
name = input('请输入你的姓名:',)
lastYearStr = input('请输入去年成绩:',)
A = int(A)
currYear = input('请输入今年成绩:',)
B = int(B)

r = (B-A)/A
print('你好,%s!,去年考了%d分,今年考了%d分,成绩提升了%.1f%%。'%(name,A,B,r*100))
 
print('你好,{0}!,去年考了{1}分,今年考了{2}分,成绩提升了{3:.1%}。'.format(name,A,B,r))

if r >=0.2 and B >=80:
	print('恭喜！进步非常大')
else:
	print('仍需继续努力！')
'''
	
'''	if else/elif 条件判断
height = 1.75
weight = 80.5

bmi=weight/(height**2)

if bmi < 18.5:
	print('过轻')
elif 18.5<bmi<25:
	print('体重正常')
elif 25<bmi<28:
	print('体重过重')
elif 28<bmi<32:
	print('体重肥胖')
elif bmi>32:
	print('体重严重肥胖')
'''

''' for in 循环
sum = 0
for x in  range(101):
	sum = sum + x
print(sum)
'''
'''
L=['Bart','Lisa','Adam']
for name in range(3):
	print('hello,%s!'%L[name])
'''


'''  while循环
n = 100
sum = 0
while n > 0:
	sum=sum+n
	n=n-1
	
print(sum)
'''


''' break 中断循环
n=1
while n <=100:
	if n> 10:
		break
	print(n)
	n = n + 1
print('END')
'''

''' dict字典 a={key:value}
a={'Michael':75,'Bob':80,'Tracy':85}
b=('Michael','Bob','Tracy')
for name in b:
	print(a[name])
'''

''' 在list中查找sarah   list(可变):L=[]  tuple(不可变)=()
L = ['Michael','Bob','Tracy','Tom','Sarah','Jack']

n = 0
while n <= len(L)-1:
	
	if L[n]=='Sarah':
		print(L[n])
		print('已找到Sarah')
		break
	n = n+1
'''


'''创建函数'''
'''
import math 
def quadratic(a,b,c):
	t = b*b-4*a*c
	if t >= 0:
		x1 = (-b + math.sqrt(t))/(2*a)
		x2 = (-b - math.sqrt(t))/(2*a)
		return x1,x2
	
	else:
		print('方程无实数根')
print('quadratic(2,3,1)=',quadratic(2,3,1))
if quadratic(2,3,1) != (-0.5,-1.0):
	print('测试失败')
else:
	print('测试成功') 
'''

import random
import time

###提示语部分
print('你好，我是机器人小埋，我们来玩个猜年龄的小游戏吧～(◆◡◆)')
time.sleep(2)

print('''
=============================
   干物妹！うまるちゃんの年齢
=============================
''')
time.sleep(1)


print('小埋的真实年龄在1到10之间哦～')
time.sleep(1)


print('不过，你只有5次机会哦～')
time.sleep(1)


print('下面，请输入小埋的年龄吧：')


#从0至10产生一个随机整数，并赋值给变量age
age = random.randint(1,10)


#设置次数
for guess in range(1,6):
   
   #输入玩家猜测的年龄
    choice=int(input())
    
    #判读玩家输入的年龄是否等于正确的年龄
    if choice<age:
        print('小埋的提示：你猜小了（；´д｀）ゞ。。。。')
                
    elif choice>age:
        print('小埋的提示：乃猜大了惹(＞﹏＜)～～')
            
    else: 
        print('猜了'+str(guess)+'次，你就猜对惹～hiu(^_^A;)～～～')
        break   
                
#判断猜测次数 
if choice  == age:
    print('搜噶～那么小埋下线了～拜拜～（￣︶￣）↗')
    
else:
    print('哎呀～你还是木有猜对啊～但是你只有5次机会诶～怎么办啊～')
    print('那好吧～心软的小埋只好告诉你，我才'+str(age)+'岁哦～')
	
	


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

