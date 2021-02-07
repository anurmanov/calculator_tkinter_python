import math
import functools
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def slice_n_calc_factorial(nums, d=1000):
    """Функция рекурсивно делит список чисел на подсписки по d элементов в каждом,
    перемножает элементы подсписков и в итоге вычисляет итоговый факториал"""
    if len(nums) > d:
        i = 1
        j = 1
        l = list()
        x = 0
        while (i < len(nums)):
            i=j*d
            l.append(nums[i-d:i])
            j+=1
        factorials = [functools.reduce(lambda x,y: x*y, i) for i in l]
        return slice_n_calc_factorial(factorials)
    return functools.reduce(lambda x,y: x*y, nums)

def my_factorial(n):
    """Генерирует список чисел от 1 до n и отдает его рекурсивной функции slice_n_calc_factorial"""
    nums = (list(range(n)) + [n])[1:]
    return slice_n_calc_factorial(nums)

def calc():
    e_result.delete('1.0', tk.END)
    e_result.insert(tk.INSERT, 'Вычисляю...')
    oper = str(operation.get())
    d1 = int(e1.get())
    if oper != '!':
        d2 = int(e2.get())
    if oper == '+':
        text = str(d1 + d2)
    elif oper == '-':
        text = str(d1 - d2)
    elif oper == '*':
        text = str(d1 * d2)
    elif oper == '/':
        text = str(d1 / d2)
    elif oper == '^':
        res = 1
        d1
        for i in range(d2):
            res*=d1
        text = str(res)
    elif oper == '!':
        #text = str(my_factorial(d1))
        text = str(math.factorial(d1))
    e_result.delete('1.0', tk.END)
    #результат записываем в result.txt
    res_file = open('result.txt', 'w')
    res_file.write(text)
    res_file.close()
    #если длина числа больше 1000 символов, то результат не отображаем
    if len(text) > 1000:
        e_result.insert(tk.INSERT, 'Результат сохранен в файле result.txt')
        messagebox.showinfo(title='Информация', message='Результат сохранен в файле result.txt')
    else:
        e_result.insert(tk.INSERT, text)

oper_names = [('+', '+'),  ('-', '-'), ('*', '*'), ('/', '/'), ('^', '^'), ('!  (факториал 1-го аргумента)', '!')]

root = tk.Tk()
root.title('Calculator')
frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl1 = tk.Label(frame, text='Первый аргумент :')
lbl1.pack(side=tk.LEFT)
e1 = tk.Entry(frame, width=30)
e1.pack(side=tk.LEFT)

operation = tk.StringVar()

frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl2 = tk.Label(frame, text='Операция :')
lbl2.pack(side=tk.LEFT)
frameForOps = tk.Frame(frame)
frameForOps.pack(side=tk.LEFT)
for oper_name, val in oper_names:
    r = tk.Radiobutton(frameForOps, text=oper_name, padx = 20, variable=operation, value=val)
    r.pack(side=tk.LEFT)
    r.select()

frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl3 = tk.Label(frame, text='Второй аргумент :')
lbl3.pack(side=tk.LEFT)
e2 = tk.Entry(frame, width=30)
e2.pack(side=tk.LEFT)

b = tk.Button(text='   calc   ', command=calc)
b.pack(anchor=tk.W)
frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl3 = tk.Label(frame, text='Результат :')
lbl3.pack(side=tk.LEFT)
e_result = ScrolledText(frame, width=150)
e_result.pack(side=tk.LEFT)
root.mainloop()
