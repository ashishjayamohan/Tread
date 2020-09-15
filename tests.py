import basic_functions as bf

def check(real = 0, predicted = 0, test_number = 0, function_name = "Null Test"):
    if(str(real) == str(predicted)):
        print('Test #' + str(test_number) + ' has passed -- ' + function_name)
    else:
        print('Test #' + str(test_number) + ' has failed')
        print('Recalibrating, recalibrating....')

def test_add():
    sample_arr = [5,3,1,4,2]
    check(bf.add(sample_arr, mode = "int"), 15, 1, "ADD")

def test_add_advanced():
    sample_arr = ["5",3.0,1,"4",2.0]
    check(bf.add(sample_arr, mode = "mixed"), 15.0, 3, "ADD - ADVANCED")

def test_highest_frequency():
    sample_arr = [5,4,19,3,19,5,2,6,7,5]
    check(bf.highest_frequency(sample_arr), [5,3], 2, "HIGHEST_FREQUENCY")

def test_determine_mode():
    sample_arr = ["5",3.0,1,"4",2.0]
    check(bf.determine_mode(sample_arr), "mixed", 4, "DETERMINE_MODE")

def test_determine_mode_advanced():
    sample_arr = [5,3,1,4,2]
    check(bf.determine_mode(sample_arr), "int", 4, "DETERMINE_MODE")


def run_all():
    test_add()
    test_highest_frequency()
    test_add_advanced()
    test_determine_mode()
    test_determine_mode_advanced()

run_all()
