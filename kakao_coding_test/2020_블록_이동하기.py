# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/60063
'''

def solution(board):
    n = len(board)
    w_board = [[0 if board[i][j]+board[i][j+1]==0 else -1 for j in range(len(board)-1)] for i in range(len(board))]
    h_board = [[0 if board[i][j]+board[i+1][j]==0 else -1 for j in range(len(board))] for i in range(len(board)-1)]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    w_dx = [0, 1, 1, 0]    
    w_dy = [-1, -1, 0, 0]
    check_w_dx = [1, 0, 0, 1]
    check_w_dy = [-1, -1, 1, 1]
    
    h_dx = [-1, 0, 0, -1]
    h_dy = [0, 0, 1, 1]
    check_h_dx = [-1, 1, 1, -1]    
    check_h_dy = [1, 1, 0, 0]
    
    target_point = [(0, 0, 0)]
    while len(target_point)!=0:
        x, y, h_w = target_point.pop(0)

        if h_w:
            v = h_board[y][x]
            for i in range(4):
                tmp_x = x + dx[i]
                tmp_y = y + dy[i]
                
                if tmp_x<0 or tmp_x>=n or tmp_y<0 or tmp_y>=n-1:
                    continue
                
                tmp_v = h_board[tmp_y][tmp_x]
                if tmp_v!=-1 and (tmp_v==0 or v+1<tmp_v):
                    h_board[tmp_y][tmp_x] = v+1
                    target_point.append((tmp_x, tmp_y, 1))
            
            for i in range(4):
                tmp_x = x + h_dx[i]
                tmp_y = y + h_dy[i]
                
                if tmp_x<0 or tmp_x>=n-1 or tmp_y<0 or tmp_y>=n:
                    continue
                if  board[y+check_h_dy[i]][x+check_h_dx[i]]==1:
                    continue
                
                tmp_v = w_board[tmp_y][tmp_x]
                if tmp_v!=-1 and (tmp_v==0 or v+1<tmp_v):
                    w_board[tmp_y][tmp_x] = v+1
                    target_point.append((tmp_x, tmp_y, 0))
        else:
            v = w_board[y][x]
            for i in range(4):
                tmp_x = x + dx[i]
                tmp_y = y + dy[i]
                
                if tmp_x<0 or tmp_x>=n-1 or tmp_y<0 or tmp_y>=n:
                    continue
                
                tmp_v = w_board[tmp_y][tmp_x]
                if tmp_v!=-1 and (tmp_v==0 or v+1<tmp_v):
                    w_board[tmp_y][tmp_x] = v+1
                    target_point.append((tmp_x, tmp_y, 0))
            
            for i in range(4):
                tmp_x = x + w_dx[i]
                tmp_y = y + w_dy[i]
                
                if tmp_x<0 or tmp_x>=n or tmp_y<0 or tmp_y>=n-1:
                    continue
                if  board[y+check_w_dy[i]][x+check_w_dx[i]]==1:
                    continue
                
                tmp_v = h_board[tmp_y][tmp_x]
                if tmp_v!=-1 and (tmp_v==0 or v+1<tmp_v):
                    h_board[tmp_y][tmp_x] = v+1
                    target_point.append((tmp_x, tmp_y, 1))
                
        
    return min([xx for xx in [w_board[-1][-1], h_board[-1][-1]] if xx!=0 and xx!=-1])


if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]] #7
    
    print(solution(board))
