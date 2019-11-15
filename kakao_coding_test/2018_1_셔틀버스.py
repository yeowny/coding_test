# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17678
'''

def solution(n, t, m, timetable):
    timetable = sorted([int(yy)*60+int(zz) for yy, zz in [xx.split(':') for xx in timetable]])

    for i in range(n):
        result_list = [540 + t*i, m, []]
        while len(timetable) != 0:
            if timetable[0] <= result_list[0] and result_list[1] != 0:
                result_list[1] -= 1
                result_list[2].append(timetable[0])
                timetable.pop(0)
            else:
                break

    if result_list[1] != 0:
        answer = result_list[0]
    else:
        answer = result_list[2][-1]-1

    return ':'.join([str(xx).zfill(2) for xx in divmod(answer, 60)])


if __name__ == '__main__':
#    n, t, m, timetable = 1, 1, 5, ['08:00', '08:01', '08:02', '08:03'] # 09:00
#    n, t, m, timetable = 2, 10, 2, ['09:10', '09:09', '08:00'] # 09:09
#    n, t, m, timetable = 2, 1, 2, ['09:00', '09:00', '09:00', '09:00'] # 08:59
#    n, t, m, timetable = 1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01'] # 00:00
#    n, t, m, timetable = 1, 1, 1, ['23:59'] # 09:00
    n, t, m, timetable = 10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59'] # 18:00
    
    print(solution(n, t, m, timetable))
