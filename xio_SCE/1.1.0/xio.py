#coding = utf-8
'''设置'''
import random
import time 

#初始化游戏
attack_c = 0
defence_c = 0
attack_u = 0
defence_u = 0	
xios = [0,0]

#设定电脑初始可用招式
usable_a = ['摸摸']
usable_d = ['地波','天波']
state = ['usable_a','usable_d','xio']

'''组件:方法'''
#招式(电脑)
def xio_c():
	print('电脑:xio')
	global defence_c, xios
	defence_c = 1
	xios[0] = xios[0]+1	
def dibo_c():
	global defence_c, xios
	defence_c = 10
	print('电脑:地波')
def tianbo_c():
	global defence_c, xios
	defence_c = 10
	print('电脑:天波')
def chaofang_c():
	global defence_c, xios
	defence_c = 90
	xios[0] = xios[0]-1
	print('电脑:超防')
def leiba_c():
	global attack_c, xios
	attack_c = 3
	xios[0] = xios[0]-0.3
	print('电脑:雷扒')
def momo_c():
	global attack_c, xios
	attack_c = 5
	xios[0] = xios[0]-1
	print('电脑:摸摸')
def sankan_c():
	global attack_c, xios
	attack_c = 30
	xios[0] = xios[0]-3
	print('电脑:三砍')
def wuhe_c():
	global attack_c, xios
	attack_c = 50
	xios[0] = xios[0]-5
	print('电脑:五合体')
def huhe_c():
	global attack_c, xios
	attack_c = 100
	xios[0] = xios[0]-10
	print('电脑:虎合体')
#招式(玩家)
def xio_u():
	global defence_u, xios
	defence_u = 1
	xios[1] = xios[1]+1
def dibo_u():
	global defence_u, xios
	defence_u = 10
def tianbo_u():
	global defence_u, xios
	defence_u = 10
def chaofang_u():
	global defence_u, xios
	defence_u = 90
	xios[1] = xios[1]-1
def leiba_u():
	global attack_u, xios
	attack_u = 3
	xios[1] =  xios[1] - 1/3
def momo_u():
	global attack_u, xios
	attack_u = 5
	xios[1] = xios[1]-1
def sankan_u():
	global attack_u, xios
	attack_u = 30
	xios[1] = xios[1]-3
def wuhe_u():
	global attack_u, xios
	attack_u = 50
	xios[1] = xios[1]-5
def huhe_u():
	global attack_u, xios
	attack_u = 100
	xios[1] = xios[1]-10

def cpu():
	#控制不爆死
	global usable_a, usable_d, attack_c, defence_c, state
	if xios[0] < 0.3:
		usable_a = []
		usable_d = ['地波','天波']
	elif xios[0] < 1:
		usable_a = ['雷扒']
		usable_d = ['地波','天波']
	elif xios[0] < 3:
		usable_a = ['摸摸','雷扒']
		usable_d = ['地波','天波','超防']
	elif xios[0] < 5:
		usable_a = ['摸摸','雷扒','三砍']
		usable_d = ['地波','天波','超防']
	elif xios[0] < 10:
		usable_a = ['摸摸','雷扒','三砍','五合体']
		usable_d = ['地波','天波','超防']	
	else:
		usable_a = ['摸摸','雷扒','三砍','五合体','虎合体']
		usable_d = ['地波','天波','超防']
	#出招式
	go = random.choice(state)
	if go == 'usable_a' and 'usable_a' != []:
		get = random.choice(usable_a)
		if get == '雷扒':
			leiba_c()
		elif get == '摸摸':
			momo_c()
		elif get == '三砍':
			sankan_c()
		elif get == '五合体':
			wuhe_c()
		elif get == '虎合体':
			huhe_c()
	elif go == 'usable_d':
		get = random.choice(usable_d)	
		if get == '天波':
			tianbo_c()
		if get == '地波':
			dibo_c()
		if get == '超防':
			chaofang_c()
	elif go == 'xio':
		xio_c()

def turn():
	global attack_c, attack_u, defence_c, defence_u
	#接受用户输入
	usr = input(str('你：'))
	#写入数值
	if usr == 'xio':
		xio_u()
	elif usr == '摸摸':
		momo_u()
	elif usr == '三砍':
		sankan_u()
	elif usr == '雷扒':
		leiba_u()
	elif usr == '五合体':
		wuhe_u()
	elif usr == '虎合体':
		huhe_u()
	elif usr == '地波':
		dibo_u()
	elif usr == '天波':
		tianbo_u()
	elif usr == '超防':
		chaofang_u()
	#调用电脑给出招式
	cpu()	
	#判断
	if xios[1] < 0:
		print('你爆死')
		print(xios)
	elif attack_u > attack_c and attack_c != 0  or attack_u > defence_c and defence_c != 0:
		print('你赢了')
	elif attack_c > attack_u and attack_u != 0 or attack_c > defence_u and defence_u != 0:
		print('你输了')
	elif attack_u > attack_c and attack_c == 0 or attack_c > attack_u and attack_u == 0 or attack_c > defence_u and defence_u ==0 and attack_u > defence_c and defence_c == 0 or attack_u == attack_c or defence_u == defence_c:
		attack_c = 0
		defence_c = 0
		attack_u = 0
		defence_u = 0	
		print(xios)
		turn()
		
		
	
print("输入'xio'以开始游戏")
start=input(str("你："))
if start=='xio':
	xios[1] = xios[1]+1              
	print('电脑：xio')
	xios[0] = xios[0]+1
turn()
	
	
		
		
		
