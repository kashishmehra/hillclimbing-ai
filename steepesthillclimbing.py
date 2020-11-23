import copy
import sys
q = []
universal=[]
length=[]

initial= [[[2,0,3],[1,8,4],[7,5,6]],
          [[2,1,3],[8,7,5],[0,6,4]],
          [[0,2,5],[8,1,3],[6,7,4]],
          [[8,3,0],[1,2,4],[7,6,5]],
          [[1,2,3],[7,6,4],[8,0,5]]
          ]
            
g=[[1,2,3],[8,0,4],[7,6,5]]


        
def compare(i,curr,f):
    if i!=curr:
        if i==f:
            #print("found")
            q.append(f)
            print(f)
            print("found")
            print("Mismatch of the last state : 0")
            #print(f)
            #print("The queue is: ",q)
            #print("The length is: ",len(q))
            return [0,i]
        else:
            print(i)
            return mismatch(i,g)
    else:
        return [10,i]

def enqueue(s):
    global q
    q=q+[s]

def mismatch(s,g):
    sum1=0
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]!=g[i][j]:
                sum1=sum1+1
    return [sum1,s]

def posofblank(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]==0:
                return [i,j]



def up(s):
    pos=posofblank(s)
    if pos[0]>0:
        temp=copy.deepcopy(s)
        temp[pos[0]][pos[1]]=temp[pos[0]-1][pos[1]]
        temp[pos[0]-1][pos[1]]=0
        return temp
    else:
        return s;

def down(s):
    pos=posofblank(s)
    if pos[0]<2:
        temp=copy.deepcopy(s)
        temp[pos[0]][pos[1]]=temp[pos[0]+1][pos[1]]
        temp[pos[0]+1][pos[1]]=0
        return temp
    else:
        return s

def left(s):
    pos=posofblank(s)
    if pos[1]>0:
        temp=copy.deepcopy(s)
        temp[pos[0]][pos[1]]=temp[pos[0]][pos[1]-1]
        temp[pos[0]][pos[1]-1]=0
        return temp
    else:
        return s
def right(s):
      pos=posofblank(s)
      if pos[1]<2:
          temp=copy.deepcopy(s)
          temp[pos[0]][pos[1]]=temp[pos[0]][pos[1]+1]
          temp[pos[0]][pos[1]+1]=0
          return temp
      else:
          return s

def search(s,g):
    curr=copy.deepcopy(s)
    q.append(curr)
    if(initial==g):
        #print("Found")
        exit()
    while True:
        #mismatch of current
        a=mismatch(curr,g)
        #print("Cuur mismatch",a[0])
        new=up(curr)
        a1=compare(new,curr,g)
        #print(a1[0])
        if(a1[0]==0):
            length.append(a1)
            return 
        new=right(curr)
        a2=compare(new,curr,g)
        #print(a2[0])
        if(a2[0]==0):
            length.append(a2)
            break
        new=left(curr)
        a3=compare(new,curr,g)
        #print(a3[0])
        if(a3[0]==0):
            length.append(a3)
            return 
        new=down(curr)
        a4=compare(new,curr,g)
        #print(a4[0])
        if(a4[0]==0):
            length.append(a4)
            return 
        ans=min(a1,a2,a3,a4)
        
        if(ans[0]<=a[0]):
            curr=ans[1]
            #print(curr)
            enqueue(ans[1])
            
        else:
            curr=a[1]
            k=mismatch(curr,g)
            print("Mismatch of the last state: ",k[0])
            length.append(k)
            print("not found")
            print()
            return
        
            


def randomstates(initial,g):
    for i in initial:
        global q
        global universal
        q=[]
        print("State ",initial.index(i)+1)
        search(i,g)
        print("The queue is:",q)
        universal=universal+[q]
        print("The length of the queue is",len(q))
        print()
        print()
    best=min(length, key=lambda x: x[0])
    print(" Best solution is : ",initial[length.index(best)] )
    search(initial[length.index(best)],g)
    print(" Intermediate states of the best solution : ")
    print(universal[length.index(best)])


randomstates(initial,g)
        
    
