import tkinter as tk
from tkinter import filedialog


root = tk.Tk() # メインウィンドウ
root.title('tkinterのファイル選択ダイアログ')

def btn_click():
    idir = 'C:\\'
    file = tk.filedialog.askopenfile(initialdir = idir)
    if file:
        fn = file.name
        textbox.delete('1.0', 'end') # テキストボックスのクリア
        textbox.insert('1.0', fn)
        print(fn)
    

root.geometry('480x180')

btn = tk.Button(root, text = 'フォルダ選択', command=btn_click)
btn.grid(row= 0, column=1)

textbox = tk.Text(width= 90, height= 2)
textbox.grid(row= 0, column=2)
textbox.insert('1.0', 'ファイルパス')

root.mainloop() 
