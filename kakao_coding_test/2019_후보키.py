# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/42890
'''

from itertools import combinations

def solution(relation):
    answer = []
    for i in range(1, len(relation[0])+1):
        for comb in combinations(range(len(relation[0])), i):
            if all([False for xx in answer if not bool(xx - set(comb))]):
                tmp_list = []
                for x in relation:
                    tmp_x = ''
                    for j in comb:
                        tmp_x += x[j]
                    tmp_list.append(tmp_x)

                if len(set(tmp_list)) == len(relation):
                    answer.append(set(comb))

    return len(answer)


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]] # 2
    
    print(solution(relation))
