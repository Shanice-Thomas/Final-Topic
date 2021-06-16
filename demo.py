import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from tkinter import *

window = Tk()
window.title("Final Topic") 
window.geometry("900x900") 
window.config(bg="#C2C287")

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.columnconfigure(0, weight=1) 
window.columnconfigure(1, weight=1)

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
    return data[7]

deadlist = []
hurtlist = []

def answer(year):
    for i in range(1,13):
        deadlist.append(int(dead(day(year,i))))
        hurtlist.append(int(hurt(day(year,i))))
        print(str(year)+"年"+str(i)+"月"+"-->"+"死亡人數:"+str(deadlist[i-1])+","+"受傷人數:"+str(hurtlist[i-1]))



btn1 = Button(window, text="100", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:answer("100"))
btn1.grid(row=0, column=0, sticky=NSEW)
btn2 = Button(window, text="101", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:answer("101"))
btn2.grid(row=1, column=0, sticky=NSEW)
btn3 = Button(window, text="102", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:answer("102"))
btn3.grid(row=2, column=0, sticky=NSEW)
btn4 = Button(window, text="103", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:answer("103"))
btn4.grid(row=3, column=0, sticky=NSEW)
btn5 = Button(window, text="104", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:answer("104"))
btn5.grid(row=4, column=0, sticky=NSEW)

btn6 = Button(window, text="105", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:answer("105"))
btn6.grid(row=0, column=1, sticky=NSEW)
btn7 = Button(window, text="106", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:answer("106"))
btn7.grid(row=1, column=1, sticky=NSEW)
btn8 = Button(window, text="107", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:answer("107")) 
btn8.grid(row=2, column=1, sticky=NSEW)
btn9 = Button(window, text="108", bg="#4DFFFF", font=("Helvetica 25 bold"), command=lambda:answer("108"))
btn9.grid(row=3, column=1, sticky=NSEW)
btn10 = Button(window, text="109", bg="#FFFF37", font=("Helvetica 25 bold"), command=lambda:answer("109"))
btn10.grid(row=4, column=1, sticky=NSEW)

btnExit = Button(window, text="Exit", bg="#FF8040", font=("Helvetica 25 bold"), command=window.destroy)
btnExit.grid(row=5, column=0, columnspan=2, sticky=NSEW)

window.mainloop()