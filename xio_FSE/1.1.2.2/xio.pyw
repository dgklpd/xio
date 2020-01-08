# coding = utf-8
'''设置'''
import random
import time
import easygui
import sys 
import os
# 初始化游戏
attack_c = 0
defence_c = 0
attack_u = 0
defence_u = 0
xios = [0, 0]

# 设定电脑初始可用招式
usable_a = ['摸摸']
usable_d = ['地波', '天波']
state = ['usable_a', 'usable_d', 'xio']

'''组件:方法'''
# 招式(电脑)
def xio_c():
    global defence_c, xios
    defence_c = 0.1
    xios[0] = xios[0] + 1
    easygui.msgbox('电脑:xio,计数器' + str(xios),image="source/b1.gif",ok_button='继续',title='xio1.1.2.2')


def dibo_c():
    global defence_c, xios
    defence_c = 1
    easygui.msgbox('电脑:地波,计数器'+str(xios),image="source/b2.gif",ok_button='继续',title='xio1.1.2.2')


def tianbo_c():
    global defence_c, xios
    defence_c = 1
    easygui.msgbox('电脑:天波,计数器'+str(xios),image="source/b3.gif",ok_button='继续',title='xio1.1.2.2')


def chaofang_c():
    global defence_c, xios
    defence_c = 9
    xios[0] = xios[0] - 1
    easygui.msgbox('电脑:超防,计数器'+str(xios),image="source/b4.gif",ok_button='继续',title='xio1.1.2.2')


def leiba_c():
    global attack_c, xios
    attack_c = 0.3
    xios[0] = xios[0] - 0.3
    easygui.msgbox('电脑:雷扒,计数器'+str(xios),image="source/b5.gif",ok_button='继续',title='xio1.1.2.2')


def momo_c():
    global attack_c, xios
    attack_c = 1
    xios[0] = xios[0] - 1
    easygui.msgbox('电脑:摸摸,计数器'+str(xios),image="source/b6.gif",ok_button='继续',title='xio1.1.2.2')


def sankan_c():
    global attack_c, xios
    attack_c = 3
    xios[0] = xios[0] - 3
    easygui.msgbox('电脑:三砍,计数器'+str(xios),image="source/b7.gif",ok_button='继续',title='xio1.1.2.2')


def wuhe_c():
    global attack_c, xios
    attack_c = 5
    xios[0] = xios[0] - 5
    easygui.msgbox('电脑:五合体,计数器'+str(xios),image="source/b8.gif",ok_button='继续',title='xio1.1.2.2')


def huhe_c():
    global attack_c, xios
    attack_c = 10
    xios[0] = xios[0] - 10
    easygui.msgbox('电脑:虎合体,计数器'+str(xios),image="source/b9.gif",ok_button='继续',title='xio1.1.2.2')


# 招式(玩家)
def xio_u():
    global defence_u, xios
    defence_u = 0.1
    xios[1] = xios[1] + 1


def dibo_u():
    global defence_u, xios
    defence_u = 1


def tianbo_u():
    global defence_u, xios
    defence_u = 1


def chaofang_u():
    global defence_u, xios
    defence_u = 9
    xios[1] = xios[1] - 1


def leiba_u():
    global attack_u, xios
    attack_u = 0.3
    xios[1] = xios[1] - 0.3


def momo_u():
    global attack_u, xios
    attack_u = 1
    xios[1] = xios[1] - 1


def sankan_u():
    global attack_u, xios
    attack_u = 3
    xios[1] = xios[1] - 3


def wuhe_u():
    global attack_u, xios
    attack_u = 5
    xios[1] = xios[1] - 5


def huhe_u():
    global attack_u, xios
    attack_u = 10
    xios[1] = xios[1] - 10


def Start():
    global start
    easygui.msgbox("请输入xio以开始游戏")
    start = easygui.enterbox('请出招式')
    if start == 'xio':
        xios[1] = xios[1] + 1
        easygui.msgbox('电脑:xio,计数器' + str(xios),image="source/b1.gif",ok_button='继续',title='xio1.1.2.2')
        xios[0] = xios[0] + 1
        turn()
    else:
        Start()
'''游戏进行状态'''
#重启组
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)
#爆死控件
def bao():
    options=easygui.buttonbox('你爆死',image="source/b13.gif",title='游戏结束',choices=('结束游戏','重新开始'))
    if options == '结束游戏':
	    sys.exit()
    else:
	    restart_program()
#赢控件
def win():
    options=easygui.buttonbox('你赢了',image="source/b10.gif",title='游戏结束',choices=('结束游戏','重新开始'))
    if options == '结束游戏':
	    sys.exit()
    else:
	    restart_program()
#输控件
def lose():
    options=easygui.buttonbox('你输了',image="source/b11.gif",title='游戏结束',choices=('结束游戏','重新开始'))
    if options == '结束游戏':
	    sys.exit()
    else:
	    restart_program()

'''电脑模块'''
def cpu():
    # 控制不爆死
    global usable_a, usable_d, attack_c, defence_c, state
    if xios[0] < 0.3:
        usable_a = ['xio']
        usable_d = ['地波', '天波']
    elif xios[0] < 1:
        usable_a = ['雷扒']
        usable_d = ['地波', '天波']
    elif xios[0] < 3:
        usable_a = ['摸摸', '雷扒']
        usable_d = ['地波', '天波', '超防']
    elif xios[0] < 5:
        usable_a = ['摸摸', '雷扒', '三砍']
        usable_d = ['地波', '天波', '超防']
    elif xios[0] < 10:
        usable_a = ['摸摸', '雷扒', '三砍', '五合体']
        usable_d = ['地波', '天波', '超防']
    else:
        usable_a = ['摸摸', '雷扒', '三砍', '五合体', '虎合体']
        usable_d = ['地波', '天波', '超防']
    if xios[1] < 3  and '超防' in usable_d:
        usable_d.remove('超防')
    else:
        pass
    # 出招式
    go = random.choice(state)
    if go == 'usable_a' and usable_a is not None:
        get = random.choice(usable_a)
        if get == 'xio':
            xio_c
        elif get == '雷扒':
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
'''用户模块'''
def user():
	global attack_c, attack_u, defence_c, defence_u
	#接受输入
	usr = easygui.enterbox("请出招式(输入'q'退出程序)",title='xio1.1.2.2')
	#判断技能，写入数值
	if usr == 'q':
		sys.exit()
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
	elif usr == '地波' or usr == 'd':
		dibo_u()
	elif usr == '天波':
		tianbo_u()
	elif usr == '超防':
		chaofang_u()
	else:
            easygui.msgbox('无定法判断这个技能，请重新输入',ok_button='重新输入')
            turn()
'''每一轮控件'''
def turn():
    global attack_c, attack_u, defence_c, defence_u
    # 调用用户出招式
    user()
    # 调用电脑给出招式
    cpu()
    '''判断'''
    # 全转浮点数
    attack_c = float(attack_c)
    attack_u = float(attack_u)
    defence_c = float(defence_c)
    defence_u = float(defence_u)
    # 判断输赢
    if xios[1] < 0:
        bao()
    elif attack_u > attack_c and attack_c != 0 or attack_u > defence_c and defence_c != 0:
        win()
    elif attack_c > attack_u and attack_u != 0 or attack_c > defence_u and defence_u != 0:
        lose()
    elif attack_u > attack_c and attack_c == 0 or attack_c > attack_u and attack_u == 0 or attack_c > defence_u and defence_u == 0 and attack_u > defence_c and defence_c == 0 or attack_u == attack_c or defence_u == defence_c:
        attack_c = 0
        defence_c = 0
        attack_u = 0
        defence_u = 0
        turn()
'''游戏开始切入点'''
easygui.msgbox('xio1.1.2版本，easygui前端特别版',image='source/b12.gif',ok_button='开始游戏')
Start()







