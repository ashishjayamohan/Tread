def summation(arr, type="Mixed"):
    sum = 0
    for j in arr:
        if(type(j) == int):
            sum += j
        elif(j.isnumeric()):
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
    a, axis = _chk_asarray(a,axis)
    n = a.count(axis)
    m2 = moment(a, 2, axis)
    m3 = moment(a, 3, axis)
    with np.errstate(all='ignore'):
        vals = ma.where(m2 == 0, 0, m3 / m2**1.5)
    if not bias:
        can_correct = (n > 2) & (m2 > 0)
        if can_correct.any():
            m2 = np.extract(can_correct, m2)
            m3 = np.extract(can_correct, m3)
            nval = ma.sqrt((n-1.0)*n)/(n-2.0)*m3/m2**1.5
            np.place(vals, can_correct, nval)
    return vals
