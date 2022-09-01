import tkinter as tk
from suite_2csv import *

def get_filepath():
    file_path=textExample.get("1.0","end-1c")
    # btnRead['text'] = 'ing'
    lbl.config(text = "Successfully file made in path.")
    # btnRead['state'] = tk.DISABLED
    result = get_xlsx(file_path)
    if result:
        btnRead['text'] = 'Done!'
        btnRead['state'] = tk.ACTIVE
        btnRead['command'] = killer

def killer():
    exit()

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("400x240")
    root.title('suite -> xlsx')

    label = tk.Label(root, text='Enter the export file path :', font=20)
    label.pack()

    textExample=tk.Text(root, height=10)
    textExample.pack()

    btnRead=tk.Button(root, height=1, text="then I will make you a xlsx file", font=20,command=get_filepath)
    btnRead.pack()

    # # Label Creation
    lbl = tk.Label(root, text = "")
    lbl.pack()

    root.mainloop()
