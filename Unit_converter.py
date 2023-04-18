from tkinter import *
root = Tk()


l1 = Label(root,text='Simple Unit Conversion',fg='blue',font=('Comic Sans MS', '40'),padx=50)
l1.grid(row=0,column=0,columnspan=3,sticky=W+E)

l2 = Label(root,text='Select a system of units',fg='blue',font=('Comic Sans MS', '20'))
l2.grid(row=1,column=0,sticky=W)

l3 = Label(root,text='Select the units',fg='blue',font=('Comic Sans MS', '20'))
l3.grid(row=2,column=0,sticky=W)

l4 = Label(root,text='Please insert the values',fg='blue',font=('Comic Sans MS', '20'))
l4.grid(row=3,column=0,sticky=W)

def check(var):
    global unit,e1,e2,unit_var1,unit_var2
    if var=='Length':
        unit ={"meter": 1.0,"kilometer": 1000.0,"centimeter": 0.01,"millimeter": 0.001,"micrometer": 10**-6,"nanometer": 10**-9,"angstrom": 10**-10,"inch": 0.0254,"foot": 0.3048,"yard": 0.9144,"mile": 1609.34}
    elif var=='Mass':
        unit ={"gram": 1.0,"kilogram": 1000.0,"milligram": 0.001,"microgram": 10**-6,"pound": 453.592,"ounce": 28.3495,"tonne": 1000000}
    elif var=='Temperature':
        unit = {"kelvin": 1.0,"celsius": lambda x: x + 273.15,"fahrenheit": lambda x: (x + 459.67) * 5/9,}
    elif var=='Time':
        unit = {"second": 1.0,"millisecond": 0.001,"microsecond": 10**-6,"nanosecond": 10**-9,"minute": 60.0,"hour": 3600.0,"day": 86400.0,"week": 604800.0,"year": 31536000.0}
    elif var=='Data':
        unit = {"megabyte": 1.0,"gigabyte": 1000.0,"terabyte": 1000.0 ** 2,"petabyte": 1000.0 ** 3,"kilobyte": 1/1000.0,"byte": 1/1000.0 ** 2}    
    unit_var1 = StringVar()
    unit_var2 = StringVar()

    slide_2 = OptionMenu(root, unit_var1, *unit.keys(), command=units_check)
    slide_2.config(fg='Blue',  font=('Times', '20'), relief='solid',width=20,
                    highlightbackground='grey', highlightthickness=2)
    slide_2.grid(row=2, column=1, sticky=W + E)

    slide_3 = OptionMenu(root, unit_var2, *unit.keys(), command=units_check)
    slide_3.config(fg='Blue',  font=('Times', '20'), relief='solid',width=20,
                    highlightbackground='grey', highlightthickness=2)
    slide_3.grid(row=2, column=2, sticky=W + E)
    e1.delete(0,END)
    e2.config(text='')


    
def units_check(n):
    pass

def convert(n=None):
    from tkinter import messagebox
    u1 = unit_var1.get()
    u2 = unit_var2.get()
    if e1.get()=='':
        messagebox.showerror('Error', 'Please enter a value for unit conversion')
        return None
    elif u1=='' or u2=='':
            messagebox.showerror('Error', 'Please select  a unit for conversion')
            return None
    if system_var.get() != 'Temperature':
        u1 = unit.get(u1)
        u2 = unit.get(u2)
        uni = u1/u2
        ans = int(e1.get())*uni
        e2.config(text=ans)
    else:
        u1 = unit.get(u1)
        u1 = u1(int(e1.get()))
        if u2=='kelvin':
            e2.config(text=u1)   
        elif u2=='celsius':
            ans = u1-273.15
            e2.config(text=ans)
        elif u2=='fahrenheit':
            ans = (u1-273.15) * 9/5 + 32
            e2.config(text=ans)


def delete(n=None):
    e1.delete(0,END)
    e2.config(text='')


system = ['Length','Mass','Temperature','Time','Data']
system_var = StringVar()
system_var.set(system[0])

slide_1 = OptionMenu(root, system_var, *system, command=check)
slide_1.config(fg='Blue',  font=('Times', '20'), relief='solid',width=20,
                highlightbackground='grey', highlightthickness=2)
slide_1.grid(row=1, column=1, sticky=W + E, columnspan=2)

unit_var1 = StringVar()
unit_var2 = StringVar()
unit ={"meter": 1.0,"kilometer": 1000.0,"centimeter": 0.01,"millimeter": 0.001,"micrometer": 1e-6,"nanometer": 1e-9,"angstrom": 1e-10,"inch": 0.0254,"foot": 0.3048,"yard": 0.9144,"mile": 1609.34}
slide_2 = OptionMenu(root, unit_var1,*unit.keys(), command=units_check)
slide_2.config(fg='Blue',  font=('Times', '20'), relief='solid',width=20,
                highlightbackground='grey', highlightthickness=2)
slide_2.grid(row=2, column=1, sticky=W + E)

slide_3 = OptionMenu(root, unit_var2, *unit.keys(), command=units_check)
slide_3.config(fg='Blue',  font=('Times', '20'), relief='solid',width=20,
                highlightbackground='grey', highlightthickness=2)
slide_3.grid(row=2, column=2, sticky=W + E)

e1 =Entry(root, fg='blue', font=('Times', '20'), width=20, borderwidth=2,relief='solid',
          highlightbackground='grey', highlightthickness=2)
e1.grid(row=3,column=1,sticky=W+E)

e2 =Label(root, fg='blue', font=('Times', '20'), width=20, borderwidth=2,relief='solid',
          highlightbackground='grey', highlightthickness=2)
e2.grid(row=3,column=2,sticky=W+E)
b1 = Button(root, text='Convert', command=convert, fg='blue',  font=('Comic Sans MS', '20'),width=10,relief='solid',
                highlightbackground='grey', highlightthickness=2)
b1.grid(row=4,column=1,sticky=E)
b2 = Button(root, text='Reset', command=delete, fg='blue',  font=('Comic Sans MS', '20'),width=10,relief='solid',
                highlightbackground='grey', highlightthickness=2)
b2.grid(row=4,column=2,sticky=W)

root.bind('<Return>',convert)
root.bind('<Delete>',delete)
root.bind('<Escape>',lambda n:root.quit())

mainloop()