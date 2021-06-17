import requests
from tkinter import *
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def answer(year):
    for i in range(1,13):
        deadlist.append(int(dead(day(year,i))))
        hurtlist.append(int(hurt(day(year,i))))
        print(str(year)+"年"+str(i)+"月"+"-->"+"死亡人數:"+str(deadlist[i-1])+","+"受傷人數(100單位):"+str(hurtlist[i-1]))

def plot(year):
    plot1.clear()
    answer(year)
    month = range(1, 13)
    plot1.plot(month, deadlist, color = 'red', marker='o', linestyle = '--', label='dead')
    plot1.plot(month, hurtlist, color = 'orange', marker='.', linestyle = '-', label='hurt')
    canvas.draw()

deadlist = []
hurtlist = []

window = Tk()
window.title("tkinter and matplotlib")

fig = Figure(figsize = (5, 4), dpi = 100)# 創建畫布
plot1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master = window)  
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
plot_button100 = Button(window, text = "100", command = lambda:plot("100")).pack(side=LEFT, fill=None, expand=1)
plot_button101 = Button(window, text = "101", command = lambda:plot("101")).pack(side=LEFT, fill=None, expand=1)
plot_button102 = Button(window, text = "102", command = lambda:plot("102")).pack(side=LEFT, fill=None, expand=0.5)
plot_button103 = Button(window, text = "103", command = lambda:plot("103")).pack(side=LEFT, fill=None, expand=0.5)
plot_button104 = Button(window, text = "104", command = lambda:plot("104")).pack(side=LEFT, fill=None, expand=0.5)
plot_button105 = Button(window, text = "105", command = lambda:plot("105")).pack(side=LEFT, fill=None, expand=0.5)
plot_button106 = Button(window, text = "106", command = lambda:plot("106")).pack(side=LEFT, fill=None, expand=0.5)
plot_button107 = Button(window, text = "107", command = lambda:plot("107")).pack(side=LEFT, fill=None, expand=0.5)
plot_button108 = Button(window, text = "108", command = lambda:plot("108")).pack(side=LEFT, fill=None, expand=0.5)
plot_button109 = Button(window, text = "109", command = lambda:plot("109")).pack(side=LEFT, fill=None, expand=0.5)

plot_button_Exit = Button(window, text = "Exit", command = window.destroy).pack(side=BOTTOM, fill=BOTH, expand=1)
window.mainloop()









