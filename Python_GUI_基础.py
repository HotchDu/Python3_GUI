import tkinter

def on_click():
	label['text'] = "No way out"

#编辑窗口各类属性
top = tkinter.Tk(className = "Hello World")
top.geometry('400x200+200+300') #分别是窗口的Size和初始位置，不可存在空格

#加上标签
label = tkinter.Label(top)
label['text'] = 'be on your own'
label.pack()

#加上按钮
button = tkinter.Button(top)
button['text'] = 'Ok'

#添加按键事件操作
button['command'] = on_click
button.pack()

#添加可编辑文本框
text = tkinter.StringVar()
text.set('Change to what?')
entry = tkinter.Entry(top)
entry['textvariable'] = text
entry.pack()

#进入消息循环体 如何理解mainloop？ 
#进入到事件（消息）循环。一旦检测到事件，就刷新组件。
top.mainloop()