graph = { "11,141" : ["65,142"],
          "859,132": ["696,154"],
          "72,27" : ["65,142"],
          "65,142" : ["11,141" , "375,153" , "59,279" , "72,27"],
          "402,26" : ["375,153"],
          "375,153" : ["65,142", "695,154","402,26","362,283"],
          "696,154" : ["375,153","859,132","694,286"],
          "12,77": ["59,279"],
          "59,279": ["12,277","362,283","65,142","350,561"],
          "362,283": ["59,279","375,153","558,285","356,422","694,286"],
          "558,285": ["362,283","694,286"],
          "694,286" : ["558,285","696,154","694,416"],
          "356,422" : ["362,283", "694,416","350,561"],
          "694,416" : ["694,286","847,464","356,422"],
          "350,561": ["59,279","356,422","349,581"],
          "349,581" : ["350,561"],
          "559,581" : ["847,464"]
          }





# definition of function
def generate_edges(graph):
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
         for neighbour in graph[node]:
             # if edge exits then append
             edges.append(node, neighbour)
    return edges





#python program for validation of a graph

#import dictionary for graph
from collections import defaultdict
# function for adding edge to graph
graph =  defaultdict(list)
def addEdge (graph: object, u: object, v: object) -> object:
    graph[u].append(v)

# defination of function
def generate_edges(graph):
    edges = []

    # for each nod ein graph
    for node in graph:

         # for each neighbour node of a single node
         for neighbour in graph[node]:

            # if edge exits then append
            edges.append((node, neighbour))
    return edges

# declaration of graph as dictionary

addEdge(graph , '11,141' , '65,142')
addEdge(graph , '72,27' , '65,142')
addEdge(graph , '859,132' , '696,154')
addEdge(graph , '65,142' , '375,153')
addEdge(graph , '65,142' , '11,141')
addEdge(graph , '65,142' , '59,279')
addEdge(graph , '65,142' , '72,27')
addEdge(graph , '42,26' , '375,153')
addEdge(graph , '375,153' , '65,142')
addEdge(graph , '375,153' , '695,154')
addEdge(graph , '375,153' , '402,26')
addEdge(graph , '375,153' , '362,287')
addEdge(graph , '696,154' , '375,153')
addEdge(graph , '696,154' , '859,132')
addEdge(graph , '696,154' , '694,286')
addEdge(graph , '12,277' , '59,279')
addEdge(graph , '59,279' , '12,277')
addEdge(graph , '59,279' , '362,283')
addEdge(graph , '59,279' , '65,142')
addEdge(graph , '59,279' , '350,561')
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


#driver function call
#to print generated graph
print(generate_edges(graph))


# python program to generate the first
#path of the graph from the nodes provided


graph = {"11,141": ["65,142"],
         "859,132": ["696,154"],
         "72,27": ["65,142"],
         "65,142": ["11,141", "375,153", "59,279", "72,27"],
         "402,26": ["375,153"],
         "375,153": ["65,142", "695,154", "402,26", "362,283"],
         "696,154": ["375,153", "859,132", "694,286"],
         "12,77": ["59,279"],
         "59,279": ["12,277", "362,283", "65,142", "350,561"],
         "362,283": ["59,279", "375,153", "558,285", "356,422", "694,286"],
         "558,285": ["362,283", "694,286"],
         "694,286": ["558,285", "696,154", "694,416"],
         "356,422": ["362,283", "694,416", "350,561"],
         "694,416": ["694,286", "847,464", "356,422"],
         "350,561": ["59,279", "356,422", "349,581"],
         "349,581": ["350,561"],
         "559,581": ["847,464"]
         }

#function to find path
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:



        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
            return None
#driver function call to print the path
print (find_path(graph, '375,153', '558,285'))

graph = {"11,141": ["65,142"],
         "859,132": ["696,154"],
         "72,27": ["65,142"],
         "65,142": ["11,141", "375,153", "59,279", "72,27"],
         "402,26": ["375,153"],
         "375,153": ["65,142", "695,154", "402,26", "362,283"],
         "696,154": ["375,153", "859,132", "694,286"],
         "12,77": ["59,279"],
         "59,279": ["12,277", "362,283", "65,142", "350,561"],
         "362,283": ["59,279", "375,153", "558,285", "356,422", "694,286"],
         "558,285": ["362,283", "694,286"],
         "694,286": ["558,285", "696,154", "694,416"],
         "356,422": ["362,283", "694,416", "350,561"],
         "694,416": ["694,286", "847,464", "356,422"],
         "350,561": ["59,279", "356,422", "349,581"],
         "349,581": ["350,561"],
         "559,581": ["847,464"]
         }

# function to generate all possible patha
def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
             newpaths = find_all_paths(graph, node, end, path)
             for newpath in newpaths:
                 paths.append(newpath)
    return paths
# driver function call to print all generated paths
print(find_all_paths(graph, '375,153' , '558,285'))




# python program to generate shortest path

graph = {"11,141": ["65,142"],
         "859,132": ["696,154"],
         "72,27": ["65,142"],
         "65,142": ["11,141", "375,153", "59,279", "72,27"],
         "402,26": ["375,153"],
         "375,153": ["65,142", "695,154", "402,26", "362,283"],
         "696,154": ["375,153", "859,132", "694,286"],
         "12,77": ["59,279"],
         "59,279": ["12,277", "362,283", "65,142", "350,561"],
         "362,283": ["59,279", "375,153", "558,285", "356,422", "694,286"],
         "558,285": ["362,283", "694,286"],
         "694,286": ["558,285", "696,154", "694,416"],
         "356,422": ["362,283", "694,416", "350,561"],
         "694,416": ["694,286", "847,464", "356,422"],
         "350,561": ["59,279", "356,422", "349,581"],
         "349,581": ["350,561"],
         "559,581": ["847,464"]
         }

# function to find the shortest path
def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

#driver function call to print
#the shortest path
print(find_shortest_path(graph, '375,153', '558,285'))

