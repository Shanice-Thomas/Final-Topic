import requests # 建立各種 HTTP 請求，從網頁伺服器上取得想要的資料
from tkinter import * # Python 內建的圖形使用者設計套件
from bs4 import BeautifulSoup # 解析網頁 HTML 碼，取出使用者有興趣的資料
from matplotlib import pyplot as plt # Python 的 2D 圖形包 (matplotlib) ; 包含一系列繪圖函數(pyplot)
from matplotlib.figure import Figure # 建立繪圖物件的模組
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # 嵌入 plots 到 tkinter

def day(y,m):
    url = "https://168.motc.gov.tw/countrydeadhurt/%E8%87%BA%E4%B8%AD%E5%B8%82?"+"y="+str(y)+"&m="+str(m) # 交通部網址
    return url # 回傳網址

def dead(url): 
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml') 
    result0 = soup.find_all('script') 
    data = result0[2].string.split('''"''')
    return data[3] # 回傳死亡人數

def hurt(url): 
    req = requests.get(url) 
    soup = BeautifulSoup(req.text, 'lxml') 
    result0 = soup.find_all('script')
    data = result0[2].string
    data = data.replace(",","")
    data = data.split('''"''')
    data[7] = float(data[7])/100 # 因為受傷人數和死亡人數差距太大，圖表上顯示效果不佳，所以把受傷人數/100
    return data[7] # 回傳受傷人數

def answer(year):
    for i in range(1,13):
        deadlist.append(int(dead(day(year,i)))) 
        hurtlist.append(int(hurt(day(year,i))))
        print(str(year)+"年"+str(i)+"月"+"-->"+"死亡人數:"+str(deadlist[i-1])+","+"受傷人數(100單位):"+str(hurtlist[i-1]))

def plot(year):    
    answer(year)
    month = range(1, 13)
    plot1.plot(month, deadlist, color = 'red', marker='o', linestyle = '--', label = 'dead')
    plot1.plot(month, hurtlist, color = 'orange', marker='.', linestyle = '-', label = 'hurt')
    canvas.draw()

def clear():
    plot1.clear()
    deadlist.clear()
    hurtlist.clear()

deadlist = []
hurtlist = []

window = Tk()
window.title("tkinter and matplotlib")
window.geometry("450x450")
window.config(bg="#C2C287")
window.resizable(0, 0)

fig = Figure(figsize = (5, 4)) # 創建畫布 (寬, 高)
plot1 = fig.add_subplot(1, 1, 1) # 1 * 1 網格 第1個子圖 

canvas = FigureCanvasTkAgg(fig, master = window)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
plot_button100 = Button(window, text = "100", command = lambda:plot("100")).pack(side=LEFT, fill=BOTH) 
plot_button101 = Button(window, text = "101", command = lambda:plot("101")).pack(side=LEFT, fill=BOTH)
plot_button102 = Button(window, text = "102", command = lambda:plot("102")).pack(side=LEFT, fill=BOTH)
plot_button103 = Button(window, text = "103", command = lambda:plot("103")).pack(side=LEFT, fill=BOTH)
plot_button104 = Button(window, text = "104", command = lambda:plot("104")).pack(side=LEFT, fill=BOTH)
plot_button105 = Button(window, text = "105", command = lambda:plot("105")).pack(side=LEFT, fill=BOTH)
plot_button106 = Button(window, text = "106", command = lambda:plot("106")).pack(side=LEFT, fill=BOTH)
plot_button107 = Button(window, text = "107", command = lambda:plot("107")).pack(side=LEFT, fill=BOTH)
plot_button108 = Button(window, text = "108", command = lambda:plot("108")).pack(side=LEFT, fill=BOTH)
plot_button109 = Button(window, text = "109", command = lambda:plot("109")).pack(side=LEFT, fill=BOTH)

plot_button_Clear = Button(window, text="Clear", command = clear).pack(side=TOP, fill=BOTH)
plot_button_Exit = Button(window, text = "Exit", command = window.destroy).pack(side=BOTTOM, fill=BOTH)
window.mainloop()









