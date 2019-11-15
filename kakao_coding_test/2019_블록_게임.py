# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/42894
'''

def next_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -2:
                board[i][j] = 0
    
    w_board = len(board[0])-1
    board = [xx for xx in board if xx.count(0)!=w_board]
    
    i = 0
    h_board = len(board)-1
    while i != len(board[0])-1:
        if sum([board[xx][i] for xx in range(h_board)])!=0:
            i += 1
        else:
            for j in range(h_board+1):
                board[j] = board[j][:i] + board[j][i+1:]
    
    board = [[0]*len(board[0]) for _ in range(2)] + board
    for j in range(len(board[0])):
        for i in range(len(board)):
            if board[i][j] != 0:
                board[i-1][j] = -2
                board[i-2][j] = -2
                break
    
    return board[2:]
    
def solution(board):
    answer = 0
    fn_board = [xx+[-1] for xx in board]
    fn_board.append([-1 for _ in range(len(fn_board[0]))])
    
    tmp_answer = -1
    while tmp_answer != 0:
        fn_board = next_board(fn_board)
        
        tmp_answer = 0
        h_board = len(fn_board)-2
        w_board = len(fn_board[0])-2
        for j in range(w_board):
            for i in range(h_board):
                tmp_list = []
                for w_i in range(i, i+2):
                    for w_j in range(j, j+3):
                        tmp_list.append(fn_board[w_i][w_j])
                
                if tmp_list.count(0)==0 and tmp_list.count(-2)==2 and len(set(tmp_list))==2:
                    tmp_answer += 1
                    for w_i in range(i, i+2):
                        for w_j in range(j, j+3):
                            fn_board[w_i][w_j] = 0
                    break
                
                tmp_list = []
                for h_i in range(i, i+3):
                    for h_j in range(j, j+2):
                        tmp_list.append(fn_board[h_i][h_j])
                
                if tmp_list.count(0)==0 and tmp_list.count(-2)==2 and len(set(tmp_list))==2:
                    tmp_answer += 1
                    for h_i in range(i, i+3):
                        for h_j in range(j, j+2):
                            fn_board[h_i][h_j] = 0
                    break
        
        answer += tmp_answer
        
    return answer


if __name__ == '__main__':
    board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]] # 2
    
    print(solution(board))
