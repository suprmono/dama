'''
class total():	
    final_scores = []
    file_lines = []  
    def totalscores(self):
        file = open('scores.txt','r',encoding='utf-8') 
        self.file_lines = file.readlines()
        file.close()
        for i in self.file_lines:			
            data =i.split()    
            sum = 0                    
            for score in data[1:]:     
                sum = sum + int(score)     
            result = data[0]+str(sum)+'\n'    
            self.final_scores.append(result)
        return self.final_scores
			
    def totalscores_write(self):
        winner = open('winner.txt','w',encoding='utf-8') 
        winner.writelines(self.totalscores())
        winner.close()

class order(total):
	dict_scores = {}
	list_scores = []
	def order_txt(self):	
		self.totalscores_write()
		file = open('winner.txt','r',encoding='utf-8')
		file_lines = file.readlines()
		print(file_lines)
		for i in file_lines:  # i是字符串。
			print(i)
			name = i[:-4]  # 取出名字（注：字符串和列表一样，是通过偏移量来获取内部数据。）
			score = int(i[-4:-1])  # 取出成绩
			#print(name)
			#print(score)
			self.dict_scores[score] = name  # 将名字和成绩对应存为字典的键值对(注意：这里的成绩是键)
			self.list_scores.append(score)
		final_scores=[]
		self.list_scores.sort(reverse=True)  # reverse，逆行，所以这时列表降序排列，分数从高到低。
		print(self.list_scores)
		for i in self.list_scores:
			result = self.dict_scores[i] + str(i) + '\n'
			#print(result)
			#print(self.final_scores)
			final_scores.append(result)
		print(final_scores)
		winner_new = open('winner_new.txt','w',encoding='utf-8') 
		winner_new.writelines(final_scores)
		winner_new.close()	

	#print(self.final_scores)  # 最终结果

test = order()
test.order_txt()
'''
# 由于系统原因，这里修改后的test.txt不会即时显示变化，你需要重新打开文件-root下的test.txt。
# 或者在本地新建文件夹，复制test.txt，在本地运行这段代码。
'''
with open ('test.txt','r') as f:
    lines = f.readlines()  # 这时，lines 的数据存放在内存里。
print(lines)  # 将读取到的内容打印出来，发现实际上读到的是带换行符的字符串。
with open('test.txt','w') as new:
    for line in lines:  # 在内存中，对数据进行处理，然后再写到文档里，覆盖之前的内容。
        if line not in ['0\n','1\n']:  # 注意：这里的条件要根据上面打印出的数据写。
            new.write(line)            

# 请你根据学到的新知识，在下面完成对文档“poem1.txt”的修改。
# 你可以处理命名为“poem1”的文档，参考代码会处理“poem1.txt”。
'''

with open ('poem1.txt','r') as f:
	lines =f.readlines()
print(lines)
with open ('test.txt','w') as new:
	for line in lines:
		if line in ['一弦一柱思华年。\n','只是当时已惘然。\n']:
			new.write('__。\n')
		else:
			new.write(line)

			
			
			
			