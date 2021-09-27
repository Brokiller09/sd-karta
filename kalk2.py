from tkinter import *
def add_digit(digit):
      e.insert(9000000,digit)  
      
      
def comconfig():
     value=e.get()
     e.delete(0,END)
     a=e.insert(0,eval(value))
  
         

     
kl=Tk()
kl["bg"]="#089"

kl.title("Калькулятор")
e=Entry(kl, width=40,font="Times 30",fg="#119")
e.place(y=740,x=15,height=600)
la=Label(text="КАЛЬКУЛЯТОР",bg="#099",bd=0,font=" Times 15",fg="red")
la.pack()
b1=Button(text="1",bd=13,command=lambda:add_digit(1), width=8,height=1)
b1.place(y=90)

b2=Button(text="2",bd=13,command=lambda:add_digit(2), width=8,height=1)
b2.place(y=90,x=380)
b3=Button(text="3",bd=13,command=lambda:add_digit(3), width=8,height=1)
b3.place(y=90,x=750)
b4=Button(text="4",bd=13,command=lambda:add_digit(4), width=8,height=1)
b4.place(y=220)
b5=Button(text="5",bd=13,command=lambda:add_digit(5), width=8,height=1)
b5.place(y=220,x=380)
b6=Button(text="6",bd=13,command=lambda:add_digit(6), width=8,height=1)
b6.place(x=750,y=220)
b7=Button(text="7",bd=13,command=lambda:add_digit(7), width=8,height=1)
b7.place(y=350)
b8=Button(text="8",bd=13,command=lambda:add_digit(8), width=8,height=1)
b8.place(y=350,x=380)
b9=Button(text="9",bd=13,command=lambda:add_digit(9), width=8,height=1)
b9.place(y=350,x=750)
b0=Button(text="0",bd=13,command=lambda:add_digit(0), width=8,height=1)
b0.place(y=480)
b10=Button(text="=",bd=13,font="Times 38",command=comconfig, width=8,height=1)
b10.place(y=1380, x=10)
b20=Button(text="×",bd=13,command=lambda:add_digit("*"), width=8,height=1)
b20.place(x=750,y=480)
b30=Button(text=":",bd=15,command=lambda:add_digit("/"), width=8,height=1)
b30.place(y=480,x=380)
b40=Button(text="-",bd=15,command=lambda:add_digit("-"), width=8,height=1)
b40.place(y=610)
b50=Button(text="+",bd=15,command=lambda:add_digit("+"), width=8,height=1)
b50.place(y=610,x=380)
b50=Button(text="DELETE",bg="red",bd=15,command=lambda:e.delete(0,END), width=8,height=1)
b50.place(y=610,x=750)
b60=Button(text="<--",bg="blue",bd=2,command=exit,)
b60.place(x=0)
kl.update()
kl.mainloop()
