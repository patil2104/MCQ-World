#finding the cost of the path using DFS and BFS


import copy

inp=[[1,2,3],[4,-1,5],[6,7,8]]
out=[[1,2,3],[6,4,5],[-1,7,8]]

# print("Enter input puzzle")
# for i in range(3):
#   for j in range(3):
#     inp[i][j]=int(input("Enter number at "+str(i)+","+str(j)+" ->"))

def move(temp, movement):
  if movement=="up":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
          # blank space found
          if i!=0:
            temp[i][j]=temp[i-1][j]
            temp[i-1][j]=-1
          return temp

  if movement=="down":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
          # blank space found
          if i!=2:
            temp[i][j]=temp[i+1][j]
            temp[i+1][j]=-1
          return temp

  if movement=="left":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
          # blank space found
          if j!=0:
            temp[i][j]=temp[i][j-1]
            temp[i][j-1]=-1
          return temp

  if movement=="right":
    for i in range(3):
      for j in range(3):
        if(temp[i][j]==-1):
          # blank space found
          if j!=2:
            temp[i][j]=temp[i][j+1]
            temp[i][j+1]=-1
          return temp

def bfs():
  global inp
  global out
  
  pathcost=0

  queue=[]
  inpx=[inp,"none"]
  queue.append(inpx)
  # for i in range(9):
  while(True):
    puzzle=queue.pop()
    pathcost=pathcost+1
    print(str(puzzle[1])+" --> "+str(puzzle[0]))
    if(puzzle[0]==out):
      print("Found")
      print('Path cost-> '+str(pathcost-1))
      break
    else:
      # up
      if(puzzle[1]!="down"):
        temp=copy.deepcopy(puzzle[0])
        up=move(temp, "up")
        upx=[up,"up"]
        queue.insert(0, upx)
      # left
      if(puzzle[1]!="right"):
        temp=copy.deepcopy(puzzle[0])
        left=move(temp, "left")
        leftx=[left,"left"]
        queue.insert(0, leftx)
      # down
      if(puzzle[1]!="up"):
        temp=copy.deepcopy(puzzle[0])
        down=move(temp, "down")
        downx=[down,"down"]
        queue.insert(0, downx)
      # right
      if(puzzle[1]!="left"):
        temp=copy.deepcopy(puzzle[0])
        right=move(temp, "right")
        rightx=[right,"right"]
        queue.insert(0, rightx)

    # print(queue)

def dfs():
  global inp
  global out
  
  pathcost=0

  stack=[]
  inpx=[inp,"none"]
  stack.append(inpx)
  # for i in range(9):
  while(True):
    puzzle=stack.pop(0)
    pathcost=pathcost+1
    print(str(puzzle[1])+" --> "+str(puzzle[0]))
    if(puzzle[0]==out):
      print("Found")
      print("Path cost -> "+str(pathcost-1))
      break
    else:
      # up
      if(puzzle[1]!="down"):
        temp=copy.deepcopy(puzzle[0])
        up=move(temp, "up")
        if(up!=puzzle[0]):
          upx=[up,"up"]
          stack.insert(0, upx)
      # left
      if(puzzle[1]!="right"):
        temp=copy.deepcopy(puzzle[0])
        left=move(temp, "left")
        if(left!=puzzle[0]):
          leftx=[left,"left"]
          stack.insert(0, leftx)
      # down
      if(puzzle[1]!="up"):
        temp=copy.deepcopy(puzzle[0])
        down=move(temp, "down")
        if(down!=puzzle[0]):
          downx=[down,"down"]
          stack.insert(0, downx)
      # right
      if(puzzle[1]!="left"):
        temp=copy.deepcopy(puzzle[0])
        right=move(temp, "right")
        if(right!=puzzle[0]):
          rightx=[right,"right"]
          stack.insert(0, rightx)




print('~~~~~~~~~~~~ BFS ~~~~~~~~~~~~')
bfs()

print('~~~~~~~~~~~~ DFS ~~~~~~~~~~~~')
dfs()


