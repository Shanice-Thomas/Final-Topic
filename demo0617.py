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
<<<<<<< HEAD
window.geometry("550x500")
window.config(bg="#C2C287")


btn1 = Button(window, text="100", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("100"))
btn1.grid(row=0, column=0, sticky=EW)
btn2 = Button(window, text="101", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("101"))
btn2.grid(row=0, column=1, sticky=EW)
btn3 = Button(window, text="102", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("102"))
btn3.grid(row=0, column=2, sticky=EW)
btn4 = Button(window, text="103", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("103"))
btn4.grid(row=0, column=3, sticky=EW)
btn5 = Button(window, text="104", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("104"))
btn5.grid(row=0, column=4, sticky=EW)

btn6 = Button(window, text="105", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("105"))
btn6.grid(row=1, column=0, sticky=EW)
btn7 = Button(window, text="106", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("106"))
btn7.grid(row=1, column=1, sticky=EW)
btn8 = Button(window, text="107", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("107")) 
btn8.grid(row=1, column=2, sticky=EW)
btn9 = Button(window, text="108", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:plot("108"))
btn9.grid(row=1, column=3, sticky=EW)
btn10 = Button(window, text="109", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:plot("109"))
btn10.grid(row=1, column=4, sticky=EW)

=======
window.geometry("500x500")
plot_button = Button(window, text = "Plot", command = lambda:plot("105"))
  
plot_button.pack()
>>>>>>> 077e5fbbee978df63b0e3ed63f9b243ee1ebf4df
window.mainloop()



<<<<<<< HEAD
=======






>>>>>>> 077e5fbbee978df63b0e3ed63f9b243ee1ebf4df
