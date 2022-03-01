import math
def minmax(arr,depth):
    maxturn=bool(depth%2)
    for i in range(depth):
        zipped=zip(arr[::2],arr[1::2])

        if maxturn:
            print("max",arr[::2],arr[1::2])
        else:
            print("min",arr[::2],arr[1::2])
        
        if maxturn:
            arr=max(arr[::2],arr[1::2])
        else:
            arr=min(arr[::2],arr[1::2])
        
        maxturn=not maxturn
    return arr
arr=[int(i) for i in input().split()]
depth=math.ceil(math.log(len(arr),2))
print("The solution is,",minmax(arr,depth))