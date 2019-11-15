# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17680
'''

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    
    answer = 0
    cache_list = ['_'] * cacheSize
    for x in cities:
        x = x.lower()
        if x in cache_list:
            answer += 1
            cache_list.remove(x)            
        else:
            answer += 5
            cache_list.pop(0)
        cache_list.append(x)
    return answer


if __name__ == '__main__':
#    cacheSize, cities = 3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'] # 50
#    cacheSize, cities = 3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'] # 21
#    cacheSize, cities = 2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'] # 60
#    cacheSize, cities = 5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'] # 52
#    cacheSize, cities = 2, ['Jeju', 'Pangyo', 'NewYork', 'newyork'] # 16
    cacheSize, cities = 0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'] # 25
    
    print(solution(cacheSize, cities))
