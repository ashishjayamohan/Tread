def summation(arr, mode="mixed"):
    if(mode == "mixed"):
        sum = 0
        for j in arr:
            if(isinstance(j, int)):
                sum += j
            elif(j.isnumeric()):
                sum += int(j)
        return sum
    elif(mode == "int"):
        sum = 0
        for j in arr:
            sum += j
        return sum
    else:
        sum = 0
        for j in arr:
            sum += int(j)
        return sum
def average(arr, mode="Mixed"):
    sum = summation(arr)
    length = len(arr)
    return sum/length
def print_tab(arr):
    out = [str(i) for i in arr]
    print("\t".join(out))
def print_space(arr):
    out = [str(i) for i in arr]
    print(" ".join(out))
def make_array(string, d=""):
    if(d == ""):
        return list(string)
    else:
        return string.split(d)
