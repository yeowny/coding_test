# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/42888
'''

def solution(record):
    str_dict = {'Enter':'{}님이 들어왔습니다.', 'Leave':'{}님이 나갔습니다.'}

    id_dict = {}
    result_list = []
    result_id_list = []
    for x in record:
        x_list = x.split()
        if len(x_list) != 2:
            id_dict[x_list[1]] = x_list[2]
        if x_list[0] != 'Change':
            result_list.append(str_dict[x_list[0]])
            result_id_list.append(x_list[1])
    
    return [xx.format(id_dict[yy]) for xx, yy in zip(result_list, result_id_list)]


if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"] # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    
    print(solution(record))
