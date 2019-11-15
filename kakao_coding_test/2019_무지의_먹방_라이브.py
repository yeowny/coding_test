# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/42891
'''

def solution(food_times, k):
    if sum(food_times) <= k:
           return -1

    time_dict = {}
    for i, x in enumerate(food_times):
        if x in time_dict:
            time_dict[x].append(i+1)
        else:
            time_dict[x] = [i+1]

    tmp_n = 0
    len_food_times = len(food_times)
    for x in sorted(time_dict):
        if k - len_food_times * (x - tmp_n) >= 0:
            k -= len_food_times * (x - tmp_n)
            len_food_times -= len(time_dict[x])
            tmp_n += x - tmp_n
        else:
            k %= len_food_times
            answer_list = []
            for y in time_dict:
                if y >= x:
                    answer_list.extend(time_dict[y])

            return sorted(answer_list)[k]


if __name__ == '__main__':
    food_times, k = [3, 1, 2], 5 # 1
    
    print(solution(food_times, k))
