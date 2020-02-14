#Input To The Programm Initial And Goal State
initial=(7, 2, 4,
         5," ",6,
         8, 3, 1)

goal_st=(7, 2,4,
         5, 3,6,
        8,1," ")

#To Print The Path Traversed
def printChilds(A):
    node=initial
    level=1
    for j in range(len(A)):
        x=findChilds(node)
        if A[j] in x:
            print("------------------Level {}-------------------".format(level))
            node=A[j]
            level=level+1
        if(j==0):print("Start State")
        
        for i in range(0,9,3):
            print(A[j][i],A[j][i+1],A[j][i+2])
        print(moves[j])

#To Hold Various Moves And Function For Movements Of Empty Tile
moves=[" "]
def up(A,i):
    A=list(A)
    A[i],A[i-3]=A[i-3],A[i]
    if A not in explored:moves.append("Move Up\n")
    return A
def down(A,i):
    A=list(A)
    A[i],A[i+3]=A[i+3],A[i]
    if A not in explored:moves.append("Move Down\n")
    return A
def left(A,i):
    A=list(A)
    A[i],A[i-1]=A[i-1],A[i]
    if A not in explored:moves.append("Move Left\n")
    return A
def right(A,i):
    A=list(A)
    A[i],A[i+1]=A[i+1],A[i]
    if A not in explored:moves.append("Move Right\n")
    return A

#To Finds Childs Of A Parent Node        
def findChilds(Node):
    index=Node.index(" ")
    childs=[]
    if((index+1 in range(0,9)) and (index % 3 != 2)):
        c1=right(Node,index)
        childs.append(c1)
        
    if(index+3 in range(0,9)):
        c2=down(Node,index)
        childs.append(c2)
    
    if(index-3 in range(0,9)):
        c3=up(Node,index)
        childs.append(c3)

    if((index-1 in range(0,9)) and (index % 3 !=0)):
        c4=left(Node,index)
        childs.append(c4)
    return childs
explored=[]

#BFS Traversal Of Nodes
def bfs_connected_component(start,goal):
    start=list(start)
    goal=list(goal)
    queue = [start]
    COST=0
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            COST+=1
            if node==goal:
                moves.append("Goal State")
                print("\nTotal Cost:- ",COST-1)
                return explored
            neighbours = findChilds(node)
            for neighbour in neighbours:queue.append(neighbour)
      
rest=bfs_connected_component(initial,goal_st) 
printChilds(rest)


