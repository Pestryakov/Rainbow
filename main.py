from tkinter import *

root = Tk()
root.title('GUI')
root.iconbitmap('python.ico')

l = Label(root, text='Сlick on the color!')
e = Entry(root, width=70, justify='center')

l.pack()
e.pack()

colors = {
    "#ff0000": "Red",
    "#ff7d00": "Orange",
    "#ffff00": "Yellow",
    "#00ff00": "Green",
    "#007dff": "Blue",
    "#0000ff": "DarkBlue",
    "#7d00ff": "Purple",
}

for k, v in colors.items():
    Button(root, bg=k, command=lambda text=v, hex=k: get_color(text, hex)).pack(fill=X)

def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)

# def color_red():
#     l['text'] = 'Red'
#     e.delete(0, END)
#     e.insert(0, '#ff0000')
#
#
# def color_orange():
#     l['text'] = 'Orange'
#     e.delete(0, END)
#     e.insert(0, '#ff7d00')
#
#
# def color_yellow():
#     l['text'] = 'Yellow'
#     e.delete(0, END)
#     e.insert(0, '#ffff00')
#
#
# def color_green():
#     l['text'] = 'Green'
#     e.delete(0, END)
#     e.insert(0, '#00ff00')
#
#
# def color_blue():
#     l['text'] = 'Blue'
#     e.delete(0, END)
#     e.insert(0, '#007dff')
#
#
# def color_darkblue():
#     l['text'] = 'DarkBlue'
#     e.delete(0, END)
#     e.insert(0, '#0000ff')
#
#
# def color_purple():
#     l['text'] = 'Purple'
#     e.delete(0, END)
#     e.insert(0, '7d00ff')

#btn_red = Button(root, bg="#ff0000", command = color_red).pack(file=X)
btn_red = Button(root, bg='#ff0000', command=lambda: get_color('Red', '#ff0000')).pack(fill=X)
btn_orange = Button(root, bg='#ff7d00', command=lambda: get_color('Orange', '#ff7d00')).pack(fill=X)
btn_yellow = Button(root, bg='#ffff00', command=lambda: get_color('Yellow', '#ffff00')).pack(fill=X)
btn_green = Button(root, bg='#00ff00', command=lambda: get_color('Green', '#00ff00')).pack(fill=X)
btn_blue = Button(root, bg='#007dff', command=lambda: get_color('Blue', '007dff')).pack(fill=X)
btn_darkblue = Button(root, bg='#0000ff', command=lambda: get_color('DarkBlue', '#0000ff')).pack(fill=X)
btn_purple = Button(root, bg='#7d00ff', command=lambda: get_color('Purple', '#7d00ff')).pack(fill=X)

root.mainloop()
