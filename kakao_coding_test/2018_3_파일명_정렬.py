# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17686
'''

def solution(files):
    answer = []
    for x in files:
        x += '_'
        tmp_f = []
        bool_tmp = True
        for i in range(1, len(x)):
            if bool_tmp and x[i].isdigit():
                tmp_f.append(x[:i])
                bool_tmp = False
            elif not bool_tmp and not x[i].isdigit():
                tmp_f.append(x[len(tmp_f[-1]):i])
                tmp_f.append(x[i:])
                break

        answer.append(tmp_f)

    return [''.join(xx)[:-1] for xx in sorted(answer, key=lambda x: [x[0].lower(), int(x[1])])]


if __name__ == '__main__':
#    files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG'] # [img1.png, IMG01.GIF, img02.png, img2.JPG, img10.png, img12.png]
    files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat'] # [A-10 Thunderbolt II, B-50 Superfortress, F-5 Freedom Fighter, F-14 Tomcat]
    
    print(solution(files))
