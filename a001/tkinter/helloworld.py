import tkinter as tk

print ('HelloWorld tkinter')

root = tk.Tk() # メインウィンドウ
root.title('My First App')

root.geometry('640x480') # メインウィンドウのサイズ

btn1 = tk.Button(root, text = '猫ボタン').pack()
btn2 = tk.Button(root, text = '犬ボタン').pack()

textbox = tk.Text(width= 90, height= 1).pack()

#frame1 = ttk.Frame(root, padding=16)

root.mainloop() # ウィンドウを表示
