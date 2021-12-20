import tkinter as tk

print ('HelloWorld tkinter')

root = tk.Tk() # メインウィンドウ
root.title('My First App')

def btn_click():
    #text1 = textbox.get("1.0","end")
    text1 = textbox.get('1.0', 'end -1c')
    print(text1)
    print('ボタンがクリックされました')
    
root.geometry('640x480') # メインウィンドウのサイズ

btn2 = tk.Button(root, text = '犬ボタン', command=btn_click).grid(row= 0, column=2)
btn3 = tk.Button(root, text = '牛ボタン').grid(row= 0, column=3)

textbox = tk.Text(width= 90, height= 1)
textbox.grid(row= 0, column=4)
textbox.insert('1.0', '赤い猫のエサ場')

btn4 = tk.Button(root, text = '山羊ボタン').grid(row= 1, column=2)
btn5 = tk.Button(root, text = '獅子ボタン').grid(row= 1, column=3)
btn6 = tk.Button(root, text = 'ヤンバルテナガコガネボタン').grid(row= 1, column=4)

root.mainloop() # ウィンドウを表示
