import sys
sys.stdin=open("input.txt", "r")

def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for j in range(4):
            xx=x+dx[j]
            yy=y+dy[j]
            if 0<=xx<=6 and 0<=yy<=6 and num[xx][yy]==0 and ch[xx][yy]==0:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0

if __name__=="__main__":
    num=[list(map(int,input().split())) for _ in range(7)]
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    cnt=0
    ch=[[0]*7 for _ in range(7)]
    ch[0][0]=1
    DFS(0,0)
    print(cnt)
