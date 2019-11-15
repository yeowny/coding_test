# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17683
'''

def fn_re_code(code):
    for x in [['C#', 'c'], ['D#', 'd'], ['F#', 'f'], ['G#', 'g'], ['A#', 'a']]:
        code = code.replace(x[0], x[1])
    return code

def solution(m, musicinfos):
    find_code = fn_re_code(m)

    correct_list = []
    for i, music_one in enumerate(musicinfos):
        music_one_list = music_one.split(',')
        
        start_time = sum([int(x)*(60**(1-i)) for i, x in enumerate(music_one_list[0].split(':'))])
        end_time = sum([int(x)*(60**(1-i)) for i, x in enumerate(music_one_list[1].split(':'))])
        music_time = end_time - start_time
        
        music_name = music_one_list[2]
        music_code = fn_re_code(music_one_list[3])
        run_code = (music_code*(int(music_time/len(music_code))+1))[:music_time]
        
        if find_code in run_code:
            correct_list.append([music_time, -i, music_name])
            
    correct_list.sort(reverse=True)
    if len(correct_list) == 0:
        return "(None)"
    else:
        return correct_list[0][-1]


if __name__ == '__main__':
#    m, musicinfos = 'ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF'] # HELLO
#    m, musicinfos = 'CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B'] # FOO
    m, musicinfos = 'ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF'] # WORLD
    
    print(solution(m, musicinfos))
