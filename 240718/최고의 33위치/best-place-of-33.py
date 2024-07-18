number = int(input())
'''
map = []

for _ in range(number):
    map.append(list(map(int, input().split())))
'''
board = [list(map(int,input().split())) for _ in range(number)]
ans = 0

for i in range(number-2):
    for j in range(number-2):
        temp = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]+board[i+2][j]+board[i+2][j+1]+board[i+2][j+2]
        ans = max(ans,temp)        

print(ans)