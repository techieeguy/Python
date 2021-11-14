from tkinter import *   #pip install tkinter
from datetime import date   #pip install datetime

root=Tk()    
root.title("Age Calculator")   
root.configure(bg="#eeeeee")   
root.geometry("340x400")    
new=Label(root,bg="#5f5f5f")  
new.grid(row=5,column=0,columnspan=3)

today=str(date.today())   
list_today=today.split("-")  
#defining a function to calcutate age
def age(b_date,b_month,b_year):
    global today
    global new
    new.grid_forget()
    b_date=int(entry_date.get())
    b_month=int(entry_month.get())
    b_year=int(entry_year.get())
    c_date=int(list_today[2])
    c_month=int(list_today[1])
    c_year=int(list_today[0])
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(b_date>c_date):
        c_month=c_month-1
        c_date=c_date+month[b_month-1]
    if (b_month>c_month):
        c_year=c_year-1
        c_month=c_month+12
    resultd=str(c_date-b_date)
    resultm=str(c_month-b_month)
    resulty=str(c_year-b_year)
    new=Label(root,text="Your Age is \n"+resulty+" Years "+resultm+" Months "+ resultd+" Days ",fg="#878298",bg="#eeeeee",borderwidth=6)
    new.config(font=("Arial Rounded MT Bold",15))
    new.grid(row=5,column=0,columnspan=3)

#defining a function to clear the previous entries
def clean(entry_date,entry_month,entry_year):
    global new
    new.grid_forget()
    entry_date.delete(0,END)
    entry_month.delete(0,END)
    entry_year.delete(0,END)

#creating widgets such as labels,entry boxes and buttons and fixing its position onto window    
title_label=Label(root,text="Age Calculator",borderwidth=10,fg="#5f5f5f",bg="#eeeeee")
title_label.config(font=("Arial Rounded MT Bold",29))
title_label.grid(row=0,column=0,columnspan=3)
label_date=Label(root,text="Enter Birth Date: ",borderwidth=4,fg="#878298",bg="#eeeeee")
label_date.config(font=("Arial Rounded MT Bold",15))
label_date.grid(row=1,column=0)
label_month=Label(root,text="Enter Birth Month: ",borderwidth=5,fg="#878298",bg="#eeeeee")
label_month.config(font=("Arial Rounded MT Bold",15))
label_month.grid(row=2,column=0)
label_year=Label(root,text="Enter Birth Year: ",borderwidth=9,fg="#878298",bg="#eeeeee")
label_year.config(font=("Arial Rounded MT Bold",15))
label_year.grid(row=3,column=0)

entry_date=Entry(root,width=20,borderwidth=3)
entry_month=Entry(root,width=20,borderwidth=3)
entry_year=Entry(root,width=20,borderwidth=3)

entry_date.grid(row=1,column=2)
entry_month.grid(row=2,column=2)
entry_year.grid(row=3,column=2)

b_date=entry_date.get()
b_month=entry_month.get()
b_year=entry_year.get()

submit=Button(root,text="Calculate Age",width=15,anchor=CENTER,command=lambda:age(b_date,b_month,b_year),bg="#6600CC",fg="#D5C6FF",borderwidth=5)
submit.grid(row=4,column=0)

clear=Button(root,text="Clear",width=10,command=lambda:clean(entry_date,entry_month,entry_year),bg="#6600CC",fg="#D5C6FF",borderwidth=5)
clear.grid(row=4,column=2)

root.mainloop()