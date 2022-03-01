graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}
def DLS(start,goal,path,level,maxD):
    path.append(start)
    if start==goal:
        print('Path found')
        return path
    if level==maxD:
        return False
    for child in graph[start]:
        if DLS(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False
start='A'
goal='G'
path=list()
res=DLS(start,goal,path,0,3)
if res:
    print('Path is',res)
else:
    print('No path')
