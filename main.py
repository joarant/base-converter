import tkinter as tk
from validator import validateNumberField, validateBase
from converter import convert

# https://www.rapidtables.com/convert/number/base-converter.html


window = tk.Tk()
window.geometry("500x500")
row = []

for i in range(11):
    row.append(i)

window.columnconfigure(row, weight=1, minsize=25)
window.rowconfigure(row, weight=1, minsize=25)



fromLabel = tk.Label(text="Enter number",)
fromLabel.grid(row=1,column=5,sticky="n")


fromInput = tk.Entry()
fromInput.grid(row=1,column=5,sticky="s")


base = tk.Label(text="From base")
base2 = tk.Label(text="To base")
base.grid(row=2,column=5,sticky="n")
base2.grid(row=3,column=5,sticky="n")

rLabel = tk.Label(text="Result:")
rLabel.grid(row=6,column=5,sticky="n")

result = tk.Entry(state="readonly")
result.grid(row=6,column=5,sticky="s")


baseFrom = tk.Entry(width=3)
baseFrom.grid(row=2,column=5,sticky="s")

baseTo = tk.Entry(width=3)
baseTo.grid(row=3,column=5,sticky="s")


reset = tk.Button(
    text="Reset",
    width=10,
    height=1,
)

calculate = tk.Button(
    text="Calculate",
    width=10,
    height=1,
)

reset.grid(row=4,column=5,sticky="s")
calculate.grid(row=5,column=5,sticky="s")



def validateFields():

    result.config(state="normal")
    result.delete(0, tk.END)
    result.config(state="readonly")

    if validateBase(baseFrom.get()) == False:
        baseFrom.config(background="#f55863")
        return False

    if validateBase(baseTo.get()) == False:
        baseTo.config(background="#f55863")

        return False

    if validateNumberField(fromInput.get(), baseFrom.get()) == False:
        fromInput.config(background="#f55863")

        return False
    
    baseFrom.config(background="#ffffff")
    baseTo.config(background="#ffffff")
    fromInput.config(background="#ffffff")

    
    return True

def calculateBaseSwitch():
    if validateFields():
        result.config(state="normal")
        result.delete(0, tk.END)
        result.insert(0,str(convert(fromInput.get(),int(baseFrom.get()),int(baseTo.get()))))
        result.config(state="readonly")

def resetFields():
    result.config(state="normal")
    result.delete(0, tk.END)
    result.config(state="readonly")
    fromInput.delete(0, tk.END)
    baseFrom.delete(0, tk.END)
    baseTo.delete(0, tk.END)


calculate['command']=calculateBaseSwitch
reset['command']=resetFields


window.mainloop()
