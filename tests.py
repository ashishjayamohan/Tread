import basic_functions as bf
import graphing_functions as gf
import file_processing_functions as fpf
import table_functions as tf
import vectorization_functions as vf

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
    check(bf.determine_mode(sample_arr), "int", 5, "DETERMINE_MODE - ADVANCED")

def test_graph_frequency_histogram():
    sample_arr = [5,4,19,3,19,5,2,6,7,5]
    gf.graph_frequency_histogram(sample_arr)

def test_graph_scatter():
    sample_arr = [[5,3], [3,2], [2,1], [4,3], [5,1], [0,2], [1,3]]
    gf.graph_scatter(sample_arr)

def test_skew():
    sample_arr = [2, 4, 5, 7, 8, 10, 11, 25, 26, 27, 36]
    check(vf.skew(sample_arr), 11.072264507421869, 6, "SKEW")

def run_all():

    test_add()
    test_highest_frequency()
    test_add_advanced()
    test_determine_mode()
    test_determine_mode_advanced()
    test_skew()

    print("----------------------------------")
    print("BEGINNING HISTOGRAM CHECK")
    test_graph_frequency_histogram()
    print("HISTOGRAM CHECK COMPLETE")
    print("BEGINNING SCATTER PLOT CHECK")
    test_graph_scatter()
    print("SCATTER PLOT CHECK COMPLETE")

run_all()
