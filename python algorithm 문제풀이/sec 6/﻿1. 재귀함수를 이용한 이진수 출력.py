import sys
sys.stdin=open("input.txt", "r")

def DFS(x):
    if x==0:
        return
    else:
        if x%2==0:
            DFS(x//2)
            print(x%2, end='')
        else: 
            DFS(x//2)
            print(x%2, end='')

if __name__=="__main__":
    n=int(input())
    DFS(n)
