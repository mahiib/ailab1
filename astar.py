class Graph:
    def __init__(self,adjac_list):
        self.adjac_list=adjac_list
        
    def get_neighbours(self,v):
        return self.adjac_list[v]
    def h(self,n):
        H={
            'A':1,
            'B':1,
            'C':1,
            'D':1
        }
        return H[n]

    def astar(self,start,stop):
        open_list=set([start])
        closed_list=set([])
        dis={}
        dis[start]=0
        adj={}
        adj[start]=start

        
        while len(open_list)>0:
            n=None
            for v in open_list:
                if n == None or dis[v]+self.h(v)<dis[n]+self.h(n):
                    n=v
                
            if n == None:
                print('No path exists')
                return None
                
            if n == stop:
                print('Path found')
                reconst_path=[]
                while adj[n]!=n:
                    reconst_path.append(n)
                    n=adj[n]
                    
                reconst_path.append(start)
                reconst_path.reverse()
                print("path is: {}".format(reconst_path))
                return reconst_path
            
            for (m,weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    dis[m]=dis[n]+weight
                    adj[m]=n

                else:
                    if dis[m]>dis[n]+weight:
                        dis[m]=dis[n]+weight
                        adj[m]=n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
                    
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist')
        return None
        
adjac_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
graph1=Graph(adjac_list)
graph1.astar('A', 'D')