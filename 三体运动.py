

import numpy as np
import getpass
import os
import tkinter as tk
import time
import matplotlib.pyplot as plt

#获取用户名
name=getpass.getuser()
judge=0
f_num1=0
def f_way1():#文件夹方法
    global f_num1
    f_num1=f_num1+1
    try:
        os.mkdir('C:\\Users\\'+name+'\\Desktop\\threebody\\threebody'+str(f_num1))
        
    except FileExistsError:
        f_way1()

def window():#创建窗口
    global f_num1,name,f,e_m1,e_m2,e_m3,e_t,e_v1x,e_v2x,e_v3x,e_v1y,e_v2y,e_v3y,e_G,e_x1,e_x2,e_x3,e_y1,e_y2,e_y3,e_waittime,x1,y1,x2,y2,x3,y3,v1_x,v1_y,v2_x,v3_x,v3_y,v2_y,write_num,e_runtime,e_file,window
    window=tk.Tk()
    window.title("Threebody")
    window.geometry('500x600')
    b_now=tk.Button(window,text="全新的计算",width=15,height=2,command=run1)
    b_now.place(x=5,y=530)
    b_keep=tk.Button(window,text="接着算",width=10,height=2,command=run2)
    b_keep.place(x=130,y=530)
    b_read=tk.Button(window,text="查看最终结果",width=10,height=2,command=read)
    b_read.place(x=225,y=530)
    b_read1=tk.Button(window,text="查看过程结果",width=10,height=2,command=read1)
    b_read1.place(x=315,y=530)
    b_import1=tk.Button(window,text="导入初始数值",width=10,height=2,command=import1)
    b_import1.place(x=410,y=530)

    
    mr_m1=tk.StringVar(value=100)#设置默认
    e_m1=tk.Entry(window,show=None,width=10,textvariable=mr_m1)
    e_m1.place(x=85,y=15)
    mr_m2=tk.StringVar(value=100)
    e_m2=tk.Entry(window,show=None,width=10,textvariable=mr_m2)
    e_m2.place(x=250,y=15)
    mr_m3=tk.StringVar(value=100)
    e_m3=tk.Entry(window,show=None,width=10,textvariable=mr_m3)
    e_m3.place(x=420,y=15)

    mr_v1x=tk.StringVar(value=3)
    e_v1x=tk.Entry(window,show=None,width=12,textvariable=mr_v1x)
    e_v1x.place(x=115,y=45)
    mr_v1y=tk.StringVar(value=1)
    e_v1y=tk.Entry(window,show=None,width=12,textvariable=mr_v1y)
    e_v1y.place(x=115,y=95)
    mr_v2x=tk.StringVar(value=-3)
    e_v2x=tk.Entry(window,show=None,width=12,textvariable=mr_v2x)
    e_v2x.place(x=115,y=145)
    mr_v2y=tk.StringVar(value=5)
    e_v2y=tk.Entry(window,show=None,width=12,textvariable=mr_v2y)
    e_v2y.place(x=115,y=195)
    mr_v3x=tk.StringVar(value=-10)
    e_v3x=tk.Entry(window,show=None,width=12,textvariable=mr_v3x)
    e_v3x.place(x=115,y=245)
    mr_v3y=tk.StringVar(value=1)
    e_v3y=tk.Entry(window,show=None,width=12,textvariable=mr_v3y)
    e_v3y.place(x=115,y=295)

    mr_x1=tk.StringVar(value=80)
    e_x1=tk.Entry(window,show=None,width=12,textvariable=mr_x1)
    e_x1.place(x=315,y=45)
    mr_y1=tk.StringVar(value=100)
    e_y1=tk.Entry(window,show=None,width=12,textvariable=mr_y1)
    e_y1.place(x=315,y=95)
    mr_x2=tk.StringVar(value=50)
    e_x2=tk.Entry(window,show=None,width=12,textvariable=mr_x2)
    e_x2.place(x=315,y=145)
    mr_y2=tk.StringVar(value=150)
    e_y2=tk.Entry(window,show=None,width=12,textvariable=mr_y2)
    e_y2.place(x=315,y=195)
    mr_x3=tk.StringVar(value=120)
    e_x3=tk.Entry(window,show=None,width=12,textvariable=mr_x3)
    e_x3.place(x=315,y=245)
    mr_y3=tk.StringVar(value=30)
    e_y3=tk.Entry(window,show=None,width=12,textvariable=mr_y3)
    e_y3.place(x=315,y=295)

    mr_G=tk.StringVar(value=50)
    e_G=tk.Entry(window,show=None,width=12,textvariable=mr_G)
    e_G.place(x=115,y=345)
    mr_t=tk.StringVar(value=0.1)
    e_t=tk.Entry(window,show=None,width=12,textvariable=mr_t)
    e_t.place(x=115,y=395)
    mr_runtime=tk.StringVar(value=50000)
    e_runtime=tk.Entry(window,show=None,width=12,textvariable=mr_runtime)
    e_runtime.place(x=315,y=345)
    mr_waittime=tk.StringVar(value=10)
    e_waittime=tk.Entry(window,show=None,width=12,textvariable=mr_waittime)
    e_waittime.place(x=315,y=395)
    mr_file=tk.StringVar(value='C:\\Users\\'+name+'\\Desktop\\threebody\\threebody0')
    e_file=tk.Entry(window,show=None,width=53,textvariable=mr_file)
    e_file.place(x=115,y=445)

    l_m1=tk.Label(window,text="绿球的质量：",width=10,height=2)
    l_m1.place(x=10,y=5)
    l_m2=tk.Label(window,text="红球的质量：",width=10,height=2)
    l_m2.place(x=175,y=5)
    l_m3=tk.Label(window,text="蓝球的质量：",width=10,height=2)
    l_m3.place(x=345,y=5)
    l_v1x=tk.Label(window,text="绿球x轴分速度：",width=15,height=2)
    l_v1x.place(x=0,y=35)
    l_v1y=tk.Label(window,text="绿球y轴分速度：",width=15,height=2)
    l_v1y.place(x=0,y=85)
    l_v2x=tk.Label(window,text="红球x轴分速度：",width=15,height=2)
    l_v2x.place(x=0,y=135)
    l_v2y=tk.Label(window,text="红球y轴分速度：",width=15,height=2)
    l_v2y.place(x=0,y=185)
    l_v3x=tk.Label(window,text="蓝球x轴分速度：",width=15,height=2)
    l_v3x.place(x=0,y=235)
    l_v3y=tk.Label(window,text="蓝球y轴分速度：",width=15,height=2)
    l_v3y.place(x=0,y=285)


    l_x1=tk.Label(window,text="绿球x轴坐标：",width=15,height=2)
    l_x1.place(x=200,y=35)
    l_y1=tk.Label(window,text="绿球y轴坐标：",width=15,height=2)
    l_y1.place(x=200,y=85)
    l_x2=tk.Label(window,text="红球x轴坐标：",width=15,height=2)
    l_x2.place(x=200,y=135)
    l_y2=tk.Label(window,text="红球y轴坐标：",width=15,height=2)
    l_y2.place(x=200,y=185)
    l_x3=tk.Label(window,text="蓝球x轴坐标：",width=15,height=2)
    l_x3.place(x=200,y=235)
    l_y3=tk.Label(window,text="蓝球y轴坐标：",width=15,height=2)
    l_y3.place(x=200,y=285)

    l_t=tk.Label(window,text="步长：",width=15,height=2)
    l_t.place(x=0,y=385)
    l_G=tk.Label(window,text="万有引力常数：",width=15,height=2)
    l_G.place(x=0,y=335)
    l_runtime=tk.Label(window,text="计算次数：",width=15,height=2)
    l_runtime.place(x=200,y=335)
    l_waittime=tk.Label(window,text="记录精度：",width=15,height=2)
    l_waittime.place(x=200,y=385)
    l_file=tk.Label(window,text="输入文件夹路径：",width=15,height=2)
    l_file.place(x=0,y=435)

    window.mainloop()

def run1():#创建新的运算
    global f_num1,name,f,e_m1,e_m2,e_m3,e_t,e_v1x,e_v2x,e_v3x,e_v1y,e_v2y,e_v3y,e_G,e_x1,e_x2,e_x3,e_y1,e_y2,e_y3,e_waittime,x1,y1,x2,y2,x3,y3,v1_x,v1_y,v2_x,v3_x,v3_y,v2_y,write_num,e_runtime
    m1=float(e_m1.get())
    m2=float(e_m2.get())
    m3=float(e_m3.get())
    v1_x=float(e_v1x.get())
    v1_y=float(e_v1y.get())
    v2_x=float(e_v2x.get())
    v2_y=float(e_v2y.get())
    v3_x=float(e_v3x.get())
    v3_y=float(e_v3y.get())
    x1=float(e_x1.get())
    y1=float(e_y1.get())
    x2=float(e_x2.get())
    y2=float(e_y2.get())
    x3=float(e_x3.get())
    y3=float(e_y3.get())
    wait_num=float(e_waittime.get())
    G=float(e_G.get())
    t=float(e_t.get())
    runtime=int(e_runtime.get())

    
    #创建文件
    
    
    try:
        os.mkdir('C:\\Users\\'+name+'\\Desktop\\threebody')
        try:
            os.mkdir('C:\\Users\\'+name+'\\Desktop\\threebody\\threebody0')
        except FileExistsError:
            f_way1()
    except FileExistsError:
        print("")
        try:
            os.mkdir('C:\\Users\\'+name+'\\Desktop\\threebody\\threebody0')
        except FileExistsError:
            f_way1()
    
    f0=open('C:\\Users\\'+name+'\\Desktop\\threebody\\threebody'+str(f_num1)+'\\threebody0.txt', mode='x+')    
    f1=open('C:\\Users\\'+name+'\\Desktop\\threebody\\threebody'+str(f_num1)+'\\threebody1.txt', mode='x+')
    f2=open('C:\\Users\\'+name+'\\Desktop\\threebody\\threebody'+str(f_num1)+'\\threebody2.txt', mode='x+')
    
    #写入初始数值
    f0.write("万有引力常数：\n"+str(G)+'\n步长t:\n'+str(t)+"\n绿色小球质量：\n"+str(m1)+'\n绿色小球初始位置x，y：\n'+str(x1)+'\n'+str(y1)+'\n绿色小球初始分速度Vx，Vy：\n'+str(v1_x)+'\n'+str(v1_y))
    f0.write("\n红色小球质量：\n"+str(m2)+'\n红色小球初始位置x，y：\n'+str(x2)+'\n'+str(y2)+'\n红色小球初始分速度Vx，Vy：\n'+str(v2_x)+'\n'+str(v2_y))
    f0.write("\n蓝色小球质量：\n"+str(m3)+'\n蓝色小球初始位置x，y：\n'+str(x3)+'\n'+str(y3)+'\n蓝色小球初始分速度Vx，Vy：\n'+str(v3_x)+'\n'+str(v3_y)+'\n')
    f0.write("记录精度：\n"+str(wait_num))
    time_begin=time.time()
    write_num=0
    for i in range(runtime): # while True: # 无限循环用这个

        distance12 = np.sqrt((x1-x2)**2+(y1-y2)**2) # 物体1和物体2之间的距离

        distance13 = np.sqrt((x1-x3)**2+(y1-y3)**2) # 物体1和物体3之间的距离

        distance23 = np.sqrt((x2-x3)**2+(y2-y3)**2) # 物体2和物体3之间的距离

        #对物体1的计算

        a1_2 = G*m2/(distance12**2) # 物体2对物体1的加速度(用上万有引力公式)

        a1_3 = G*m3/(distance13**2) # 物体3对物体1的加速度

        a1_x = a1_2*(x2-x1)/distance12 + a1_3*(x3-x1)/distance13 # 物体1受到的水平加速度

        a1_y = a1_2*(y2-y1)/distance12 + a1_3*(y3-y1)/distance13 # 物体1受到的垂直加速度

        v1_x = v1_x + a1_x*t # 物体1的速度

        v1_y = v1_y + a1_y*t # 物体1的速度

        x1 = x1 + v1_x*t # 物体1的水平位置

        y1 = y1 + v1_y*t # 物体1的垂直位置

        
        # 对物体2的计算

        a2_1 = G*m1/(distance12**2)

        a2_3 = G*m3/(distance23**2)

        a2_x = a2_1*(x1-x2)/distance12 + a2_3*(x3-x2)/distance23

        a2_y = a2_1*(y1-y2)/distance12 + a2_3*(y3-y2)/distance23

        v2_x = v2_x + a2_x*t

        v2_y = v2_y + a2_y*t

        x2 = x2 + v2_x*t

        y2 = y2 + v2_y*t

        

        # 对物体3的计算

        a3_1 = G*m1/(distance13**2)

        a3_2 = G*m2/(distance23**2)

        a3_x = a3_1*(x1-x3)/distance13 + a3_2*(x2-x3)/distance23

        a3_y = a3_1*(y1-y3)/distance13 + a3_2*(y2-y3)/distance23

        v3_x = v3_x + a3_x*t

        v3_y = v3_y + a3_y*t

        x3 = x3 + v3_x*t

        y3 = y3 + v3_y*t
        
        
    #记录数据进入文件
        write_num=write_num+1
        if write_num==wait_num:
            write_num=0
            f1.write(str(x1)+'\n')
            f1.write(str(y1)+'\n')
            
            f1.write(str(x2)+'\n')
            f1.write(str(y2)+'\n')
            
            f1.write(str(x3)+'\n')
            f1.write(str(y3)+'\n')
            
            print(f1.read())
        if i==runtime-1:#最后记录速度和坐标
            
            f2.write(str(x1)+'\n')
            f2.write(str(y1)+'\n')
            f2.write(str(x2)+'\n')
            f2.write(str(y2)+'\n')  
            f2.write(str(x3)+'\n')
            f2.write(str(y3)+'\n')
            f2.write(str(v1_x)+'\n') 
            f2.write(str(v1_y)+'\n')
            f2.write(str(v2_x)+'\n')
            f2.write(str(v2_y)+'\n')
            f2.write(str(v3_x)+'\n')
            f2.write(str(v3_y)+'\n')
            f2.write(str(m1)+'\n')
            f2.write(str(m2)+'\n')
            f2.write(str(m3)+'\n')
            f2.write(str(G)+'\n')
            f2.write(str(t)+'\n')

            time_end=time.time()
            print(f2.read())
            if (time_end-time_begin)>0:
                print('计算'+str(runtime)+'次用时：'+str(time_end-time_begin)+'s\n平均一秒计算：'+str(runtime/(time_end-time_begin))+'次')
            f0.close()
            f1.close()
            f2.close()

def run2():#接着运算
    global f_num1,name,f,e_runtime,e_file
    
    f=open(e_file.get()+'\\threebody1.txt', mode='a+')
    f2=open(e_file.get()+'\\threebody2.txt', mode='r+')
    
    runtime=int(e_runtime.get())#只有计算次数和记录精度可以改变
    wait_num=float(e_waittime.get())
    
    
    x1=float(f2.readline())
    y1=float(f2.readline())
    x2=float(f2.readline())
    y2=float(f2.readline())
    x3=float(f2.readline())
    y3=float(f2.readline())
    v1_x=float(f2.readline())
    v1_y=float(f2.readline())
    v2_x=float(f2.readline())
    v2_y=float(f2.readline())
    v3_x=float(f2.readline())
    v3_y=float(f2.readline())
    m1=float(f2.readline())
    m2=float(f2.readline())
    m3=float(f2.readline())
    G=float(f2.readline())
    t=float(f2.readline())#精度
    f2.close
    f2=open(e_file.get()+'\\threebody2.txt', mode='w+')
    
    

    time_begin=time.time()
    write_num=0
    
    
    for i in range(runtime): # while True: # 无限循环用这个

        distance12 = np.sqrt((x1-x2)**2+(y1-y2)**2) # 物体1和物体2之间的距离

        distance13 = np.sqrt((x1-x3)**2+(y1-y3)**2) # 物体1和物体3之间的距离

        distance23 = np.sqrt((x2-x3)**2+(y2-y3)**2) # 物体2和物体3之间的距离

        #对物体1的计算

        a1_2 = G*m2/(distance12**2) # 物体2对物体1的加速度(用上万有引力公式)

        a1_3 = G*m3/(distance13**2) # 物体3对物体1的加速度

        a1_x = a1_2*(x2-x1)/distance12 + a1_3*(x3-x1)/distance13 # 物体1受到的水平加速度

        a1_y = a1_2*(y2-y1)/distance12 + a1_3*(y3-y1)/distance13 # 物体1受到的垂直加速度

        v1_x = v1_x + a1_x*t # 物体1的速度

        v1_y = v1_y + a1_y*t # 物体1的速度

        x1 = x1 + v1_x*t # 物体1的水平位置

        y1 = y1 + v1_y*t # 物体1的垂直位置

        
        # 对物体2的计算

        a2_1 = G*m1/(distance12**2)

        a2_3 = G*m3/(distance23**2)

        a2_x = a2_1*(x1-x2)/distance12 + a2_3*(x3-x2)/distance23

        a2_y = a2_1*(y1-y2)/distance12 + a2_3*(y3-y2)/distance23

        v2_x = v2_x + a2_x*t

        v2_y = v2_y + a2_y*t

        x2 = x2 + v2_x*t

        y2 = y2 + v2_y*t

        

        # 对物体3的计算

        a3_1 = G*m1/(distance13**2)

        a3_2 = G*m2/(distance23**2)

        a3_x = a3_1*(x1-x3)/distance13 + a3_2*(x2-x3)/distance23

        a3_y = a3_1*(y1-y3)/distance13 + a3_2*(y2-y3)/distance23

        v3_x = v3_x + a3_x*t

        v3_y = v3_y + a3_y*t

        x3 = x3 + v3_x*t

        y3 = y3 + v3_y*t
        distance12 = np.sqrt((x1-x2)**2+(y1-y2)**2) # 物体1和物体2之间的距离

        distance13 = np.sqrt((x1-x3)**2+(y1-y3)**2) # 物体1和物体3之间的距离

        distance23 = np.sqrt((x2-x3)**2+(y2-y3)**2) # 物体2和物体3之间的距离

        #对物体1的计算

        a1_2 = G*m2/(distance12**2) # 物体2对物体1的加速度(用上万有引力公式)

        a1_3 = G*m3/(distance13**2) # 物体3对物体1的加速度

        a1_x = a1_2*(x2-x1)/distance12 + a1_3*(x3-x1)/distance13 # 物体1受到的水平加速度

        a1_y = a1_2*(y2-y1)/distance12 + a1_3*(y3-y1)/distance13 # 物体1受到的垂直加速度

        v1_x = v1_x + a1_x*t # 物体1的速度

        v1_y = v1_y + a1_y*t # 物体1的速度

        x1 = x1 + v1_x*t # 物体1的水平位置

        y1 = y1 + v1_y*t # 物体1的垂直位置

        
        # 对物体2的计算

        a2_1 = G*m1/(distance12**2)

        a2_3 = G*m3/(distance23**2)

        a2_x = a2_1*(x1-x2)/distance12 + a2_3*(x3-x2)/distance23

        a2_y = a2_1*(y1-y2)/distance12 + a2_3*(y3-y2)/distance23

        v2_x = v2_x + a2_x*t

        v2_y = v2_y + a2_y*t

        x2 = x2 + v2_x*t

        y2 = y2 + v2_y*t

        

        # 对物体3的计算

        a3_1 = G*m1/(distance13**2)

        a3_2 = G*m2/(distance23**2)

        a3_x = a3_1*(x1-x3)/distance13 + a3_2*(x2-x3)/distance23

        a3_y = a3_1*(y1-y3)/distance13 + a3_2*(y2-y3)/distance23

        v3_x = v3_x + a3_x*t

        v3_y = v3_y + a3_y*t

        x3 = x3 + v3_x*t

        y3 = y3 + v3_y*t
        
    #记录数据进入文件
        write_num=write_num+1
        if write_num==wait_num:
            write_num=0
            f.write(str(x1)+"\n")
            f.write(str(y1)+"\n")
            
            f.write(str(x2)+"\n")
            f.write(str(y2)+"\n")
            
            f.write(str(x3)+"\n")
            f.write(str(y3)+"\n")
            
            print(f.read())
        if i==runtime-1:#最后记录速度和坐标
            
            f2.write(str(x1)+"\n")
            f2.write(str(y1)+"\n")
            f2.write(str(x2)+"\n")
            f2.write(str(y2)+"\n")  
            f2.write(str(x3)+"\n")
            f2.write(str(y3)+"\n")
            f2.write(str(v1_x)+"\n") 
            f2.write(str(v1_y)+"\n")
            f2.write(str(v2_x)+"\n")
            f2.write(str(v2_y)+"\n")
            f2.write(str(v3_x)+"\n")
            f2.write(str(v3_y)+"\n")
            f2.write(str(m1)+'\n')
            f2.write(str(m2)+'\n')
            f2.write(str(m3)+'\n')
            f2.write(str(G)+'\n')
            f2.write(str(t))

            time_end=time.time()
            print(f2.read())
            if (time_end-time_begin)>0:
                print('计算'+str(runtime)+'次用时：'+str(time_end-time_begin)+'s\n平均一秒计算：'+str(runtime/(time_end-time_begin))+'次')
            f.close()
            f2.close()
            
def read():#查看最终结果
    global observation_max,e_file
    f1=open(e_file.get()+'\\threebody1.txt', mode='r')
    plt.ion() # 开启交互模式（重点）

    observation_max = 100 # 观测坐标范围初始值
    
    
    lines=f1.readlines()
    x1_all = [] # 轨迹初始值

    y1_all = []

    x2_all = []

    y2_all = []

    x3_all = []

    y3_all = []
    ii=0
    while True:
        ii=ii+1
        if ii%6==1:
            x1=float(lines[ii-1])
            x1_all = np.append(x1_all, x1)
            
        if ii%6==2:
            y1=float(lines[ii-1])
            y1_all = np.append(y1_all, y1) 
            
        if ii%6==3:
            x2=float(lines[ii-1])
            x2_all = np.append(x2_all, x2)
            
        if ii%6==4:

            y2=float(lines[ii-1])
            y2_all = np.append(y2_all, y2) 
            
        if ii%6==5:

        
            x3=float(lines[ii-1])
            x3_all = np.append(x3_all, x3)
            
        if ii%6==0:

        
            y3=float(lines[ii-1])
            y3_all = np.append(y3_all, y3)
            
        if ii==len(lines):
            break
    


    plt.plot(x1, y1, 'og', markersize=10) #设置物体大小

    plt.plot(x2, y2, 'or', markersize=10)

    plt.plot(x3, y3, 'ob', markersize=10)

    plt.plot(x1_all, y1_all, '-g') # 画轨迹

    plt.plot(x2_all, y2_all, '-r')

    plt.plot(x3_all, y3_all, '-b')

    axis_x= np.mean([x1, x2, x3]) # 观测坐标中心固定在平均值的地方

    axis_y = np.mean([y1, y2, y3]) # 观测坐标中心固定在平均值的地方
    while True:

        if np.abs(x1-axis_x) > observation_max or np.abs(x2-axis_x) > observation_max or np.abs(x3-axis_x) > observation_max or np.abs(y1-axis_y) > observation_max or np.abs(y2-axis_y) > observation_max or np.abs(y3-axis_y) > observation_max:

            observation_max = observation_max * 2 # 有一个物体超出视线时，坐标翻倍

        elif np.abs(x1-axis_x) < observation_max/10 and np.abs(x2-axis_x) < observation_max/10 and np.abs(x3-axis_x) < observation_max/10 and np.abs(y1-axis_y) < observation_max/10 and np.abs(y2-axis_y) < observation_max/10 and np.abs(y3-axis_y) < observation_max/10:

            observation_max = observation_max / 2 # 所有物体都在的视线的10分之一内，坐标减半

        else:

            break
    plt.axis([axis_x-observation_max, axis_x+observation_max, axis_y-observation_max, axis_y+observation_max])
    

    

    

    plt.show() # 显示图像
    f1.close()
   
    #plt.pause(0.001) # 暂停0.00001，防止画图过快

    

    #plt.clf() # 清空(重点)
    #if np.mod(i, 1000) == 0:

        #plt.savefig('three-body/'+str(i)+'.jpg') # 保存为图片可以用来做动画

        #plt.clf() # 清空

def read1():#查看过程结果
    global observation_max,e_file,x1,y1,x2,y2,x3,y3
    f1=open(e_file.get()+'\\threebody1.txt', mode='r')
    plt.ion() # 开启交互模式（重点）

    observation_max = 100 # 观测坐标范围初始值
    
    
    lines=f1.readlines()
    x1_all = [] # 轨迹初始值

    y1_all = []

    x2_all = []

    y2_all = []

    x3_all = []

    y3_all = []
    ii=0
    while True:
        ii=ii+1
        if ii%6==1:
            x1=float(lines[ii-1])
            x1_all = np.append(x1_all, x1)
            
        if ii%6==2:
            y1=float(lines[ii-1])
            y1_all = np.append(y1_all, y1) 
            
        if ii%6==3:
            x2=float(lines[ii-1])
            x2_all = np.append(x2_all, x2)
            
        if ii%6==4:

            y2=float(lines[ii-1])
            y2_all = np.append(y2_all, y2) 
            
        if ii%6==5:

        
            x3=float(lines[ii-1])
            x3_all = np.append(x3_all, x3)
            
        if ii%6==0:
            y3=float(lines[ii-1])
            y3_all = np.append(y3_all, y3)
            plt.plot(x1, y1, 'og', markersize=10) #设置物体大小

            plt.plot(x2, y2, 'or', markersize=10)

            plt.plot(x3, y3, 'ob', markersize=10)

            plt.plot(x1_all, y1_all, '-g') # 画轨迹

            plt.plot(x2_all, y2_all, '-r')

            plt.plot(x3_all, y3_all, '-b')

            axis_x= np.mean([x1, x2, x3]) # 观测坐标中心固定在平均值的地方

            axis_y = np.mean([y1, y2, y3]) # 观测坐标中心固定在平均值的地方
            while True:

                if np.abs(x1-axis_x) > observation_max or np.abs(x2-axis_x) > observation_max or np.abs(x3-axis_x) > observation_max or np.abs(y1-axis_y) > observation_max or np.abs(y2-axis_y) > observation_max or np.abs(y3-axis_y) > observation_max:

                    observation_max = observation_max * 2 # 有一个物体超出视线时，坐标翻倍

                elif np.abs(x1-axis_x) < observation_max/10 and np.abs(x2-axis_x) < observation_max/10 and np.abs(x3-axis_x) < observation_max/10 and np.abs(y1-axis_y) < observation_max/10 and np.abs(y2-axis_y) < observation_max/10 and np.abs(y3-axis_y) < observation_max/10:

                    observation_max = observation_max / 2 # 所有物体都在的视线的10分之一内，坐标减半

                else:

                    break
            plt.axis([axis_x-observation_max, axis_x+observation_max, axis_y-observation_max, axis_y+observation_max])
            plt.show() # 显示图像
            plt.pause(0.001) # 暂停0.00001，防止画图过快
            if ii!=len(lines):
                plt.clf() # 清空(重点)
            
        if ii==len(lines):
            break
    f1.close()

def import1():#导入初始数值
    global e_file,mr_m1,window
    f0=open(e_file.get()+'\\threebody0.txt', mode='r')
    f0.readline()
    G=float(f0.readline())
    f0.readline()
    t=float(f0.readline())
    f0.readline()
    m1=float(f0.readline())
    f0.readline()
    x1=float(f0.readline())
    y1=float(f0.readline())
    f0.readline()
    v1_x=float(f0.readline())
    v1_y=float(f0.readline())
    f0.readline()
    m2=float(f0.readline())
    f0.readline()
    x2=float(f0.readline())
    y2=float(f0.readline())
    f0.readline()
    v2_x=float(f0.readline())
    v2_y=float(f0.readline())
    f0.readline()
    m3=float(f0.readline())
    f0.readline()
    x3=float(f0.readline())
    y3=float(f0.readline())
    f0.readline()
    v3_x=float(f0.readline())
    v3_y=float(f0.readline())
    f0.readline()
    wait_num=float(f0.readline())
    f0.close()
    window.destroy()

    global f_num1,name,f,e_m1,e_m2,e_m3,e_t,e_v1x,e_v2x,e_v3x,e_v1y,e_v2y,e_v3y,e_G,e_x1,e_x2,e_x3,e_y1,e_y2,e_y3,e_waittime,write_num,e_runtime
    window=tk.Tk()
    window.title("Threebody")
    window.geometry('500x600')
    b_now=tk.Button(window,text="全新的计算",width=15,height=2,command=run1)
    b_now.place(x=5,y=530)
    b_keep=tk.Button(window,text="接着算",width=10,height=2,command=run2)
    b_keep.place(x=130,y=530)
    b_read=tk.Button(window,text="查看最终结果",width=10,height=2,command=read)
    b_read.place(x=225,y=530)
    b_read1=tk.Button(window,text="查看过程结果",width=10,height=2,command=read1)
    b_read1.place(x=315,y=530)
    b_import1=tk.Button(window,text="导入初始数值",width=10,height=2,command=import1)
    b_import1.place(x=410,y=530)

    
    mr_m1=tk.StringVar(value=m1)#设置默认
    e_m1=tk.Entry(window,show=None,width=10,textvariable=mr_m1)
    e_m1.place(x=85,y=15)
    mr_m2=tk.StringVar(value=m2)
    e_m2=tk.Entry(window,show=None,width=10,textvariable=mr_m2)
    e_m2.place(x=250,y=15)
    mr_m3=tk.StringVar(value=m3)
    e_m3=tk.Entry(window,show=None,width=10,textvariable=mr_m3)
    e_m3.place(x=420,y=15)

    mr_v1x=tk.StringVar(value=v1_x)
    e_v1x=tk.Entry(window,show=None,width=12,textvariable=mr_v1x)
    e_v1x.place(x=115,y=45)
    mr_v1y=tk.StringVar(value=v1_y)
    e_v1y=tk.Entry(window,show=None,width=12,textvariable=mr_v1y)
    e_v1y.place(x=115,y=95)
    mr_v2x=tk.StringVar(value=v2_x)
    e_v2x=tk.Entry(window,show=None,width=12,textvariable=mr_v2x)
    e_v2x.place(x=115,y=145)
    mr_v2y=tk.StringVar(value=v2_y)
    e_v2y=tk.Entry(window,show=None,width=12,textvariable=mr_v2y)
    e_v2y.place(x=115,y=195)
    mr_v3x=tk.StringVar(value=v3_x)
    e_v3x=tk.Entry(window,show=None,width=12,textvariable=mr_v3x)
    e_v3x.place(x=115,y=245)
    mr_v3y=tk.StringVar(value=v3_y)
    e_v3y=tk.Entry(window,show=None,width=12,textvariable=mr_v3y)
    e_v3y.place(x=115,y=295)

    mr_x1=tk.StringVar(value=x1)
    e_x1=tk.Entry(window,show=None,width=12,textvariable=mr_x1)
    e_x1.place(x=315,y=45)
    mr_y1=tk.StringVar(value=y1)
    e_y1=tk.Entry(window,show=None,width=12,textvariable=mr_y1)
    e_y1.place(x=315,y=95)
    mr_x2=tk.StringVar(value=x2)
    e_x2=tk.Entry(window,show=None,width=12,textvariable=mr_x2)
    e_x2.place(x=315,y=145)
    mr_y2=tk.StringVar(value=y2)
    e_y2=tk.Entry(window,show=None,width=12,textvariable=mr_y2)
    e_y2.place(x=315,y=195)
    mr_x3=tk.StringVar(value=x3)
    e_x3=tk.Entry(window,show=None,width=12,textvariable=mr_x3)
    e_x3.place(x=315,y=245)
    mr_y3=tk.StringVar(value=y3)
    e_y3=tk.Entry(window,show=None,width=12,textvariable=mr_y3)
    e_y3.place(x=315,y=295)

    mr_G=tk.StringVar(value=G)
    e_G=tk.Entry(window,show=None,width=12,textvariable=mr_G)
    e_G.place(x=115,y=345)
    mr_t=tk.StringVar(value=t)
    e_t=tk.Entry(window,show=None,width=12,textvariable=mr_t)
    e_t.place(x=115,y=395)
    mr_runtime=tk.StringVar(value=50000)
    e_runtime=tk.Entry(window,show=None,width=12,textvariable=mr_runtime)
    e_runtime.place(x=315,y=345)
    mr_waittime=tk.StringVar(value=wait_num)
    e_waittime=tk.Entry(window,show=None,width=12,textvariable=mr_waittime)
    e_waittime.place(x=315,y=395)
    mr_file=tk.StringVar(value='C:\\Users\\'+name+'\\Desktop\\threebody\\threebody0')
    e_file=tk.Entry(window,show=None,width=53,textvariable=mr_file)
    e_file.place(x=115,y=445)

    l_m1=tk.Label(window,text="绿球的质量：",width=10,height=2)
    l_m1.place(x=10,y=5)
    l_m2=tk.Label(window,text="红球的质量：",width=10,height=2)
    l_m2.place(x=175,y=5)
    l_m3=tk.Label(window,text="蓝球的质量：",width=10,height=2)
    l_m3.place(x=345,y=5)
    l_v1x=tk.Label(window,text="绿球x轴分速度：",width=15,height=2)
    l_v1x.place(x=0,y=35)
    l_v1y=tk.Label(window,text="绿球y轴分速度：",width=15,height=2)
    l_v1y.place(x=0,y=85)
    l_v2x=tk.Label(window,text="红球x轴分速度：",width=15,height=2)
    l_v2x.place(x=0,y=135)
    l_v2y=tk.Label(window,text="红球y轴分速度：",width=15,height=2)
    l_v2y.place(x=0,y=185)
    l_v3x=tk.Label(window,text="蓝球x轴分速度：",width=15,height=2)
    l_v3x.place(x=0,y=235)
    l_v3y=tk.Label(window,text="蓝球y轴分速度：",width=15,height=2)
    l_v3y.place(x=0,y=285)


    l_x1=tk.Label(window,text="绿球x轴坐标：",width=15,height=2)
    l_x1.place(x=200,y=35)
    l_y1=tk.Label(window,text="绿球y轴坐标：",width=15,height=2)
    l_y1.place(x=200,y=85)
    l_x2=tk.Label(window,text="红球x轴坐标：",width=15,height=2)
    l_x2.place(x=200,y=135)
    l_y2=tk.Label(window,text="红球y轴坐标：",width=15,height=2)
    l_y2.place(x=200,y=185)
    l_x3=tk.Label(window,text="蓝球x轴坐标：",width=15,height=2)
    l_x3.place(x=200,y=235)
    l_y3=tk.Label(window,text="蓝球y轴坐标：",width=15,height=2)
    l_y3.place(x=200,y=285)

    l_t=tk.Label(window,text="步长：",width=15,height=2)
    l_t.place(x=0,y=385)
    l_G=tk.Label(window,text="万有引力常数：",width=15,height=2)
    l_G.place(x=0,y=335)
    l_runtime=tk.Label(window,text="计算次数：",width=15,height=2)
    l_runtime.place(x=200,y=335)
    l_waittime=tk.Label(window,text="记录精度：",width=15,height=2)
    l_waittime.place(x=200,y=385)
    l_file=tk.Label(window,text="输入文件夹路径：",width=15,height=2)
    l_file.place(x=0,y=435)

    window.mainloop()
    
if __name__=='__main__':
    window()