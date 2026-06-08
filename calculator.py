import tkinter as aps
root = aps.Tk()
root.geometry("300x350+550+100")
root.title("CALCULATOR")
input_text = aps.Entry(root,font=("Arial",20))
root["bg"] = "black"

def click(num):
    data = input_text.get()
    input_text.delete(0,aps.END)
    data = data + str(num)
    input_text.insert(0,data)

def clear():
    input_text.delete(0,aps.END)

def backspace_action():
    insert_index = input_text.index(aps.INSERT)
    
    if insert_index > 0:
        input_text.delete(insert_index - 1)

def calculate():
    expression = input_text.get()
    result = eval(expression)
    input_text.delete(0,aps.END)
    input_text.insert(0,result)

seven = aps.Button(root,text="7",font=("Arial",15),command=lambda:click(7),)
eight = aps.Button(root,text="8",font=("Arial",15),command=lambda:click(8))
nine= aps.Button(root,text="9",font=("Arial",15),command=lambda:click(9))
div = aps.Button(root,text="/",font=("Arial",15),command=lambda:click("/"),bg="orange")

four = aps.Button(root,text="4",font=("Arial",15),command=lambda:click(4))
five = aps.Button(root,text="5",font=("Arial",15),command=lambda:click(5))
six = aps.Button(root,text="6",font=("Arial",15),command=lambda:click(6))
multiply= aps.Button(root,text="X",font=("Arial",15),command=lambda:click("*"),bg="orange")

one = aps.Button(root,text="1",font=("Arial",15),command=lambda:click(1))
two = aps.Button(root,text="2",font=("Arial",15),command=lambda:click(2))
three= aps.Button(root,text="3",font=("Arial",15),command=lambda:click(3))
minus= aps.Button(root,text="-",font=("Arial",15),command=lambda:click("-"),bg="orange")

plus= aps.Button(root,text="+",font=("Arial",15),command=lambda:click("+"),bg="orange")
zero= aps.Button(root,text="0",font=("Arial",15),command=lambda:click(0))
c = aps.Button(root,text="C",font=("Arial",15),command= clear)
result= aps.Button(root,text="=",font=("Arial",15),command=calculate,bg="yellow")

modulus = aps.Button(root,text="%",font=("Arial",15),command=lambda:click("%"),bg="orange")
back_space= aps.Button(root,text="DEL",font=("Arial",10),command=backspace_action,bg="orange")
dot = aps.Button(root,text=".",font=("Arial",15),command= lambda:click("."),bg="orange")
square= aps.Button(root,text="^",font=("Arial",15),command=lambda:click("**"),bg="orange")

input_text.grid(row=0,column=0,columnspan=4,ipady=10)

seven.grid(row=2,column=0,ipadx=15,ipady=5,padx=4,pady=4)
eight.grid(row=2,column=1,ipadx=15,ipady=5,padx=4,pady=4)
nine.grid(row=2,column=2,ipadx=15,ipady=5,padx=4,pady=4)
div.grid(row=2,column=3,ipadx=18,ipady=5,padx=4,pady=4)

four.grid(row=3,column=0,ipadx=15,ipady=5,padx=4,pady=4)
five.grid(row=3,column=1,ipadx=15,ipady=5,padx=4,pady=4)
six.grid(row=3,column=2,ipadx=15,ipady=5,padx=4,pady=4)
multiply.grid(row=3,column=3,ipadx=15,ipady=5,padx=4,pady=4)

one.grid(row=4,column=0,ipadx=15,ipady=5,padx=4,pady=4)
two.grid(row=4,column=1,ipadx=15,ipady=5,padx=4,pady=4)
three.grid(row=4,column=2,ipadx=15,ipady=5,padx=4,pady=4)
minus.grid(row=4,column=3,ipadx=17,ipady=5,padx=4,pady=4)

zero.grid(row=5,column=1,ipadx=15,ipady=5,padx=4,pady=4)
c.grid(row=5,column=0,ipadx=15,ipady=5,padx=4,pady=4)
result.grid(row=5,column=2,ipadx=15,ipady=5,padx=4,pady=4)
plus.grid(row=5,column=3,ipadx=15,ipady=5,padx=4,pady=4)

modulus.grid(row=1,column=1,ipadx=13,ipady=5,padx=4,pady=4)
back_space.grid(row=1,column=0,ipadx=15,ipady=5,padx=4,pady=4)
dot.grid(row=1,column=2,ipadx=17,ipady=5,padx=4,pady=4)
square.grid(row=1,column=3,ipadx=17,ipady=5,padx=4,pady=4)

root.mainloop()