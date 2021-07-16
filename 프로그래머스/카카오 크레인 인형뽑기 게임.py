def solution(board, moves):
    ans=[]
    cnt=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                ans.append(board[j][i-1])
                board[j][i-1]=0
                if ans[-1:]==ans[-2:-1]:
                    cnt+=2
                    ans=ans[:-2]
                break
    return cnt
