
import tkinter as tk
from tkinter import messagebox
from typing import Text
import datetime as dt
from tkinter import ttk
from tkinter import *

rt=tk.Tk()
rt.geometry("600x300")
rt.title('Currency Converter') 

#Title label
tk.Label(rt, text='INR to international converter', font='arial 20 bold').pack()
w = tk.Label(rt, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 10)).place(x=490,y=270)
#Second Label
tk.Label(rt, text='Enter amount',font='arial 15').place(x=225,y=50)

#First entry feild 
entry_field = tk.Entry(rt ,width ='50')
entry_field.place(x=150,y=80)
Msg=tk.StringVar()
Msg2=tk.StringVar()
Msg3=tk.StringVar()
Msg4=tk.StringVar()

#Second Label
tk.Label(rt, text='US Doller',font='arial 10').place(x=20,y=110)

#First Output feild
feild=tk.Entry(rt, textvariable = Msg ,width =25)
feild.place(x=20,y=140)

#Third Label
tk.Label(rt, text='Canadian Doller',font='arial 10').place(x=20,y=175)

#Second Output feild
E3=tk.Entry(rt,textvariable= Msg2,width=25)
E3.place(x=20,y=200)

#Fourth Label
tk.Label(rt, text='Euro',font='arial 10').place(x=330,y=110)

#Third Output
E4=tk.Entry(rt,textvariable= Msg3,width=25)
E4.place(x=330,y=135)

#Fifth Label
tk.Label(rt, text='Russian Ruble',font='arial 10').place(x=330,y=170)

#fourth Output
E5=tk.Entry(rt,textvariable= Msg4,width=25)
E5.place(x=330,y=195)

#Function to convert USD from INR
def us_change():
    amount=entry_field.get()
    if amount== '':
        messagebox.showerror('Converter','Please Enter amount')
    else:
        amount=int(amount)
        usd=amount*0.014
        feild.insert(0,usd)
        
#Function to convert CAD from INR
def cad_change():
    amt=entry_field.get()
    amt=int(amt)
    cad=amt*0.017
    E3.insert(0,cad)

#Function to convert EUR from INR
def eur_change():
    amte=entry_field.get()
    amte=int(amte)
    eur=amte*0.012
    E4.insert(0,eur)

#Function to convert RUB from INR
def rus_change():
    amtr=entry_field.get()
    amtr=int(amtr)
    rus=amtr*0.96
    E5.insert(0,rus)

#Clears all entry feilds
def clear():
    entry_field.delete(0, 'end')
    feild.delete(0, 'end')
    E3.delete(0, 'end')
    E4.delete(0, 'end')
    E5.delete(0, 'end')

#Performs exit task 
def closing():
    rt.destroy()

#Button to convert usd from inr
do=tk.Button(rt, text='Convert',command=us_change,bg='red')
do.place(x=120,y=113)

#Button to convert cad from inr
do_cad=tk.Button(rt, text='convert',command=cad_change,bg='red')
do_cad.place(x=120,y=173)

#Button to convert eur from inr
do_eur=tk.Button(rt, text='convert',command=eur_change,bg='red')
do_eur.place(x=430,y=108)

#Button to convert rub from inr
do_rub=tk.Button(rt, text='convert',command=rus_change,bg='red')
do_rub.place(x=430,y=168)

#Clear button
clearB=tk.Button(rt, text='Clear', command=clear, bg='cyan2')
clearB.place(x=90,y=240)

#Exit Buttton
exit=tk.Button(rt, text='Exit',command=closing,bg='orange2',width='20')
exit.place(x=230,y=250)

#Starting GUI
rt.mainloop()