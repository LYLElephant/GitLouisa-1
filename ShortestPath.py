
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
'''
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
'''
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
def Make_Map(scale):     #将Prim算法的两种方法综合在一起，并有随机加边
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

def solution(x,y):
    #global themap,m,thelist,s
    themap=[]
    for i in Map:
        themap.append(i[:])
    themap[x][y]=3
    destination=(1,scale-2)
    wk=[(x,y)]
    while destination not in wk:
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
    m=themap[1][scale-2]
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
    

'''
def hint():
    result=solution(locmanx,locmany)
    x=min(4,len(result)-1)
    for i in range(x):
        cv.create_line(result[i],result[i+1],fill='yellow',width=1)

def pint_solution():
    s=solution(scale-2,1)
    for i in range(len(s)-1):
        cv.create_line(s[i],s[i+1],fill='yellow',width=1)
'''      
if __name__=='__main__':
    width=10
    scale=1+width*2
    Make_Map(scale)
    solution(scale-4,3)
