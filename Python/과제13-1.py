def max_score(score_list):
    max_num = 0
    for score in score_list:
        if(max_num < score):
            max_num = score
    return max_num
'''
math_num = [12,25,65,85,13]
print("최고점은",max_score(math_num),'점 입니다')
'''
