import tkinter
import  tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window=tkinter.Tk()
window.resizable()
window.title('BMI Calculator')
window.minsize(400,150)
frame=tkinter.Frame(window)
frame.pack()
window.eval('tk::PlaceWindow . center')

#clear
def clear():
    fntxt.delete(0,'end')
    Lntxt.delete(0,'end')
    wghttxt.delete(0,'end')
    hghttxt.delete(0,'end')

#showdata
def show_2():
    normal=0
    over=0
    under=0
    obese=0
    with open('BmiResults.csv','r') as file:
        csvreader=csv.reader(file)
        for row in csvreader:
            if(len(row)!=0):
                if(row[2]=='Overweight'):
                    over=over+1
                elif(row[2]=='Normal'):
                    normal=normal+1
                elif(row[2]=='Obese'):
                    obese=obese+1
                elif(row[2]=='underweight'):
                    under=under+1
        numbers = [over, obese,normal,under]
        label = ['Overweight','Obese', 'Normal', 'underweight']
        explode = (0.1, 0, 0, 0)
        fig, ax1 = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        ax1.pie(numbers, explode=explode, labels=label,
                shadow=True, startangle=90,
                autopct='%1.1f%%')
        ax1.axis('equal')
        canvas.draw()

#Save
def save(b):
        BMI=bmiinterpretor(b)
        firstname=fntxt.get()
        lastname=Lntxt.get()
        with open('BmiResults.csv','a')as filewriter:
            csvfilewriter=csv.writer(filewriter)
            csvfilewriter.writerow([firstname,lastname,BMI])
def bmiinterpretor(b):
    if(b>=40):
        result='Obese'
    elif(25<=b<=39.9):
        result='Overweight'
    elif(18.5<=b<24.9):
        result='Normal'
    elif b<=18.4:
        result='underweight'
    return result

#Calculatefunc:
def calculate():
    try:
     height=float(hghttxt.get())
     weight=int(wghttxt.get())
     firstname = fntxt.get()
     lastname = Lntxt.get()
     if (firstname == '' or lastname == ''):
         messagebox.showwarning(title='invalid input', message='Please fillout all fields')
     else:
        bmi = weight / (height ** 2)
        save(bmi)
    except ValueError:
        messagebox.showwarning(title="Invalid Input",message="Please enter valid input")
        hghttxt.delete(0,'end')
        wghttxt.delete(0,'end')

    messagebox.showinfo(title='result',message='You are '+ bmiinterpretor(bmi))
    clear()



infoframe=tkinter.LabelFrame(frame,text='Information')
infoframe.grid(row=0,column=0,padx=10)
#firstname
fnlable=tkinter.Label(infoframe,text='First name')
fnlable.grid(row=0,column=0,padx=10,pady=10)
fntxt=tkinter.Entry(infoframe)
fntxt.grid(row=0,column=1,padx=10,pady=10)
#lastname
Lnlable=tkinter.Label(infoframe,text='Last name')
Lnlable.grid(row=0,column=2,padx=10,pady=10)
Lntxt=tkinter.Entry(infoframe)
Lntxt.grid(row=0,column=3,padx=10,pady=10)
#weight
wghtlable=tkinter.Label(infoframe,text='Weight (kg.)')
wghtlable.grid(row=1,column=0,padx=10)
wghttxt=tkinter.Entry(infoframe)
wghttxt.grid(row=1,column=1,padx=10)
#height
hghtlable=tkinter.Label(infoframe,text='Height (m)')
hghtlable.grid(row=1,column=2,padx=10,pady=10)
hghttxt=tkinter.Entry(infoframe)
hghttxt.grid(row=1,column=3,padx=10,pady=10)
#Calculatebtn
calcbutton=tkinter.Button(infoframe,text='Calculate',command=calculate)
#calcbutton.place(x=200,y=110)
calcbutton.grid(row=4,column=1,pady=10)

#resultbutton
rsltbutton=tkinter.Button(infoframe,text='Result',command=show_2)
rsltbutton.grid(row=4,column=2,pady=10)
#rsltbutton.place(x=280,y=110)

window.mainloop()