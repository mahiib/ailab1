visited=[]
frontier=[]
flag=0

def ucs(goal):
    global frontier
    global graph
    global flag
    if frontier:
        whole=sorted(frontier)[0]
        frontier.remove(whole)
        node=whole[1]
        cost=whole[0]
        for a in graph[node]:
            frontier.append((cost+graph[node][a],a))
            if(a==goal):
                print("city found, total cost: "+str(cost+graph[node][a]))
                flag=1
        if flag!=1:
            ucs(goal)

graph={
    'arad':{'zerind':75,'sibiu':140,'timisoara':118},
    'zerind':{'arad':75,'oradea':71},
    'oradea':{'zerind':71,'sibiu':151},
    'timisoara':{'arad':118,'lugoj':111},
    'sibiu':{'arad':140,'oradea':151,'fagaras':99,'rimnicu vilcea':80},
    'lugoj':{'timisoara':111,'mehadia':70},
    'fagaras':{'sibiu':99,'bucharest':211},
    'rimnicu vilcea':{'sibiu':80,'pitesti':97,'craiova':146},
    'mehadia':{'lugoj':70,'dobreta':75},
    'dobreta':{'mehadia':75,'craiova':120},
    'bucharest':{'fagaras':211,'pitesti':101,'urziceni':85,'giurglu':90},
    'giurglu':{'bucharest':90},
    'pitesti':{'bucharest':101,'craiova':138,'rimnicu vilcea':97},
    'craiova':{'dobreta':120,'rimnicu vilcea':146,'pitesti':138},
    'urziceni':{'hirsova':98,'vaslui':142,'bucharest':85},
    'hirsova':{'urziceni':98,'eforie':86},
    'vaslui':{'urziceni':142,'lasi':92},
    'lasi':{'vaslui':92,'neamt':87},
    'eforie':{'hirsova':86},
    'neamt':{'lasi':87}
}



#search=input("Enter the city to be searched\n")
start='arad'
#input("Enter the starting city\n")
frontier.append((0,start))
ucs('oradea')
