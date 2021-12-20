import tkinter as tk
from tkinter import filedialog


root = tk.Tk() # メインウィンドウ
root.title('tkinterのフォルダ選択ダイアログ')

def btn_click():
    idir = 'C:\\'
    dir_path = tk.filedialog.askdirectory(initialdir = idir)
    textbox.delete('1.0', 'end') # テキストボックスのクリア
    textbox.insert('1.0', dir_path)
    print(dir_path)
    

root.geometry('480x180')

btn = tk.Button(root, text = 'フォルダ選択', command=btn_click)
btn.grid(row= 0, column=1)

textbox = tk.Text(width= 90, height= 2)
textbox.grid(row= 0, column=2)
textbox.insert('1.0', 'ディレクトリパス')

root.mainloop() 
