from tkinter import *
from tkinter.font import *
from collections import defaultdict


Final_Path = list()
a = str()
h = '558,285'
graph =  defaultdict(list)
update = False
l = list()

"""def addEdge (graph: object, u: object, v: object) -> object:
    graph[u].append(v)

def generate_edges(graph):
    edges = []
    for node in graph:
         for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges"""


"""# declaration of graph as dictionary
addEdge(graph , '11,141' , '65,142')
addEdge(graph , '72,27' , '65,142')
addEdge(graph , '859,132' , '696,154')
addEdge(graph , '65,142' , '375,153')
addEdge(graph , '65,142' , '11,141')
addEdge(graph , '65,142' , '59,279')
addEdge(graph , '65,142' , '72,27')
addEdge(graph , '42,26' , '375,153')
addEdge(graph , '375,153' , '65,142')
addEdge(graph , '375,153' , '696,154')
addEdge(graph , '375,153' , '402,26')
addEdge(graph , '375,153' , '362,287')
addEdge(graph , '696,154' , '375,153')
addEdge(graph , '696,154' , '859,132')
addEdge(graph , '696,154' , '694,286')
addEdge(graph , '12,277' , '59,279')
addEdge(graph , '59,279' , '12,277')
addEdge(graph , '59,279' , '362,283')
addEdge(graph , '59,279' , '65,142')
addEdge(graph , '59,279' , '50,498')
addEdge(graph , '362,283' , '59,279')
addEdge(graph , '362,283' , '375,153')
addEdge(graph , '362,283' , '558,285')
addEdge(graph , '362,283' , '356,422')
addEdge(graph , '362,283' , '694,286')
addEdge(graph , '558,285' , '362,283')
addEdge(graph , '558,285' , '694,286')
addEdge(graph , '694,286' , '558,285' )
addEdge(graph , '694,286' , '696,154' )
addEdge(graph , '694,286' , '694,416' )
addEdge(graph , '356,422' , '362,283' )
addEdge(graph , '356,422' , '694,416' )
addEdge(graph , '356,422' , '350,561' )
addEdge(graph , '694,416' , '694,286' )
addEdge(graph , '694,416' , '847,464' )
addEdge(graph , '694,416' , '356,422' )
addEdge(graph , '350,561' , '59,279' )
addEdge(graph , '350,561' , '356,422' )
addEdge(graph , '350,561' , '349,581' )
addEdge(graph , '349,581' , '350,561' )
addEdge(graph , '559,581' , '847,464' )
addEdge(graph , '847,464' , '694,416' )
addEdge(graph , '847,464' , '347,664' )
addEdge(graph , '347,664' , '847,464' )
addEdge(graph , '347,664' , '350,561' )
addEdge(graph , '50,498' , '59,279')
addEdge(graph ,  '50,498' , '66,539')
addEdge(graph ,  '66,539' , '100,559')
addEdge(graph ,  '66,539' , '50,498' )
addEdge(graph ,  '100,559' , '66,539')
addEdge(graph ,  '100,559' , '350,561')"""


"""def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                     paths.append(newpath)
        return paths"""


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        try:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        except:
            continue
    return shortest

def get_values():
    global a, update
    update = False
    a = str()
    a = str(x.get())+','+str(y.get())
    return a

def process(b):
    global update
    for i in range(len(b)):
        b[i]=b[i].split(',')
        b[i][0], b[i][1] = int(b[i][0]), int(b[i][1])
    print(Final_Path)
    show_path()
    update = True

def process_path():
    global a, Final_Path
    Final_Path = find_shortest_path(graph, a, h)
    process(Final_Path)

def show_path():
    global Final_Path, l
    for i in range(len(Final_Path)):
        if i != len(Final_Path)-1:
            l.append(canvas.create_line(Final_Path[i][0], Final_Path[i][1], Final_Path[i+1][0], Final_Path[i+1][1], dash=(4, 2)))
    l.append(canvas.create_bitmap(Final_Path[0][0], Final_Path[0][1], bitmap="warning"))


def update_canvas():
    global update, l
    if update:
        for i in l:
            canvas.delete(i)


graph = { "11,141" : ["65,142"],
          "859,132": ["696,154"],
          "72,27" : ["65,142"],
          "65,142" : ["11,141" , "375,153" , "59,279" , "72,27"],
          "402,26" : ["375,153"],
          "375,153" : ["65,142", "696,154","402,26","362,283"],
          "696,154" : ["375,153","859,132","694,286"],
          "12,277": ["59,279"],
          "59,279": ["12,277","362,283","65,142","50,498"],
          "362,283": ["59,279","375,153","558,285","356,422","694,286"],
          "558,285": ["362,283","694,286"],
          "694,286" : ["558,285","696,154","694,416"],
          "356,422" : ["362,283", "694,416","350,561"],
          "694,416" : ["694,286","847,464","356,422"],
          "350,561": ["100,559","356,422","349,581"],
          "349,581" : ["350,561"],
          "559,581" : ["847,464"],
          "50,498" : ["66,539" , "59,279"],
          "66,539" : ["50,498" , "100,559"],
          "100,559": ["66,539" , "350,561"]
          }


master = Tk()
master.title("Emergency Services")
master.state('zoomed')

canvas = Canvas(master, width=860, height=675)
img = PhotoImage(file="Map.ppm")
canvas.create_image(10, 25, anchor=NW, image=img)
canvas.place(x=0, y=0)

Label(master, text="Accident Co-ordinates:", font=Font(family="Lucida Grande", size=15)).place(x=1020, y=100)
Label(master, text="X:", font=Font(family="Lucida Grande", size=12)).place(x=980, y=130)
Label(master, text="Y:", font=Font(family="Lucida Grande", size=12)).place(x=1140, y=130)

x = Entry(master)
y = Entry(master)
x.place(x=1000, y=132)
y.place(x=1160, y=132)

Button(master, text='Submit', command=lambda: get_values()).place(x=1010, y=160)
Button(master, text='Show Path', command=lambda: process_path()).place(x=1090, y=160)
Button(master, text='Clear', command=lambda: update_canvas()).place(x=1190, y=160)

Label(master, text="Hospital Co-ordinates:", font=Font(family="Lucida Grande", size=15)).place(x=1020, y=200)
Label(master, text="X: 558", font=Font(family="Lucida Grande", size=12)).place(x=980, y=230)
Label(master, text="Y: 285", font=Font(family="Lucida Grande", size=12)).place(x=1120, y=230)

msg = "\tLEGEND\t\n\nT\tTraffic-Signals\t\nH\tHospital\t\nA\tAmbulance\t\n!\tAccident-Spot\t\n----\tPath\t\n"
legend = Message(master, text=msg)
legend.config(bg='white', font=('times', 14), justify='left', width=500)
legend.place(x=1000, y=380)

mainloop()