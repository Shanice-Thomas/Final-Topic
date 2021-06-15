from tkinter import *
from typing import SupportsBytes

def changeText(num):
    if int(lab["text"]) != 0:
        lab["Text"] = lab["Text"] + num
    else:
        lab["Text"] = num

#def Addfun(num):
    #lab["Text"] = lab["Text"] + num
#def Subfun(num):
    #lab["Text"] = lab["Text"] - num
#def Mulfun(num):
    #lab["Text"] = lab["Text"] * num
#def Divfun(num):
    #lab["Text"] = lab["Text"] / num

window = Tk()
window.title("期末專題") 
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

btn1 = Button(window, text="100", command=lambda:爬蟲("100"))
btn1.grid(row=0, column=0, sticky=NSEW)
btn2 = Button(window, text="101", command=lambda:爬蟲("101"))
btn2.grid(row=1, column=0, sticky=NSEW)
btn3 = Button(window, text="102", command=lambda:爬蟲("102"))
btn3.grid(row=2, column=0, sticky=NSEW)
btn4 = Button(window, text="103", command=lambda:爬蟲("103"))
btn4.grid(row=3, column=0, sticky=NSEW)
btn5 = Button(window, text="104", command=lambda:爬蟲("104"))
btn5.grid(row=4, column=0, sticky=NSEW)

btn6 = Button(window, text="105", command=lambda:爬蟲("105"))
btn6.grid(row=0, column=1, sticky=NSEW)
btn7 = Button(window, text="106", command=lambda:爬蟲("106"))
btn7.grid(row=1, column=1, sticky=NSEW)
btn8 = Button(window, text="107", command=lambda:爬蟲("107")) 
btn8.grid(row=2, column=1, sticky=NSEW)
btn9 = Button(window, text="108", command=lambda:爬蟲("108"))
btn9.grid(row=3, column=1, sticky=NSEW)
btn10 = Button(window, text="109", command=lambda:爬蟲("109"))
btn10.grid(row=4, column=1, sticky=NSEW)

btn10 = Button(window, text="進入題目", command=lambda:爬蟲("110")) 
btn10.grid(row=5, column=0, columnspan=2, sticky=NSEW)

window.mainloop()