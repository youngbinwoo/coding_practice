import sys
sys.stdin=open("input.txt", "r")

def DFS(x,y):
    if x==0:
        print(y)
    elif 10>y-1>=0 and num[x][y-1]>0 and ch[x][y-1]==0:
        ch[x][y-1]=1
        DFS(x,y-1)
    elif 10>y+1>=0 and num[x][y+1]>0 and ch[x][y+1]==0:
        ch[x][y+1]=1
        DFS(x,y+1)
    else:
        ch[x-1][y]=1
        DFS(x-1,y)



if __name__=="__main__":
    num=[list(map(int,input().split())) for _ in range(10)]
    ch=[[0]*10 for _ in range(10)]
    for j in range(10):
        if num[9][j]==2:
            ch[9][j]=1
            DFS(9,j)
