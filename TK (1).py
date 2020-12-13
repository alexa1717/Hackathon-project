from tkinter import *
from tkinter.font import *

global path
global a


def get_values():
    a=list()
    a.append(x.get())
    a.append(y.get())
    
def show_path():
    print (a)

master = Tk()
master.title("Emergency Services")
master.state('zoomed')

canvas = Canvas(master, width= 850, height= 650)
img = PhotoImage(file="Map.ppm")
canvas.create_image(0,0,anchor=NW, image=img)
canvas.place(x=10, y=25)

Label(master, text="Accident Co-ordinates:", font= Font(family="Lucida Grande", size=15)).place(x=1020, y=100)
Label(master, text="X:", font= Font(family="Lucida Grande", size=12)).place(x=980, y=130)
Label(master, text="Y:", font= Font(family="Lucida Grande", size=12)).place(x=1130, y=130)

x = Entry(master)
y = Entry(master)
x.place(x=1000, y=132)
y.place(x=1160, y=132)

Button(master, text='Submit', command= lambda: get_values()).place(x=1050, y=160)
Button(master, text='Show Path', command= lambda: show_path()).place(x=1150, y=160)

Label(master, text="Hospital Co-ordinates:", font= Font(family="Lucida Grande", size=15)).place(x=1020, y=200)
Label(master, text="X: 558", font= Font(family="Lucida Grande", size=12)).place(x=980, y=230)
Label(master, text="Y: 285", font= Font(family="Lucida Grande", size=12)).place(x=1120, y=230)

msg = "\tLEGEND\t\n\nT\tTraffic-Signals\t\nH\tHospital\t\nA\tAmbulance\t\nX\tAccident-Spot\t\n----\tPath\t\n"
legend = Message(master, text = msg)
legend.config(bg='white', font=('times', 14), justify='left', width=500)
legend.place(x=1000, y=380)

mainloop()