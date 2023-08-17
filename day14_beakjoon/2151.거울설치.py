import sys
from collections import deque

N = int(sys.stdin.readline())
grid = [sys.stdin.readline().rstrip() for _ in range(N)]
door = []
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def init():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "#": 
                door.append((i, j))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    if not in_range(x,y): return False
    if grid[x][y] == "*": return False
    return True

def bfs():
    answer = 0
    q = deque()
    x, y = door[-1][0], door[-1][1]
    cnt_arr = [[sys.maxsize] * N for _ in range(N)]
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        q.append((new_x, new_y, i))
    
    while q:
        x, y, dir = q.popleft()
        
        if x == door[0][0] and y == door[0][1]:
            answer = cnt_arr[x][y][dir]
            break
            
        new_x, new_y = x+dx[dir], y+dy[dir]
        
        if can_go(new_x, new_y):
            # 처음 방문하는 곳이거나 더 적은 거울로 갈 수 있다면
            if cnt_arr[new_x][new_y] > cnt_arr[x][y][dir]:
                cnt_arr[new_x][new_y][dir] = cnt_arr[x][y][dir]
                q.appendleft((new_x, new_y, dir))
            
                
        
        
        
        
