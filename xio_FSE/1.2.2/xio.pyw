# coding:utf-8
'''璁剧疆'''
import random
import time
import easygui
import sys 
import os
# 鍒濆�鍖栨父鎴�attack_c = 0
defence_c = 0
attack_u = 0
defence_u = 0
xios = [0, 0]
pan = 0

# 璁惧畾鐢佃剳鍒濆�鍙�敤鎷涘紡
usable_a = ['鎽告懜']
usable_d = ['鍦版尝', '澶╂尝']
state = ['usable_a', 'usable_d', 'xio']

'''缁勪欢:鏂规硶'''
# 鎷涘紡(鐢佃剳)
def xio_c():
    global defence_c, xios
    defence_c = 0.1
    xios[0] = xios[0] + 1
    easygui.msgbox('鐢佃剳:xio,璁℃暟鍣� + str(xios),image="source/b1.gif",ok_button='缁х画',title='xio1.1.2.2')


def dibo_c():
    global defence_c, xios
    defence_c = 1
    easygui.msgbox('鐢佃剳:鍦版尝,璁℃暟鍣�+str(xios),image="source/b2.gif",ok_button='缁х画',title='xio1.1.2.2')


def tianbo_c():
    global defence_c, xios
    defence_c = 1
    easygui.msgbox('鐢佃剳:澶╂尝,璁℃暟鍣�+str(xios),image="source/b3.gif",ok_button='缁х画',title='xio1.1.2.2')


def chaofang_c():
    global defence_c, xios
    defence_c = 9
    xios[0] = xios[0] - 1
    easygui.msgbox('鐢佃剳:瓒呴槻,璁℃暟鍣�+str(xios),image="source/b4.gif",ok_button='缁х画',title='xio1.1.2.2')


def leiba_c():
    global attack_c, xios
    attack_c = 0.3
    xios[0] = xios[0] - 0.3
    easygui.msgbox('鐢佃剳:闆锋墥,璁℃暟鍣�+str(xios),image="source/b5.gif",ok_button='缁х画',title='xio1.1.2.2')


def momo_c():
    global attack_c, xios
    attack_c = 1
    xios[0] = xios[0] - 1
    easygui.msgbox('鐢佃剳:鎽告懜,璁℃暟鍣�+str(xios),image="source/b6.gif",ok_button='缁х画',title='xio1.1.2.2')


def sankan_c():
    global attack_c, xios
    attack_c = 3
    xios[0] = xios[0] - 3
    easygui.msgbox('鐢佃剳:涓夌爫,璁℃暟鍣�+str(xios),image="source/b7.gif",ok_button='缁х画',title='xio1.1.2.2')


def wuhe_c():
    global attack_c, xios
    attack_c = 5
    xios[0] = xios[0] - 5
    easygui.msgbox('鐢佃剳:浜斿悎浣�璁℃暟鍣�+str(xios),image="source/b8.gif",ok_button='缁х画',title='xio1.1.2.2')


def huhe_c():
    global attack_c, xios
    attack_c = 10
    xios[0] = xios[0] - 10
    easygui.msgbox('鐢佃剳:铏庡悎浣�璁℃暟鍣�+str(xios),image="source/b9.gif",ok_button='缁х画',title='xio1.1.2.2')


# 鎷涘紡(鐜╁�)
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
    easygui.msgbox("璇疯緭鍏�io浠ュ紑濮嬫父鎴�)
    start = easygui.enterbox('璇峰嚭鎷涘紡')
    if start == 'xio':
        xios[1] = xios[1] + 1
        easygui.msgbox('鐢佃剳:xio,璁℃暟鍣� + str(xios),image="source/b1.gif",ok_button='缁х画',title='xio1.1.2.2')
        xios[0] = xios[0] + 1
        turn()
    else:
        Start()
'''娓告垙杩涜�鐘舵�'''
#閲嶅惎缁�def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)
#鐖嗘�鎺т欢
def bao():
    options=easygui.buttonbox('浣犵垎姝�,image="source/b13.gif",title='娓告垙缁撴潫',choices=('缁撴潫娓告垙','閲嶆柊寮��'))
    if options == '缁撴潫娓告垙':
	    sys.exit()
    else:
	    restart_program()
#璧㈡帶浠�def win():
    options=easygui.buttonbox('浣犺耽浜�,image="source/b10.gif",title='娓告垙缁撴潫',choices=('缁撴潫娓告垙','閲嶆柊寮��'))
    if options == '缁撴潫娓告垙':
	    sys.exit()
    else:
	    restart_program()
#杈撴帶浠�def lose():
    options=easygui.buttonbox('浣犺緭浜�,image="source/b11.gif",title='娓告垙缁撴潫',choices=('缁撴潫娓告垙','閲嶆柊寮��'))
    if options == '缁撴潫娓告垙':
	    sys.exit()
    else:
	    restart_program()

'''鐢佃剳妯″潡'''
def cpu():
    # 鎺у埗涓嶇垎姝�    global usable_a, usable_d, attack_c, defence_c, state
    if xios[0] < 0.3:
        usable_a = ['xio']
        usable_d = ['鍦版尝', '澶╂尝']
    elif xios[0] < 1:
        usable_a = ['闆锋墥']
        usable_d = ['鍦版尝', '澶╂尝']
    elif xios[0] < 3:
        usable_a = ['鎽告懜', '闆锋墥']
        usable_d = ['鍦版尝', '澶╂尝', '瓒呴槻']
    elif xios[0] < 5:
        usable_a = ['鎽告懜', '闆锋墥', '涓夌爫']
        usable_d = ['鍦版尝', '澶╂尝', '瓒呴槻']
    elif xios[0] < 10:
        usable_a = ['鎽告懜', '闆锋墥', '涓夌爫', '浜斿悎浣�]
        usable_d = ['鍦版尝', '澶╂尝', '瓒呴槻']
    else:
        usable_a = ['鎽告懜', '闆锋墥', '涓夌爫', '浜斿悎浣�, '铏庡悎浣�]
        usable_d = ['鍦版尝', '澶╂尝', '瓒呴槻']
    if xios[1] < 3  and '瓒呴槻' in usable_d:
        usable_d.remove('瓒呴槻')
    else:
        pass
    # 鍑烘嫑寮�    go = random.choice(state)
    if go == 'usable_a' and usable_a is not None:
        get = random.choice(usable_a)
        if get == 'xio':
            xio_c
        elif get == '闆锋墥':
            leiba_c()
        elif get == '鎽告懜':
            momo_c()
        elif get == '涓夌爫':
            sankan_c()
        elif get == '浜斿悎浣�:
            wuhe_c()
        elif get == '铏庡悎浣�:
            huhe_c()
    elif go == 'usable_d':
        get = random.choice(usable_d)
        if get == '澶╂尝':
            tianbo_c()
        if get == '鍦版尝':
            dibo_c()
        if get == '瓒呴槻':
            chaofang_c()
    elif go == 'xio':
        xio_c()
'''鐢ㄦ埛妯″潡'''
def user():
	global attack_c, attack_u, defence_c, defence_u
	#鎺ュ彈杈撳叆
	usr = easygui.enterbox("璇峰嚭鎷涘紡(杈撳叆'q'閫�嚭绋嬪簭)",title='xio1.1.2.2')
	#鍒ゆ柇鎶�兘锛屽啓鍏ユ暟鍊�	if usr == 'q':
		sys.exit()
	if usr == 'xio' or usr=='x':
		xio_u()
	elif usr == '鎽告懜' or usr=='momo':
		momo_u()
	elif usr == '涓夌爫' or usr == 'sankan':
		sankan_u()
	elif usr == '闆锋墥' or usr == 'leiba':
		leiba_u()
	elif usr == '浜斿悎浣� or usr == 'wuhe':
		wuhe_u()
	elif usr == '铏庡悎浣� or usr =='huhe':
		huhe_u()
	elif usr == '鍦版尝' or usr == 'd':
		dibo_u()
	elif usr == '澶╂尝' or usr== 'tianbo':
		tianbo_u()
	elif usr == '瓒呴槻' or usr == 'chaofang':
		chaofang_u()
	else:
            easygui.msgbox('鏃犲畾娉曞垽鏂�繖涓�妧鑳斤紝璇烽噸鏂拌緭鍏�,ok_button='閲嶆柊杈撳叆')
            turn()
'''姣忎竴杞�帶浠�''
def turn():
    global attack_c, attack_u, defence_c, defence_u
    # 璋冪敤鐢ㄦ埛鍑烘嫑寮�    user()
    # 璋冪敤鐢佃剳缁欏嚭鎷涘紡
    cpu()
    '''鍒ゆ柇'''
    # 鍏ㄨ浆娴�偣鏁�    attack_c = float(attack_c)
    attack_u = float(attack_u)
    defence_c = float(defence_c)
    defence_u = float(defence_u)
    # 鍒ゆ柇杈撹耽
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
'''娓告垙寮��鍒囧叆鐐�''
easygui.msgbox('xio1.1.2鐗堟湰锛宔asygui鍓嶇�鐗瑰埆鐗�,image='source/b12.gif',ok_button='寮��娓告垙')
Start()







