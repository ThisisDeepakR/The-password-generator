#password Generator
from random import *
from tkinter import *
x='abcdef#ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
p=''

def make(p):
	try:
		n=e1.get()
		n=int(n)
		for i in range(n):
			p=p+choice(x)
		t1.insert(END,p+'\n')
	except ValueError as e:
		t1.insert(END,'Enter Value,M getting ValueError ;)\n')
	

window=Tk()
window.title('The password Generator')
l1=Label(text='The Password Generator',bg='red',fg='white',font=('Roboto',20))
l1.pack(fill=X)
l2=Label(text='How much length you required?',fg='brown',font=('Times',12))
l2.pack()
e1=Entry()
e1.pack()
b1=Button(text='Generate',bg='brown',fg='white',command=lambda :make(p))
b1.pack()
t1=Text(font=('Times',20),height=10)
t1.pack()
l3=Label(text='By Deepak R',font=('Times',22),fg='brown')
l3.pack()
window.geometry('500x500')
window.mainloop()