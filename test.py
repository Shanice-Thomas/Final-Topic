import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *

def day(y,m):
    url = "https://168.motc.gov.tw/countrydeadhurt/%E8%87%BA%E4%B8%AD%E5%B8%82?"+"y="+str(y)+"&m="+str(m)
    return url

def dead(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    result0 = soup.find_all('script')
    data = result0[2].string.split('''"''')
    return data[3]

def hurt(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    result0 = soup.find_all('script')
    data = result0[2].string
    data = data.replace(",","")
    data = data.split('''"''')
    data[7] = float(data[7])/100
    return data[7]

deadlist = []
hurtlist = []

def plot(year):
    fig = Figure(figsize = (5, 5), dpi = 100)# 創建畫布
    plot1 = fig.add_subplot(111)
    for i in range(1,13):
        deadlist.append(int(dead(day(year,i))))
        hurtlist.append(int(hurt(day(year,i))))
        print(str(year)+"年"+str(i)+"月"+"-->"+"死亡人數:"+str(deadlist[i-1])+","+"受傷人數(100單位):"+str(hurtlist[i-1]))
    month = range(1, 13)
    plot1.plot(month, deadlist, color = 'red', marker='o', linestyle = '--', label='dead')
    plot1.plot(month, hurtlist, color = 'orange', marker='.', linestyle = '-', label='hurt')
    plt.xlabel('month', color = 'blue')
    plt.ylabel('people', color = 'blue')
    plt.title('dead&hurt', color = 'blue')
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

window = Tk()
window.title('Plotting in Tkinter')
window.geometry("837x500")
window.config(bg="#C2C287")
window.resizable(0, 0)

frame1 = Frame(window)
frame1.grid(row=0, column=0)

btn1 = Button(frame1, text="100", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("100"))
btn1.pack(side='left')
btn2 = Button(frame1, text="101", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("101"))
btn2.pack(side='left')
btn3 = Button(frame1, text="102", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("102"))
btn3.pack(side='left')
btn4 = Button(frame1, text="103", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("103"))
btn4.pack(side='left')
btn5 = Button(frame1, text="104", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("104"))
btn5.pack(side='left')
btn6 = Button(frame1, text="105", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("105"))
btn6.pack(side='left')
btn7 = Button(frame1, text="106", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("106"))
btn7.pack(side='left')
btn8 = Button(frame1, text="107", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("107")) 
btn8.pack(side='left')
btn9 = Button(frame1, text="108", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("108"))
btn9.pack(side='left')
btn10 = Button(frame1, text="109", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("109"))
btn10.pack(side='left')

window.mainloop()