import basic_functions as bf

def check(real, predicted, test_number):
    if(str(real) == str(predicted)):
        print('Test #' + str(test_number) + ' has passed')
    else:
        print('Test #' + str(test_number) + ' has passed')
        print('Test has failed')
        print('Recalibrating, recalibrating....')

def test_add():
    sample_arr = [5,3,1,4,2]
    check(bf.add(sample_arr), 15, 1)

def run_all():
    test_add()

run_all()
