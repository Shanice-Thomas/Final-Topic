import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *

def day(y,m):
    url = "https://168.motc.gov.tw/countrydeadhurt/臺中市?%22+%22y=%22+str(y)+%22&m=%22+str(m)"
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
window.geometry("500x500")
plot_button = Button(window, text = "Plot", command = lambda:plot("105"))
  
plot_button.pack()
window.mainloop()