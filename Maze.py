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