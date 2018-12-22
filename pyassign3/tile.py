#Assign#；放瓷砖

#姓名：崔若瑶
#学号：1800011755
#院系：化学与分子工程学院
#邮箱：1800011755@pku.edu.cn

import turtle
import time
def find_blank(wall):
	#找到下一个没铺的位置
	ii=0
	jj=0
	for q in range(len(wall)): 
		for p in range(len(wall[q])):
			if wall[q][p] ==0:
				ii =q
				jj =p
				return ii,jj

def conflict_judge(wall):
	#检查墙面是否有已经铺上砖的地方又铺上了砖
	ccc=True
	for p in range (b):
		for q in range (a):
			if wall[p][q]==2:
				ccc=False
				
			return ccc


def hengpu(wall,i_,j_):
	#横着铺一块砖 改变墙的值 并且返回砖的值
	brick=[]
	for x in range(i_,i_+d):
		for y in range(j_,j_+c):
			wall[x][y]=wall[x][y]+1
			kkk=x*a+y
			brick.append(kkk)
	return wall,brick


def hengchai(wall,i,j):
	#将刚铺的横着的砖拆下来
	for x in range(i,i+d):
		for y in range(j,j+c):
			wall[x][y]-=1
	return wall


def hengpu_judge(wall,i,j):
	'''检查是否能横着铺一块砖
	分两种情况 格子不够和要铺砖的地方已经有砖了
	由于横铺改变了墙的状态 所以要把砖拆下来'''

	if j+c > a or i+d>b :
		return False
	else:
		wallll=hengpu(wall,i,j)[0]
		try:
			return conflict_judge(wallll)
		finally:
			hengchai(wallll,i,j)


def shupu(wall,i_,j_):
	#与横铺作用相同 竖着铺一块砖
	brick=[]
	for x in range(i_,i_+c):
		for y in range(j_,j_+d):
			wall[x][y]=1
			kkk=x*a+y
			brick.append(kkk)
	return wall,brick


def shupu_judge(wall,i,j):
	'''判断能否竖着铺一块砖 
	由于改变了墙的状态 需要把砖拆下来'''
	if j+d > a or i+c > b :
		return False
	else:
		wallll=shupu(wall,i,j)[0]
		try:
			return conflict_judge(wallll)
		finally:
			shuchai(wallll,i,j)


def shuchai(wall,i_,j_):
	#把刚铺的横着的砖拆下来
	for x in range(i_,i_+c):
		for y in range(j_,j_+d):
			wall[x][y]-=1
	return wall


def puzhuan(ans,alls):
	global qiang
	if len(ans)==kk:
		answ1=ans.copy()  #做了一次复制 每次递归ans会发生变化

		alls.append(answ1)		#alls中是所有的解法 
	else:
		m=find_blank(qiang)[0]
		n=find_blank(qiang)[1]
		if hengpu_judge(qiang,m,n):
			
			qiang=hengpu(qiang,m,n)[0]
			bbb=hengpu(qiang,m,n)[1]
			ans.append(bbb)

			qiang=hengchai(qiang,m,n)

			puzhuan(ans,alls)
			qiang=hengchai(qiang,m,n)

			ans.remove(bbb)


		if shupu_judge(qiang,m,n):

			qiang=shupu(qiang,m,n)[0]
			ans.append(shupu(qiang,m,n)[1])
			puzhuan(ans,alls)
			qiang=shuchai(qiang,m,n)
			ans.pop()

def dereplication(alls):
	#如果瓷砖为正方形，横着铺和竖着铺一样，会有重复解法
	final_allanswer=[]
	for i in alls:
		if sorted(i) not in final_allanswer:
			final_allanswer.append(i)
	return final_allanswer

def view(one_idea): 
	#其中一种铺法进行可视化操作
	turtle.speed(80)
	turtle.screensize(600,600)
	allcolor=['yellow','hotpink','orange','red','write','purple','brown','green',
			'blue','gray']

	for i in sorted(one_idea):
		mm=sorted(one_idea).index(i)
		col=allcolor[mm%10] #为标记不同的砖 选取不同颜色
		for k in i:
			g=k//a
			h=k%a
			turtle.penup()
			turtle.goto(-350+70*h,250-70*g)
			turtle.pendown()
			turtle.pencolor('black')
			turtle.begin_fill()
			turtle.fillcolor(col)
			for i in range(4):
				turtle.forward(70)
				turtle.left(90)
			turtle.end_fill()
			turtle.write(k,100,font='Arial')
	time.sleep(20)  #画的时间太快啦 没时间看


def main():
	global qiang
	global a
	global b
	global c
	global d
	global kk
	a=int(input('请输入墙面长度：'))
	b=int(input('请输入墙面宽度：'))
	c=int(input('请输入长方形瓷砖长度：'))
	d=int(input('请输入长方形瓷砖宽度：'))
	qiang=[[0]*a for i in range (b)]

    
	if (a*b)%(c*d)==0:
		kk=(a*b)//(c*d)
		answ=[]
		alls=[]
		puzhuan(answ,alls)
		 #若瓷砖为正方形瓷砖 横着铺和竖着铺一样 会有重复结果
		num=len( dereplication(alls) )
		print("共有%d种铺法！" %( num ) )
		print("铺法如下：")
		for h in dereplication(alls):
			print(h)
		pufa=int(input('请输入0～%p中的一个数字，选择一种铺法进行可视化' %(num-1) ) ) 
		view(dereplication(alls)[pufa])
	else :
		print("不能用这种瓷砖铺满墙面！")

if __name__=='__main__':
	main()


