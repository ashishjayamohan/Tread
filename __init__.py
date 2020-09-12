def summation(arr, type="Mixed"):
    if(type == "Mixed"):
        sum = 0
        for j in arr:
            if(type(j) == int):
                sum += j
            elif(j.isnumeric()):
                sum += int(j)
        return sum
    elif(type == "int"):
        sum = 0
        for j in arr:
            sum += j
        return sum
    else:
        sum = 0
        for j in arr:
            sum += int(j)
        return sum
def average(arr, type="Mixed"):
    sum = summation(arr)
    length = len(arr)
    return sum/length
def print_tab(arr):
    out = [str(i) for i in arr]
    print("\t".join(out))
def print_space(arr):
    out = [str(i) for i in arr]
    print(" ".join(out))
def or(a, b, ind=min(len(a),len(b))):
    arr = []
    for j in range(ind):
        arr.append(a[j]|b[j])
    return arr
def skew(a, axis=0, bias=True):
