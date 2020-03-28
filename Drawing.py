import random
from tkinter import *
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
    
    if  ((width*2-1)**2-(width**2)*2)//50 != 0 :  #下面随机加边
        times=random.randint(1,(((width*2-1)**2-(width**2)*2)//50))  
        for i in range(times):
            a=random.randrange(1,scale-1,2)  #注意易犯错误，randint后边括号内，左右都可以取到
            b=random.randrange(2,scale-1,2)
            Map[a][b]=2
            if Map[a-1][b]==0 and Map[a-1][b-1]==2 and Map[a-1][b+1]==2:
                if a>=3 and Map[a-2][b]==2:  
                    Map[a-1][b]=2
            if Map[a+1][b]==0 and Map[a+1][b-1]==2 and Map[a+1][b+1]==2:
                if a<=scale-4 and Map[a+2][b]==2:
                    Map[a+1][b]=2
    
    
#from tkinter import *
def pint_line(m):
    x,y=m
    linelength=pint_size()
    linewidth=1
    map_locx=scale//5
    map_locy=scale//4
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
def pint_dot(m):
    size=pint_size()
    map_locx=scale//5
    map_locy=scale//4
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
def pint_size():
    if width<=20:
        return 10
    if width>20 and width<=50:
        return 5
    else:
        return 3

def pint_dotMap():
    global dotcan
    dotcan=Canvas(pintwindow,width=scale*size*3//2,height=800,bg='LightSkyBlue')
    for i in range(scale):
        for j in range(scale):
            pint_dot((i,j))
    dotcan.pack(anchor='w')
    
def pint_lineMap():
    global linecan 
    linecan=Canvas(pintwindow,width=scale*size*3//2,height=800,bg='OldLace')       
    for i in range(scale):
        for j in range(scale):
            pint_line((i,j))
    linecan.pack(anchor='w')
    
def pint(flag):
    global size,pintwindow
    pintwindow=Tk()
    pintwindow.title('走迷宫')
    pintwindow.geometry("1000x700")
    Make_Map()
    size=pint_size()
    if flag==0:
        pint_lineMap()
    else:
        pint_dotMap()
    pintwindow.mainloop()
        
def choose_condition():
    global conditionwindow
    conditionwindow=Tk()
    conditionwindow.title('走迷宫')
    button1=Button(conditionwindow,text='室内寻宝',command=lambda:pint(0))
    button2=Button(conditionwindow,text='海上探险',command=lambda:pint(1))
    #button=Button(conditionwindow,text='确定',command=pint)
    #can.create_text(300,30,text="绘制",font=("Arial",18))
    button1.pack()
    button2.pack()
    #button.pack()
    conditionwindow.mainloop()

if __name__=='__main__':
    width=20
    scale=1+width*2
    pint(0)
    #choose_condition()
