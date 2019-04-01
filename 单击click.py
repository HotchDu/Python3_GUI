import tkinter

def on_click():
    print('hello world')

top=tkinter.Tk(className='hello world') 

#定义窗体的大小，是400X200像素 
top.geometry('400x200')

#加上按钮
button = tkinter.Button(top)
button['text'] = 'click'

#添加按钮操作 
button['command'] = on_click 
button.pack()

#进入消息循环体
top.mainloop()