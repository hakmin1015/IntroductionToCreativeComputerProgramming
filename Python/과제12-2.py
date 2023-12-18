def list_avg(numlist):
    sum = 0
    for i in numlist:
        sum += i
    result = sum / len(numlist)
    return result

math_score = [80,75,85,90,60]
print(list_avg(math_score))
