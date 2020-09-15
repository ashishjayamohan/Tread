def cumulative_sum(arr):
    current_val = 0
    answer = []
    for j in arr:
        current_val += j
        answer.append(current_val)
    return answer
