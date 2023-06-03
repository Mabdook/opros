from config import *

def scores(answers):
    score = 0
    for i in range(len(questions)):
        if answers[i] in questions[i]['answer']:
            if questions[i]['type'] == 'close':
                score += 1
            if questions[i]['type'] == 'variant':
                score += 2
            if questions[i]['type'] == 'open':
                score += 0
    return score