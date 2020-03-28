#This is an example
import random
from tkinter import *
import tkinter.font as tkFont

def set_Map(scale):
    Map=[[0 for i in range(scale)] for j in range(scale)]
    Map[1][scale-1]=2
    Map[scale-2][0]=2 
    for i in range(scale):
        for j in range(scale):
            if i%2==1 and j%2==1:
                Map[i][j]=1
    Map[scale-2][1]=2
    return Map
'''将生成一个原始“地图”的二维列表'''

def check_position(L,x,y,step,num):
    l=[]
    if x>=3 and L[x-step][y]==num:
        l.append((x-step,y))
    if x<=scale-4 and L[x+step][y]==num:
        l.append((x+step,y))
    if y>=3 and L[x][y-step]==num:
        l.append((x,y-step))
    if y<=scale-4 and L[x][y+step]==num:
        l.append((x,y+step))
    if len(l)==0:
        return 0
    else:
        return l
'''检查某个列表L某个位置(x,y)，离它step长的上下左右（如果有的话）的等于num的位置坐标，如果没有的话返回0'''

def Make_Map():     #将Prim算法的两种方法综合在一起，并有随机加边
    global Map
    Map=set_Map(scale)
    Will_check=[(scale-2,1)]
    while len(Will_check)!=0:
        the=random.choice(Will_check)
        x,y=the
        if check_position(Map,x,y,2,1)!=0:            
            new=random.choice(check_position(Map,x,y,2,1))
            Will_check.append(new)
            Map[new[0]][new[1]]=2
            Map[(new[0]+x)//2][(new[1]+y)//2]=2
        else:
            Will_check.remove(the)
    if  ((wid*2-1)**2-(wid**2)*2)//50 != 0 :     #下面随机加边
        times=random.randint(1,(((wid*2-1)**2-(wid**2)*2)//50))  
        for i in range(times):
            a=random.randrange(1,scale-1,2)    #注意易犯错误，randint后边括号内，左右都可以取到
            b=random.randrange(2,scale-1,2)    #取的点位置保证是两个房间之间的，而不是对角上的
            Map[a][b]=2                        #以下操作是为了防止某些点被孤立
            if Map[a-1][b]==0 and Map[a-1][b-1]==2 and Map[a-1][b+1]==2:
                if a>=3 and Map[a-2][b]==2:  
                    Map[a-1][b]=2
            if Map[a+1][b]==0 and Map[a+1][b-1]==2 and Map[a+1][b+1]==2:
                if a<=scale-4 and Map[a+2][b]==2:
                    Map[a+1][b]=2
'''将生成一个随机的迷宫地图，其中2表示可走，0表示不可走'''

def pint_line(m):
    x,y=m
    linelength=size
    linewidth=1
    linecolor='Peru'
    arrowcolor='red'
    if Map[x][y]==0 and x>0 and Map[x-1][y]==0:
        a=x-1
        b=y
        loc1=(linelength*(y+map_locy),linelength*(x+map_locx))
        loc2=(linelength*(b+map_locy),linelength*(a+map_locx))
        linecan.create_line(loc1,loc2,width=linewidth,fill=linecolor)
    if Map[x][y]==0 and x<scale-2 and Map[x+1][y]==0:
        a=x+1
        b=y
        loc1=(linelength*(y+map_locy),linelength*(x+map_locx))
        loc2=(linelength*(b+map_locy),linelength*(a+map_locx))
        linecan.create_line(loc1,loc2,width=linewidth,fill=linecolor)
    if Map[x][y]==0 and y>0 and Map[x][y-1]==0:
        a=x
        b=y-1
        loc1=(linelength*(y+map_locy),linelength*(x+map_locx))
        loc2=(linelength*(b+map_locy),linelength*(a+map_locx))
        linecan.create_line(loc1,loc2,width=linewidth,fill=linecolor)
    if Map[x][y]==0 and y<scale-2 and Map[x][y+1]==0:
        a=x
        b=y+1
        loc1=(linelength*(y+map_locy),linelength*(x+map_locx))
        loc2=(linelength*(b+map_locy),linelength*(a+map_locx))
        linecan.create_line(loc1,loc2,width=linewidth,fill=linecolor)
    if m==(scale-2,0):
        y,x=linelength*(x+map_locx),linelength*(y-1+map_locy)
        loc3=(x-15,y)
        loc4=(x+linelength//2,y)
        linecan.create_line(loc3,loc4,fill=arrowcolor,arrow='last')
    if m==(1,scale-1):
        y,x=linelength*(x+map_locx),linelength*(y+1+map_locy)
        loc3=(x-linelength//2,y)
        loc4=(x+15,y)
        linecan.create_line(loc3,loc4,fill=arrowcolor,arrow='last')
'''画出线式迷宫之间的连线，并且画出入口和出口的箭头'''

def pint_dot(m):
    dotcolor='green'
    arrowcolor='red'
    x,y=m
    if Map[x][y]==0:
        y,x=size*(x+map_locx),size*(y+map_locy)
        loc1=(x-size//2,y-size//2)
        loc2=(x+size//2,y+size//2)
        dotcan.create_rectangle(loc1,loc2,outline=dotcolor,fill=dotcolor)
    if m==(scale-2,0):
        y,x=size*(x+map_locx),size*(y-1+map_locy)
        loc3=(x-15,y)
        loc4=(x+size//2,y)
        dotcan.create_line(loc3,loc4,fill=arrowcolor,arrow='last')
    if m==(1,scale-1):
        y,x=size*(x+map_locx),size*(y+1+map_locy)
        loc3=(x-size//2,y)
        loc4=(x+15,y)
        dotcan.create_line(loc3,loc4,fill=arrowcolor,arrow='last')
'''画出点式迷宫中所代表的含义——即要么不画，要么为矩形，代表墙，并且画出入口和出口的箭头'''

def pint_dotMap():
    global dotcan,man
    dotcan=Canvas(pintwindow,width=1000,height=800,bg='LightSkyBlue')
    for i in range(scale):
        for j in range(scale):
            pint_dot((i,j))
    dotcan.pack(anchor='w')
    button_choose=Button(dotcan,text='选择关卡',font=ft02,command=lambda:choose())
    dotcan.create_window((820,450),window=button_choose)
    button_over=Button(dotcan,text='退出游戏',font=ft02,command=lambda:over(pintwindow))
    button_hint=Button(dotcan,text='提示',font=ft02,command=lambda:hint())
    button_solution=Button(dotcan,text='参考答案',font=ft02,command=lambda:pint_solution())
    dotcan.create_window((820,510),window=button_over)
    dotcan.create_window((820,330),window=button_hint)
    dotcan.create_window((820,390),window=button_solution)
    dotcan.create_text(820,50,text="首先用鼠标点击一下迷宫^o^",font=ft02,fill='red')
    dotcan.create_text(820,100,text="你的键盘上的上下左右键",font=ft02)
    dotcan.create_text(820,130,text="可以控制迷宫中小圆点的移动哦",font=ft02)
    dotcan.create_text(820,180,text="帮助入口的小圆点找到出口的小圆点，",font=ft02)
    dotcan.create_text(820,210,text="你就成功了！加油ヾ(◍°∇°◍)ﾉﾞ",font=ft02)
    dotcan.create_text(820,260,text="如果你在迷宫中迷路了，请按提示按钮",font=ft02)
    man=dotcan.create_oval((size*(1+map_locy)-(size//2),size*(scale-2+map_locx)-(size//2)),(size*(1+map_locy)+(size//2),size*(scale-2+map_locx)+(size//2)),fill='red')
    dotcan.create_oval((size*(scale-2+map_locy)-(size//2),size*(1+map_locx)-(size//2)),(size*(scale-2+map_locy)+(size//2),size*(1+map_locx)+(size//2)),fill='red')
'''设置点式迷宫的画布，以及在画布中要展现的按钮、文字等'''

def pint_lineMap():
    global linecan,man
    linecan=Canvas(pintwindow,width=1000,height=800,bg='OldLace')       
    for i in range(scale):
        for j in range(scale):
            pint_line((i,j))
    linecan.pack(anchor='w')
    button_choose=Button(linecan,text='选择关卡',font=ft02,command=lambda:choose())
    linecan.create_window((820,450),window=button_choose)
    button_over=Button(linecan,text='退出游戏',font=ft02,command=lambda:over(pintwindow))
    button_hint=Button(linecan,text='提示',font=ft02,command=lambda:hint())
    button_solution=Button(linecan,text='参考答案',font=ft02,command=lambda:pint_solution())
    linecan.create_window((820,510),window=button_over)
    linecan.create_window((820,330),window=button_hint)
    linecan.create_window((820,390),window=button_solution)
    linecan.create_text(820,50,text="首先用鼠标点击一下迷宫^o^",font=ft02,fill='red')
    linecan.create_text(820,100,text="你的键盘上的上下左右键",font=ft02)
    linecan.create_text(820,130,text="可以控制迷宫中小圆点的移动哦",font=ft02)
    linecan.create_text(820,180,text="帮助入口的小圆点找到出口的小圆点，",font=ft02)
    linecan.create_text(820,210,text="你就成功了！加油ヾ(◍°∇°◍)ﾉﾞ",font=ft02)
    linecan.create_text(820,260,text="如果你在迷宫中迷路了，请按提示按钮",font=ft02)
    man=linecan.create_oval((size*(1+map_locy)-(size//2),size*(scale-2+map_locx)-(size//2)),(size*(1+map_locy)+(size//2),size*(scale-2+map_locx)+(size//2)),fill='red')
    linecan.create_oval((size*(scale-2+map_locy)-(size//2),size*(1+map_locx)-(size//2)),(size*(scale-2+map_locy)+(size//2),size*(1+map_locx)+(size//2)),fill='red')
'''设置线式迷宫的画布，以及在画布中要展现的按钮、文字等'''

def pint(flag):
    global size,pintwindow,locmanx,locmany,condition,cv
    over(conditionwindow)
    pintwindow=Tk()
    pintwindow.title('迷宫游戏')
    pintwindow.geometry("1000x700+200+2")
    Make_Map()
    locmanx=scale-2
    locmany=1
    condition=flag
    pintwindow.bind("<Left>",Left0)
    pintwindow.bind("<Right>",Right0)
    pintwindow.bind("<Up>",Up0)
    pintwindow.bind("<Down>",Down0)
    if condition==0:
        pint_lineMap()
        cv=linecan
    else:
        pint_dotMap()
        cv=dotcan
'''设置在不同场景选择下相同和不同的参数'''
        
def choose_condition():
    global conditionwindow
    conditionwindow=Tk()
    conditionwindow.title('迷宫游戏')
    conditionwindow.geometry('400x300+450+125')
    can_condition=Canvas(conditionwindow,height=300,width=400,bg='black')
    can_condition.create_text(200,50,text='本游戏提供两种游戏背景，',fill='white',font=ft02)
    can_condition.create_text(205,80,text='两种情境下的迷宫是一样的，只是背景不同。',fill='white',font=ft02)
    can_condition.create_text(200,110,text='请你选择一种你更喜欢的游戏背景：',fill='white',font=ft02)
    button1=Button(can_condition,text='室内寻宝',fg='white',bg='black',font=ft02,command=lambda:pint(0))
    button2=Button(can_condition,text='海上探险',fg='white',bg='black',font=ft02,command=lambda:pint(1))
    can_condition.create_window((120,200),window=button1)
    can_condition.create_window((290,200),window=button2)
    can_condition.pack()
'''设置选择场景的界面'''

def over(m):
    m.destroy()
'''关闭某个窗口'''
    
def choose():
    over(pintwindow)
    choose_level()
'''关闭上一个初始窗口，并进入下一个等级选择的窗口'''

def choose_level():
    global levelwindow
    levelwindow=Tk()
    levelwindow.title('迷宫游戏')
    levelwindow.geometry('300x400+500+150')
    can_level=Canvas(levelwindow,height=400,width=300,bg='black')
    can_level.create_text(90,50,text='请选择难度等级：',fill='white',font=ft02)
    buttona=Button(can_level,text='初级0：轻松一刻',fg='white',bg='black',font=ft03,command=lambda:start(1))
    buttonb=Button(can_level,text='中级1：小试牛刀',fg='white',bg='black',font=ft03,command=lambda:start(2))
    buttonc=Button(can_level,text='中级2：更上层楼',fg='white',bg='black',font=ft03,command=lambda:start(3))
    buttond=Button(can_level,text='高级1：突破自我',fg='white',bg='black',font=ft03,command=lambda:start(4))
    buttone=Button(can_level,text='高级2：笑傲江湖',fg='white',bg='black',font=ft03,command=lambda:start(5))
    buttonf=Button(can_level,text='高级3：炉火纯青',fg='white',bg='black',font=ft03,command=lambda:start(6))
    can_level.create_window((150,100),window=buttona)
    can_level.create_window((150,150),window=buttonb)
    can_level.create_window((150,200),window=buttonc)
    can_level.create_window((150,250),window=buttond)
    can_level.create_window((150,300),window=buttone)
    can_level.create_window((150,350),window=buttonf)
    can_level.pack()
'''设置等级选择的窗口'''
    
def start(k):
    global level,wid,scale,size,map_locx,map_locy
    level=k
    if level==1:
        wid=20
        size=10
        map_locx=10
        map_locy=10
    elif level==2:
        wid=40
        size=7
        map_locx=5
        map_locy=5
    elif level==3:
        wid=50
        size=6
        map_locx=2
        map_locy=5
    elif level==4:
        wid=60
        size=5
        map_locx=2
        map_locy=5
    elif level==5:
        wid=70
        size=4
        map_locx=8
        map_locy=8
    else:
        wid=80
        size=3
        map_locx=20
        map_locy=20
    scale=1+wid*2
    choose_condition()
    over(levelwindow)
'''设置不同等级的参数，并关闭等级选择的窗口，进入情景选择的窗口'''

def Up0(event):
    global locmanx,locmany
    x=locmanx
    y=locmany
    if x>=3 and Map[x-1][y]==2 and Map[x-2][y]==2:
        cv.move(man,0,-2*size)
        loc1=(size*(y+map_locy),size*(x+map_locx))
        loc2=(size*(y+map_locy),size*(x-2+map_locx))
        cv.create_line(loc1,loc2,width=1,fill='red')
        locmanx-=2
    if (locmanx,locmany)==(1,scale-2):
        pintwin()
'''设置键盘上绑定的Up按键触发后窗口的交互，并判断游戏者目前所处位置是否是终点位置'''
    
def Down0(event):
    global locmanx,locmany
    x=locmanx
    y=locmany
    if x<=scale-4 and Map[x+1][y]==2 and Map[x+2][y]==2:
        cv.move(man,0,2*size)
        loc1=(size*(y+map_locy),size*(x+map_locx))
        loc2=(size*(y+map_locy),size*(x+2+map_locx))
        cv.create_line(loc1,loc2,width=1,fill='red')
        locmanx+=2
    if (locmanx,locmany)==(1,scale-2):
        pintwin()
'''设置键盘上绑定的Down按键触发后窗口的交互，并判断游戏者目前所处位置是否是终点位置'''
        
def Left0(event):
    global locmanx,locmany
    x=locmanx
    y=locmany
    if y>=3 and Map[x][y-1]==2 and Map[x][y-2]==2:
        cv.move(man,-2*size,0)
        loc1=(size*(y+map_locy),size*(x+map_locx))
        loc2=(size*(y-2+map_locy),size*(x+map_locx))
        cv.create_line(loc1,loc2,width=1,fill='red')
        locmany-=2
    if (locmanx,locmany)==(1,scale-2):
        pintwin()
'''设置键盘上绑定的Left按键触发后窗口的交互，并判断游戏者目前所处位置是否是终点位置'''

def Right0(event):
    global locmanx,locmany
    x=locmanx
    y=locmany
    if y<=scale-4 and Map[x][y+1]==2 and Map[x][y+2]==2:
        cv.move(man,2*size,0)
        loc1=(size*(y+map_locy),size*(x+map_locx))
        loc2=(size*(y+2+map_locy),size*(x+map_locx))
        cv.create_line(loc1,loc2,width=1,fill='red')
        locmany+=2
    if (locmanx,locmany)==(1,scale-2):
        pintwin()
'''设置键盘上绑定的Right按键触发后窗口的交互，并判断游戏者目前所处位置是否是终点位置'''

def solution(x,y):
    themap=[]
    for i in Map:
        themap.append(i[:])       #复制一个Map的副本，命名为themap
    themap[x][y]=3
    destination=(1,scale-2)
    wk=[(x,y)]
    while destination not in wk:  #广度优先遍历themap，并在themap上做标记
        po=wk.pop(0)
        if check_position(themap,po[0],po[1],1,2)!=0:
            n=themap[po[0]][po[1]]+1
            newlist=check_position(themap,po[0],po[1],1,2)
            for i in newlist:
                nx=2*i[0]-po[0]
                ny=2*i[1]-po[1]
                wk.append((nx,ny))
                themap[nx][ny]=n
                themap[i[0]][i[1]]=1
    s=[destination]
    m=themap[1][scale-2]      #根据themap上做的标记，将最短路径寻找出来，并将路径的位置放入s中
    while m!=3:
        m-=1
        thelist=check_position(themap,s[-1][0],s[-1][1],2,m)
        for k in thelist:
            zx=(s[-1][0]+k[0])//2
            zy=(s[-1][1]+k[1])//2
            if themap[zx][zy]==1:
                s.append(k)
                break
    return s
'''根据广度优先算法，将(x,y)位置的房间到终点房间的最短路径寻找出来'''

def hint():
    result=solution(locmanx,locmany)
    for i in range(len(result)-1):
        loc1=(size*(result[i][1]+map_locy),size*(result[i][0]+map_locx))
        loc2=(size*(result[i+1][1]+map_locy),size*(result[i+1][0]+map_locx))
        cv.create_line(loc1,loc2,fill='black',width=1)
'''提示按钮，画出从当前位置到迷宫终点的最短路径'''

def pint_solution():
    s=solution(scale-2,1)
    for i in range(len(s)-1):
        loc1=(size*(s[i][1]+map_locy),size*(s[i][0]+map_locx))
        loc2=(size*(s[i+1][1]+map_locy),size*(s[i+1][0]+map_locx))
        cv.create_line(loc1,loc2,fill='yellow',width=1)
'''参考答案按钮，画出从迷宫起点到迷宫终点的最短路径'''

def pintwin():
    winwindow=Tk()
    winwindow.title('赢咯！你真厉害！')
    winwindow.geometry('800x300+330+100')
    can_photo=Canvas(winwindow,height=300,width=800,bg='white')
    can_photo.create_text(400,150,text='You are great!    \(@^0^@)/',fill='red',font=("Arial",40))
    can_photo.pack()
    winwindow.mainloop()
'''设置当游戏者成功走到迷宫终点时的弹出窗口'''

def begin():
    over(startwindow)
    choose_level()
'''关闭起始窗口，打开等级选择窗口'''
startwindow=Tk()
startwindow.title('迷宫游戏')
startwindow.geometry('600x650+330+6')
ft01 = tkFont.Font(size=50, weight=tkFont.BOLD)
ft02 = tkFont.Font(size=20, weight=tkFont.BOLD)
ft03 = tkFont.Font(size=10, weight=tkFont.BOLD)
img2=PhotoImage(file='0.migong.gif')
can_start=Canvas(startwindow,height=650,width=700,bg='black')
can_start.create_image(300,330,image=img2)
can_start.create_text(300,150,text='迷宫游戏',fill='white',font=ft01)
button_start=Button(can_start,text='开始游戏',fg='white',bg='black',font=ft02,command=lambda:begin())
button_over=Button(can_start,text='退出游戏',fg='white',bg='black',font=ft02,command=lambda:over(startwindow))
can_start.create_window((300,450),window=button_start)
can_start.create_window((300,530),window=button_over)
can_start.pack()
startwindow.mainloop()
'''设置起始窗口'''
'''This is an example'''
'''if you have more idea,please email me'''