def solution(answers):
    answer = []
    
    # Initialization
    counts = [0, 0, 0]
    
    answer_one = [1, 2, 3, 4, 5]
    answer_two = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(0, len(answers)):
        if answers[i] == answer_one[i % 5]:
            counts[0] = counts[0] + 1
            
        if answers[i] == answer_two[i % 8]:
            counts[1] = counts[1] + 1
            
        if answers[i] == answer_three[i % 10]:
            counts[2] = counts[2] + 1         
    
    # compare the number of answers that three students got right
    max = 0
    for i in range(len(counts)):
        if counts[i] > max:
            max = counts[i]
    
    for i in range(len(counts)):
        if counts[i] == max:
            answer.append(i + 1)
    
    return answer
