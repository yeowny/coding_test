# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17676
'''

import datetime
import time

def solution(lines):
    result_list = []
    for line in lines:
        line_date = line[:line.find(' ', line.find(' ')+1)]
        line_time = line[line.find(' ', line.find(' ')+1)+1:-1]
        
        end_time = datetime.datetime.strptime(line_date, '%Y-%m-%d %H:%M:%S.%f')
        start_time = end_time - datetime.timedelta(microseconds=(float(line_time)-0.001)*10**6)
        
        end_timestamp = time.mktime(end_time.timetuple()) + end_time.microsecond / 10.0**6
        start_timestamp = time.mktime(start_time.timetuple()) + start_time.microsecond / 10.0**6
        
        result_list.append([start_timestamp, end_timestamp])
    result_list.sort()
    
    answer = 0
    for result_point in result_list:
        tmp_cnt = 0
        sec_point = [result_point[0], result_point[0]+1]
        for ck_point in result_list:
            if sec_point[0] >= ck_point[0] and sec_point[0] <= ck_point[1]:
                tmp_cnt += 1
            elif sec_point[1] > ck_point[0] and sec_point[1] < ck_point[1]:
                tmp_cnt += 1
            elif sec_point[0] <= ck_point[0] and sec_point[1] >= ck_point[1]:
                tmp_cnt += 1
            answer = max(tmp_cnt, answer)
        
        tmp_cnt = 0
        sec_point = [result_point[0]-1, result_point[0]]
        for ck_point in result_list:
            if sec_point[0] > ck_point[0] and sec_point[0] < ck_point[1]:
                tmp_cnt += 1
            elif sec_point[1] >= ck_point[0] and sec_point[1] <= ck_point[1]:
                tmp_cnt += 1
            elif sec_point[0] <= ck_point[0] and sec_point[1] >= ck_point[1]:
                tmp_cnt += 1
            answer = max(tmp_cnt, answer)
    
    return answer


if __name__ == '__main__':
#    lines = ['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s'] #1 
    lines = ['2016-09-15 01:00:04.002 2.0s', '2016-09-15 01:00:07.000 2s'] #2
    
    print(solution(lines))
    