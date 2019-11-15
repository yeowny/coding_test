# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/60061
'''

def solution(n, build_frame):
    answer = []
    b_frame = [[2]*(n+3)] + [[2]+[0]*(n+1)+[2] for _ in range(n+1)] + [[2]*(n+3)]
    g_frame = [[2]*(n+3)] + [[2]+[0]*(n+1)+[2] for _ in range(n+1)] + [[2]*(n+3)]
    
    for x, y, bg, br in build_frame:
        x += 1
        y += 1
        if br:
            if bg:
                if not(g_frame[y-1][x]==1 or g_frame[y-1][x+1]==1 or b_frame[y][x-1]*b_frame[y][x+1]==1):
                    continue
                b_frame[y][x] = 1
            else:
                if not(y==1 or g_frame[y-1][x]==1 or b_frame[y][x]==1 or b_frame[y][x-1]==1):
                    continue
                g_frame[y][x] = 1
            answer.append([x-1, y-1, bg])
        else:
            if bg:
                if g_frame[y][x]==1 and g_frame[y-1][x]==0:
                    if b_frame[y][x-1]!=1:
                        continue
                if g_frame[y][x+1]==1 and g_frame[y-1][x+1]==0:
                    if b_frame[y][x+1]!=1:
                        continue
                    
                if b_frame[y][x-1]==1:
                    if not(g_frame[y-1][x]==1 or g_frame[y-1][x-1]==1):
                        continue
                if b_frame[y][x+1]==1:
                    if not(g_frame[y-1][x+1]==1 or g_frame[y-1][x+2]==1):
                        continue
                b_frame[y][x] = 0
            else:
                if g_frame[y+1][x]==1:
                    if not(b_frame[y+1][x-1]==1 or b_frame[y+1][x]==1):
                        continue
                
                if b_frame[y+1][x-1]==1:
                    if b_frame[y+1][x]!=1:
                        if g_frame[y][x-1]!=1:
                            continue
                    else:
                        if b_frame[y+1][x+1]!=1:
                            if g_frame[y][x+1]!=1:
                                continue
                if b_frame[y+1][x]==1:
                    if b_frame[y+1][x-1]!=1:
                        if g_frame[y][x+1]!=1:
                            continue
                    else:
                        if b_frame[y+1][x-2]!=1:
                            if g_frame[y][x-1]!=1:
                                continue
                g_frame[y][x] = 0
            answer.remove([x-1, y-1, bg])
                
    return sorted(answer)


if __name__ == '__main__':
    n, build_frame = 5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] #[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
    n, build_frame = 5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]] #[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

    print(solution(n, build_frame))
