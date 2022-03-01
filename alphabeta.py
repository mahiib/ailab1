import math
depth=0
MIN=-1000
MAX=1000
def minmax(depth,ni,mp,values,a,b):
    if depth==3:
        return values[ni]
    

    if mp:
        best=MIN
        for i in range(0,2):
            val=minmax(depth+1,ni*2+i,False,values,a,b)
            best=max(best,val)
            a=max(best,a)
        
            if b <=a:
                break
        

        return best
    else:
        best = MAX
        for i in range(0,2):
            val=minmax(depth+1,ni*2+i,True,values,a,b)
            best=min(best,val)
            b=min(best,b)

            if b<=a:
                break
        return best
values=[int(i) for i in input().split()]
depth=math.ceil(math.log(len(values),2))
print("Optimal value is",minmax(0,0,True,values,MIN,MAX))
