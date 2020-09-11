def summation(arr):
    sum = 0
    for j in arr:
        if(type(j) == int):
            sum += j
        elif(j.isnumeric()):
            sum += int(j)
    return sum
def average(arr):
    sum = summation(arr)
    length = len(arr)
    return sum/length
