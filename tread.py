class BasicFunctions:
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
        elif(mode == "str"):
            sum = 0
            for j in arr:
                sum += int(j)
            return sum
        elif(mode == "float" or mode == "double"):
            sum = 0
            for j in arr:
                sum += j
            return sum
        else:
            print("Error: Incorrect Data Type")
    def average(arr, mode="Mixed"):
        sum = summation(arr, mode)
        length = len(arr)
        return sum/length
    def print_delim(arr, d=""):
        out = [str(i) for i in arr]
        print(d.join(out))
    def make_array(string, d=""):
        if(d == ""):
            return list(string)
        else:
            return string.split(d)
    def func_all(arr, operand="+", fact=0):
        if(operand == "+"):
            for j in range(len(arr)):
                arr[j] += fact
        elif(operand == "*"):
            for j in range(len(arr)):
                arr[j] *= fact
