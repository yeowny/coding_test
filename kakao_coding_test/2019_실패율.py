# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/42889
'''

def solution(N, stages):
    stages.sort()
    result_list = [[0, -i] for i in range(N+2)]
    
    tmp_len = len(stages)
    tmp_level, tmp_cnt = 0, 0
    for i in range(len(stages)):
        if tmp_level != stages[i]:
            if tmp_cnt != 0:
                result_list[tmp_level][0] = tmp_cnt/tmp_len
            tmp_level = stages[i]
            tmp_len -= tmp_cnt
            tmp_cnt = 1
        else:
            tmp_cnt += 1
    
    if tmp_level <= N:
        if tmp_cnt != 0:
            result_list[tmp_level][0] = tmp_cnt/tmp_len
    
    return [-ii for _, ii in sorted(result_list[1:-1], reverse=True)]


if __name__ == '__main__':
#    N, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3] # [3,4,2,1,5]
    N, stages = 4, [4,4,4,4,4] # [4,1,2,3]
    
    print(solution(N, stages))
