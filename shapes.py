from tkinter import *
from tkinter import ttk 

window = Tk()

window.title("Working on canvas using functions")
window.geometry("600x600")




startx = Label(window,text="startx")

starty = Label(window,text="starty")

choose_color_label = Label(window,text="Choose a colour")

endx = Label(window,text="endx")

endy = Label(window,text="endy")


start_y = ttk.Combobox(window)

color = ttk.Combobox(window)

start_x = ttk.Combobox(window)

end_x = ttk.Combobox(window)

end_y = ttk.Combobox(window)

start_x.place(relx=0.2, rely=0.85,anchor=CENTER)

starty.place( relx=0.3, rely=0.85,anchor=CENTER)

start_y.place(relx=0.4, rely=0.85,anchor=CENTER)

color.place(relx=0.8,rely=0.9,anchor=CENTER)

choose_color_label.place(relx=0.6,rely = 0.9,anchor=CENTER)

startx.place(relx=0.1,rely = 0.85,anchor=CENTER)

endx.place(relx=0.5, rely=0.85,anchor=CENTER)

end_x.place(relx=0.6, rely=0.85,anchor=CENTER)

end_y.place(relx=0.8, rely=0.85,anchor=CENTER)

endy.place(relx=0.7, rely=0.85,anchor=CENTER)



canvas = Canvas(window,width=990,height=490,bg="white",highlightbackground="gray")
canvas.pack()

my_image = canvas.create_image(50,50)

direction = ""

old_x = 50
old_y = 50

new_x = 50
new_y = 50


def right_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y

    old_x = new_x
    old_y = new_y

    new_x = new_x+5
    direction = "right"
    draw(direction,old_x,old_y,new_x,new_y)


def left_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y

    old_x = new_x
    old_y = new_y

    new_x = new_x-5
    direction = "left"
    draw(direction,old_x,old_y,new_x,new_y)


def up_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y

    old_x = new_x
    old_y = new_y

    new_y = new_y-5
    direction = "up"
    draw(direction,old_x,old_y,new_x,new_y)


def down_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y

    old_x = new_x
    old_y = new_y

    new_y = new_y+5
    direction = "down"
    draw(direction,old_x,old_y,new_x,new_y)


def draw(direction,old_x,old_y,new_x,new_y):
    fill_color = color.get()
    if(direction=="right"):
        right_line = canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)

    if(direction=="left"):
        left_line = canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)

    if(direction=="up"):
        up_line = canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color) 

    if(direction=="down"):
        down_line = canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)       


canvas.pack()

window.bind("<Right>",right_dir)
window.bind("<Left>",left_dir)
window.bind("<Up>",up_dir)
window.bind("<Down>",down_dir)

window.mainloop()