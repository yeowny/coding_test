# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17679
'''

def solution(m, n, board):
    board = [list(xx) for xx in board]
    answer = 0
    while True:
        check_board = [[0]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '_':
                    if len(set([board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]])) == 1:
                        check_board[i][j] = 1
                        check_board[i][j+1] = 1
                        check_board[i+1][j] = 1
                        check_board[i+1][j+1] = 1

        tmp_sum = sum([sum(xx) for xx in check_board])
        if tmp_sum != 0:
            answer += tmp_sum
            for j in range(n):
                for i in range(m):
                    if check_board[i][j] == 1:
                        board[i][j] = '_'
                        while i != 0:
                            tmp_block = board[i][j]
                            board[i][j] = board[i-1][j]
                            board[i-1][j] = tmp_block
                            i -= 1
        else:
            break

    return answer


if __name__ == '__main__':
#    m, n, board = 4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF'] # 14
    m, n, board = 6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'] # 15
    
    print(solution(m, n, board))
