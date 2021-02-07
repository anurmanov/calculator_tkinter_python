import gmpy2
import inflect
import Tkinter as tk
import tkMessageBox
import ScrolledText

max_length_of_result = 21000000

def calc():
    e_result.delete('1.0', tk.END)
    e_result.insert(tk.INSERT, 'Calculating...')
    oper = str(operation.get())
    d1 = gmpy2.mpz(e1.get())
    if oper != '!':
        d2 = gmpy2.mpz(e2.get())
    if oper == '+':
        text = gmpy2.add(d1, d2).digits()
    elif oper == '-':
        text = gmpy2.sub(d1, d2).digits()
    elif oper == '*':
        text = gmpy2.mul(d1, d2).digits()
    elif oper == '/':
        text = (d1 / d2).digits()
    elif oper == '^':
        text = (d1**d2).digits()
    elif oper == '!':
        n = gmpy2.fac(d1)
        text = n.digits()
    len_text = len(text)
    #only first 21 million digits of result will be save to file
    if len_text > max_length_of_result:
        text = text[:max_length_of_result]
    res_file = open('result.txt', 'w')
    res_file.write(text)
    res_file.close()
    e_result.delete('1.0', tk.END)
    if len(text) > 1000:
        if len_text > max_length_of_result:
            p = inflect.engine()
            
            msg = 'Length of result text is ' + str(len_text) + '. Only first ' + p.number_to_words(max_length_of_result) + ' digits of the result of calculation was saved to the file "result.txt"'
        else:
            msg = 'Length of result text is ' + str(len_text) + '. The result of calculation was saved to the file "result.txt"'
        e_result.insert(tk.INSERT, msg)
        tkMessageBox.showinfo(title='Information', message=msg)
    else:
        e_result.insert(tk.INSERT, text)

oper_names = [('+', '+'),  ('-', '-'), ('*', '*'), ('/', '/'), ('^', '^'), ('!', '!')]

root = tk.Tk()
root.title('Calculator')
frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl1 = tk.Label(frame, text='First argument :')
lbl1.pack(side=tk.LEFT)
e1 = tk.Entry(frame, width=30)
e1.pack(side=tk.LEFT)

operation = tk.StringVar()

frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl2 = tk.Label(frame, text='Operation :')
lbl2.pack(side=tk.LEFT)
frameForOps = tk.Frame(frame)
frameForOps.pack(side=tk.LEFT)
for oper_name, val in oper_names:
    r = tk.Radiobutton(frameForOps, text=oper_name, padx = 20, variable=operation, value=val)
    r.pack(side=tk.LEFT)
    r.select()

frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl3 = tk.Label(frame, text='Second argument :')
lbl3.pack(side=tk.LEFT)
e2 = tk.Entry(frame, width=30)
e2.pack(side=tk.LEFT)

b = tk.Button(text='   calc   ', command=calc)
b.pack(anchor=tk.W)
frame = tk.Frame(root)
frame.pack(anchor=tk.W)
lbl3 = tk.Label(frame, text='Result :')
lbl3.pack(side=tk.LEFT)
e_result = ScrolledText.ScrolledText(frame, width=150)
e_result.pack(side=tk.LEFT)
root.mainloop()
