import scripts.basic_functions as bf
import scripts.graphing_functions as gf
import scripts.file_processing_functions as fpf
import scripts.vectorization_functions as vf
import scripts.matrix_functions as mf

def check(real, predicted, function_name):
    if(str(real) == str(predicted)):
        print('  ✓ ' + function_name + ' PASSED')
    else:
        print('  ✖ ' + function_name + ' FAILED')
        print('Recalibrating, recalibrating....')

def test_add():
    sample_arr = [5,3,1,4,2]
    check(bf.add(sample_arr, mode = "int"), 15, "ADD")

def test_add_advanced():
    sample_arr = ["5",3.0,1,"4",2.0]
    check(bf.add(sample_arr, mode = "mixed"), 15.0, "ADD - ADVANCED")

def test_highest_frequency():
    sample_arr = [5,4,19,3,19,5,2,6,7,5]
    check(bf.highest_frequency(sample_arr), [5,3], "HIGHEST_FREQUENCY")

def test_determine_mode():
    sample_arr = ["5",3.0,1,"4",2.0]
    check(bf.determine_mode(sample_arr), "mixed", "DETERMINE_MODE")

def test_determine_mode_advanced():
    sample_arr = [5,3,1,4,2]
    check(bf.determine_mode(sample_arr), "int", "DETERMINE_MODE - ADVANCED")

def test_graph_frequency_histogram():
    sample_arr = [5,4,19,3,19,5,2,6,7,5]
    gf.graph_frequency_histogram(sample_arr)

def test_graph_scatter():
    sample_arr = [[5,3], [3,2], [2,1], [4,3], [5,1], [0,2], [1,3]]
    gf.graph_scatter(sample_arr)

def test_skew():
    sample_arr = [2, 4, 5, 7, 8, 10, 11, 25, 26, 27, 36]
    check(vf.skew(sample_arr), 11.072264507421869, "SKEW")

def test_determinant():
    matrix1 = [[1]]
    matrix2 = [[1, 2], [3, 4]]
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix4 = [[6, 2, 8, 3, 7], [2, 8, 1, 8, 1], [7, 4, 11, 6, 2], [15, 72, 1, 11, 19], [22, 44, 94, 67, 1]]
    check(mf.determinant(matrix1), 1, "DETERMINANT - 1x1 Matrix")
    check(mf.determinant(matrix2), -2, "DETERMINANT - 2x2 Matrix")
    check(mf.determinant(matrix3), 0, "DETERMINANT - 3x3 Matrix")
    check(mf.determinant(matrix4), -1008848, "DETERMINANT - 5x5 Irregular Matrix")

def test_average():
    average1a = [2]
    average1b = [2.2]
    average2 = [1,3]
    average3 = [6,2,5,27,'75',1.0,6,32]
    check(bf.average(average1a), 2.0, 'AVERAGE - 1 element (integer)')
    check(bf.average(average1b), 2.2, 'AVERAGE - 1 element (float)')
    check(bf.average(average2), 2.0, 'AVERAGE - 2 elements')
    check(bf.average(average3), 19.25, 'AVERAGE - Many elements, mixed types')

def test_types():
    types1 = [2]
    types2 = [2, '3']
    types3 = [4, 4.0, '4']
    types4 = [-300000, 32768.1, '25624642']
    check(bf.types(types1), [type(2)], 'TYPES - 1 element')
    check(bf.types(types2), [type(2), type('3')], 'TYPES - 2 elements')
    check(bf.types(types3), [type(4), type(4.0), type('4')], 'TYPES - 3 elements')
    check(bf.types(types4), [type(-3000000), type(32768.1), type('25624642')], 'TYPES - Large inputs')

def test_frequency():
    freq1 = [2]
    freq2 = [2, '2', 2.0]
    freq3 = [1, 2, 3, 3, 4, 4, 4]
    freq4 = [64214.0, -15213, '1563', 64214.0]
    check(bf.frequency(freq1), {2: 1}, 'FREQUENCY - 1 element')
    check(bf.frequency(freq2, cast=False), {2: 2, '2': 1}, 'FREQUENCY - same value, different types (cast=False)')
    check(bf.frequency(freq2, cast=False), {2.0: 3}, 'FREQUENCY - same value, different types (cast=True)')
    check(bf.frequency(freq3), {1: 1, 2: 1, 3: 2, 4: 3}, 'FREQUENCY - 7 elements')
    check(bf.frequency(freq4), { 64214.0: 2, -15213: 1, '1563': 1}, 'FREQUENCY - Large inputs')

def run_all():
    print('Test #1')
    test_add()
    print('Test #2')
    test_highest_frequency()
    print('Test #3')
    test_add_advanced()
    print('Test #4')
    test_determine_mode()
    print('Test #5')
    test_determine_mode_advanced()
    print('Test #6')
    test_skew()
    print('Test #7')
    test_determinant()
    print('Test #8')
    test_average()
    print('Test #9')
    test_types()

    print("----------------------------------")
    print("BEGINNING HISTOGRAM CHECK")
    test_graph_frequency_histogram()
    print("HISTOGRAM CHECK COMPLETE")
    print("BEGINNING SCATTER PLOT CHECK")
    test_graph_scatter()
    print("SCATTER PLOT CHECK COMPLETE")

run_all()
