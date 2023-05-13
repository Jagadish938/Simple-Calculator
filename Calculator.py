import tkinter as tk
# from tkinter import *

OFF_WHITE="#F8FAFF"

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
# def backspace():
#     global calculation
#     calculation=""
#     numLen=len(text_result.get())
#     text_result.delete(numLen -1,"end")
#     if numLen == 1:
#         text_result.insert(0,"0")
def backspace_pressed(event=None):
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)



root= tk.Tk()
root.title("Simple Calculator")
root.geometry("500x400")
root.resizable(False,False)
root.configure(bg="#17161b")
text_result=tk.Text(root,height=2,width=30,font=("Arial",24))
text_result.grid(columnspan=30)

btn_1=tk.Button(root,text="1",command=lambda: add_to_calculation(1),width=8,font=("Arial",14))
btn_1.grid(row=2,column=1)
btn_2=tk.Button(root,text="2",command=lambda: add_to_calculation(2),width=8,font=("Arial",14))
btn_2.grid(row=2,column=2)
btn_3=tk.Button(root,text="3",command=lambda: add_to_calculation(3),width=8,font=("Arial",14))
btn_3.grid(row=2,column=3)
btn_4=tk.Button(root,text="4",command=lambda: add_to_calculation(4),width=8,font=("Arial",14))
btn_4.grid(row=3,column=1)
btn_5=tk.Button(root,text="5",command=lambda: add_to_calculation(5),width=8,font=("Arial",14))
btn_5.grid(row=3,column=2)
btn_6=tk.Button(root,text="6",command=lambda: add_to_calculation(6),width=8,font=("Arial",14))
btn_6.grid(row=3,column=3)
btn_7=tk.Button(root,text="7",command=lambda: add_to_calculation(7),width=8,font=("Arial",14))
btn_7.grid(row=4,column=1)
btn_8=tk.Button(root,text="8",command=lambda: add_to_calculation(8),width=8,font=("Arial",14))
btn_8.grid(row=4,column=2)
btn_9=tk.Button(root,text="9",command=lambda: add_to_calculation(9),width=8,font=("Arial",14))
btn_9.grid(row=4,column=3)
btn_0=tk.Button(root,text="0",command=lambda: add_to_calculation(0),width=8,font=("Arial",14))
btn_0.grid(row=5,column=1)
btn_plus=tk.Button(root,text="+",command=lambda: add_to_calculation("+"),width=8,font=("Arial",14))
btn_plus.grid(row=2,column=4)
btn_minus=tk.Button(root,text="-",command=lambda: add_to_calculation("-"),width=8,font=("Arial",14))
btn_minus.grid(row=3,column=4)
btn_mul=tk.Button(root,text="*",command=lambda: add_to_calculation("*"),width=8,font=("Arial",14))
btn_mul.grid(row=4,column=4)
btn_div=tk.Button(root,text="/",command=lambda: add_to_calculation("/"),width=8,font=("Arial",14))
btn_div.grid(row=5,column=4)
btn_open=tk.Button(root,text="(",command=lambda: add_to_calculation("("),width=8,font=("Arial",14))
btn_open.grid(row=5,column=2)
btn_close=tk.Button(root,text=")",command=lambda: add_to_calculation(")"),width=8,font=("Arial",14))
btn_close.grid(row=5,column=3)
btn_equals=tk.Button(root,text="=",command= evaluate_calculation,width=16,height=2,bg=OFF_WHITE,font=("Arial",14))
btn_equals.grid(row=6,column=3,columnspan=2)
btn_clear=tk.Button(root,text="c",command=clear_field,width=16,height=2,font=("Arial",14))
btn_clear.grid(row=6,column=1,columnspan=2)
btn_backspace=tk.Button(root,text="←",command=backspace_pressed,width=6,height=1,font=("Arial",14))
btn_backspace.grid(row=1,column=4,columnspan=1)
root.mainloop()
