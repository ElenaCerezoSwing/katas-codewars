def golf_score_calculator(par_string, score_string):
    par = [int(i) for i in par_string]
    score = [int(i) for i in score_string]
    acc = 0
    for i in range(len(par)):
        acc += score[i] - par[i]    
    return acc