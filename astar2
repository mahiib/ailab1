from queue import PriorityQueue
graph={
       "A":{"B":1,"C":3,"D":7},
       "B":{"D":5},
       "C":{"D":12},
}
h_value={
    "A":2,
    "B":2,
    "C":2,
    "D":2,
}
def  search(graph,start,end):
    queue=PriorityQueue()
    queue.put((0+h_value[start],[start]))
    while not queue.empty():
        node=queue.get()
        current=node[1][len(node[1])-1]
        if end in node[1]:
            print("path found:"+str(node[1])+",cost="+str(node[0]))
            break
        cost=node[0]-h_value[current]
        for neighbor in graph[current]:
            temp=node[1][:]
            temp.append(neighbor)
            queue.put((cost+graph[current][neighbor]+h_value[neighbor],temp)) 
search(graph,"A","D")
