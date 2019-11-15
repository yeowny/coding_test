# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/60059
'''

def key_trun(key, n_key):
    re_key = [[-1]*n_key for _ in range(n_key)]
    for i in range(n_key):
        for j in range(n_key):
            re_key[j][-i-1] = key[i][j]
        
    return re_key
    
def solution(key, lock):
    n_key = len(key)
    tmp_n_key = n_key-1
    
    key_list = [key]
    for _ in range(3):
        key_list.append(key_trun(key_list[-1], n_key))
    
    key_list = [[yy for xx in zz for yy in xx] for zz in key_list]
    
    out_list = [99]
    p_cnt = sum([xx.count(0) for xx in lock])
    lock = [out_list*tmp_n_key+xx+out_list*tmp_n_key for xx in lock]
    for _ in range(tmp_n_key):
        lock.insert(0, out_list*len(lock[0]))
    lock.extend([out_list*len(lock[0]) for _ in range(tmp_n_key)])
    
    tmp_n_lock = len(lock)-tmp_n_key
    for i in range(tmp_n_lock):
        for j in range(tmp_n_lock):
            tmp_lock = [lock[i+ii][j+jj] for ii in range(tmp_n_key+1) for jj in range(n_key)]
            if p_cnt == tmp_lock.count(0):
                for tmp_key in key_list:
                    tmp_check = [xx+yy for xx, yy in zip(tmp_key, tmp_lock)]
                    if tmp_check.count(0) == tmp_check.count(2) == 0:
                        return True
            
    return False


if __name__ == '__main__':
    key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]] # true

    print(solution(key, lock))
