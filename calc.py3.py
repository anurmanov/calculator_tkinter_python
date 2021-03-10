"""
Tkinter calculator for big numbers
"""

import math
import functools
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

#Tkinter global binded variables.
#They are used for fetching the result, the arguments and operation type.
e_result = None
operation = None
e_arg1 = None
e_arg2 = None
#global dictionary for calculations
operations_dict = {'+': {'label': '+'},
                   '-': {'label': '-'},
                   '*': {'label': '*'},
                   '/': {'label': '/'},
                   '^': {'label': '^'},
                   '!': {'label': '!  (factorial of the 1st arg)'}}

def slice_n_calc_factorial(nums, d=1000):
    """
    Recursive function slices list of numbers on sublists (d items in each one),
    multiply items of sublists and return final factorial
    """
    if len(nums) > d:
        i = 1
        j = 1
        l = list()
        x = 0
        while (i < len(nums)):
            i = j * d
            l.append(nums[i-d:i])
            j += 1
        factorials = [functools.reduce(lambda x, y: x * y, i) for i in l]
        return slice_n_calc_factorial(factorials)
    return functools.reduce(lambda x, y: x * y, nums)

def my_factorial(n):
    nums = (list(range(n)) + [n])[1:]
    return slice_n_calc_factorial(nums)

def read_entry_argument(tkinter_entry):
    try:
        value = int(tkinter_entry.get())
    except:
        e_result.delete('1.0', tk.END)
        e_result.insert(tk.INSERT, 'Some arguments have bad format!')
        value = None
    return value
	
def init_calc_methods():
    """
    Add calculationg lambda functions to the each operation
    """
    operations_dict['+'].update(calc = lambda x, y: x + y)
    operations_dict['-'].update(calc = lambda x, y: x - y)
    operations_dict['*'].update(calc = lambda x, y: x * y)
    operations_dict['/'].update(calc = lambda x, y: x / y)
    operations_dict['^'].update(calc = lambda x, y: pow(x, y))
    operations_dict['!'].update(calc = lambda x, y: my_factorial(x))

def show_result(result_text):
    e_result.delete('1.0', tk.END)
    if len(result_text) > 1000:
        with open('result.txt', 'w') as res_file:
            res_file.write(result_text)
        e_result.insert(tk.INSERT, 'Result saved to result.txt')
        messagebox.showinfo(title='Information',
                            message='Result saved to result.txt')
    else:
        e_result.insert(tk.INSERT, result_text)
        
def start_calculation():
    """
    Main calculating function.
    Uses tkinter binded variables fetching for arguments, operation and result
    """
    show_result('Calculating...')
    oper = str(operation.get())
    arg1, arg2 = None, None
    arg1 = read_entry_argument(e_arg1)
    if not arg1:
        return
    #factorial operation ! uses just 1st argument
    if oper != '!':
        arg2 = read_entry_argument(e_arg2)
        if not arg2:
            return

    result = str(operations_dict[oper]['calc'](arg1, arg2))

    show_result(result)


def build_tkinter_interface():
    """
    Application form builder function
    """
    global e_result
    global operation
    global e_arg1
    global e_arg2
    
    #TK subsystem initializing
    root = tk.Tk()
    root.title('Calculator')
    
    #main window
    frame = tk.Frame(root)
    frame.pack(anchor=tk.W)
    
    #label "1st argument"
    lbl1 = tk.Label(frame, text='1st argument :')
    lbl1.pack(side=tk.LEFT)
    e_arg1 = tk.Entry(frame, width=30)
    e_arg1.pack(side=tk.LEFT)
    #binded variable
    operation = tk.StringVar()
    
    #label "Operation"
    frame = tk.Frame(root)
    frame.pack(anchor=tk.W)
    lbl2 = tk.Label(frame, text='Operation :')
    lbl2.pack(side=tk.LEFT)
    frameForOps = tk.Frame(frame)
    frameForOps.pack(side=tk.LEFT)
    for oper, value in operations_dict.items():
        r = tk.Radiobutton(frameForOps,
                           text=value['label'],
                           padx = 20,
                           variable=operation,
                           value=oper)
        r.pack(side=tk.LEFT)
        r.select()

    #label "2nd argument"
    frame = tk.Frame(root)
    frame.pack(anchor=tk.W)
    lbl3 = tk.Label(frame, text='2nd argument :')
    lbl3.pack(side=tk.LEFT)
    e_arg2 = tk.Entry(frame, width=30)
    e_arg2.pack(side=tk.LEFT)

    #button "calc"
    b = tk.Button(text='   calc   ', command=start_calculation)
    b.pack(anchor=tk.W)
    frame = tk.Frame(root)
    frame.pack(anchor=tk.W)
    
    #label "Result"
    lbl3 = tk.Label(frame, text='Result :')
    lbl3.pack(side=tk.LEFT)
    e_result = ScrolledText(frame, width=150)
    e_result.pack(side=tk.LEFT)
    #run Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    init_calc_methods()
    build_tkinter_interface()
