#迷宫形成
import random
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
def check_position(x,y):
    l=[]
    if x>=3 and Map[x-2][y]==1:
        l.append((x-2,y))
    if x<=scale-4 and Map[x+2][y]==1:
        l.append((x+2,y))
    if y>=3 and Map[x][y-2]==1:
        l.append((x,y-2))
    if y<=scale-4 and Map[x][y+2]==1:
        l.append((x,y+2))
    if len(l)==0:
        return 0
    else:
        return l
def Make_Map(scale):     #将Prim算法的两种方法综合在一起，并有随机加边
    global Map
    Map=set_Map(scale)
    Will_check=[(scale-2,1)]
    while len(Will_check)!=0:
        the=random.choice(Will_check)
        x,y=the
        if check_position(x,y)!=0:            
            new=random.choice(check_position(x,y))
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
if __name__=='__main__':
    width=20
    scale=1+width*2
    Make_Map(scale)
'''
def prim1(scale):           #深度优先制作迷宫
    global Map
    Map=set_Map(scale)
    Will_check=[(scale-2,1)]
    while len(Will_check)!=0:
        x,y=Will_check[-1]
        if check_position(x,y)!=0:
            new=random.choice(check_position(x,y))
            Will_check.append(new)
            Map[new[0]][new[1]]=2
            Map[(new[0]+x)//2][(new[1]+y)//2]=2
        else:
            Will_check.pop(-1)
    print(Map)                    #待用GUI形式表现出来

def prim2(scale):          #广度优先制作迷宫
    global Map
    Map=set_Map(scale)
    Will_check=[(scale-2,1)]
    while len(Will_check)!=0:
        x,y=Will_check[0]
        if check_position(x,y)!=0:
            Will_check.pop(0)
            new_list=check_position(x,y)
            random.shuffle(new_list)
            Will_check+=new_list
            for new in new_list:
                Map[new[0]][new[1]]=2
                Map[(new[0]+x)//2][(new[1]+y)//2]=2
        else:
            Will_check.pop(0)     
    print(Map)                    #待用GUI形式表现出来
'''