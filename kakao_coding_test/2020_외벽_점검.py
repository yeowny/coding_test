# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/60062
'''

def search_result(n, weak_list, dist, k=1):
    tmp_weak_set = set()
    dist_pop = dist.pop(0)
    for weak in weak_list:
        for j in range(len(weak)):
            tmp_weak = [xx-weak[j] for xx in weak[j:]] + [n+xx-weak[j] for xx in weak[:j]]
            tmp_weak = [xx for xx in tmp_weak if xx>dist_pop]
            tmp_weak_set.add(tuple(tmp_weak))
            if len(tmp_weak)==0:
                return k
            
    if len(dist) != 0:
        return search_result(n, list(tmp_weak_set), dist, k+1)
        
    return -1

def solution(n, weak, dist):
    dist = sorted(dist, reverse=True)
    return search_result(n, [weak], dist)
    


if __name__ == '__main__':
#    n, weak, dist = 12, [1, 5, 6, 10], [1, 2, 3, 4] #2
    n, weak, dist = 12, [1, 3, 4, 9, 10], [3, 5, 7] #1

    print(solution(n, weak, dist))
