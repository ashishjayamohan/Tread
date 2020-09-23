def check(real, predicted, function_name):
    if str(real) == str(predicted):
        print("  ✓ " + function_name + " PASSED")
    else:
        print("  ✖ " + function_name + " FAILED")
        print("Recalibrate System")
        print("-----------------------------------------")

from os import environ

import scripts.basic_functions as bf
if not hasattr(environ, 'githubaction'):
    import scripts.graphing_functions as gf
    skip_graphic = False
else:
    gf = type('gf_shim', (), {'__getattr__': lambda *_, **__: lambda *_, **__: None })()
    skip_graphic = False
import scripts.vectorization_functions as vf
import scripts.matrix_functions as mf
import scripts.math_functions as math

def test_add():
    # ADD - Vector functions version
    sample_arr = [5, 3, 1, 4, 2]
    check(bf.add(sample_arr, mode="int"), 15, "ADD")


def test_add_advanced():
    # ADD - Vector functions version
    sample_arr = ["5", 3.0, 1, "4", 2.0]
    check(bf.add(sample_arr, mode="mixed"), 15.0, "ADD - ADVANCED")


def test_highest_frequency():
    sample_arr = [5, 4, 19, 3, 19, 5, 2, 6, 7, 5]
    check(bf.highest_frequency(sample_arr), [5, 3], "HIGHEST_FREQUENCY")


def test_determine_mode():
    # Not numerical mode
    sample_arr = ["5", 3.0, 1, "4", 2.0]
    check(bf.determine_mode(sample_arr), "mixed", "DETERMINE_MODE")


def test_determine_mode_advanced():
    # Not numerical mode
    sample_arr = [5, 3, 1, 4, 2]
    check(bf.determine_mode(sample_arr), "int", "DETERMINE_MODE - ADVANCED")


def test_graph_frequency_histogram():
    sample_arr = [5, 4, 19, 3, 19, 5, 2, 6, 7, 5]
    gf.graph_frequency_histogram(sample_arr)


def test_graph_scatter():
    sample_arr = [[5, 3], [3, 2], [2, 1], [4, 3], [5, 1], [0, 2], [1, 3]]
    gf.graph_scatter(sample_arr)


def test_skew():
    sample_arr = [2, 4, 5, 7, 8, 10, 11, 25, 26, 27, 36]
    check(vf.skew(sample_arr), 11.072264507421869, "SKEW")


def test_determinant():
    matrix1 = [[1]]
    matrix2 = [[1, 2], [3, 4]]
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix4 = [
        [6, 2, 8, 3, 7],
        [2, 8, 1, 8, 1],
        [7, 4, 11, 6, 2],
        [15, 72, 1, 11, 19],
        [22, 44, 94, 67, 1],
    ]
    check(mf.determinant(matrix1), 1, "DETERMINANT - 1x1 Matrix")
    check(mf.determinant(matrix2), -2, "DETERMINANT - 2x2 Matrix")
    check(mf.determinant(matrix3), 0, "DETERMINANT - 3x3 Matrix")
    check(mf.determinant(matrix4), -1008848, "DETERMINANT - 5x5 Irregular Matrix")


def test_average():
    average1a = [2]
    average1b = [2.2]
    average2 = [1, 3]
    average3 = [6, 2, 5, 27, "75", 1.0, 6, 32]
    check(bf.average(average1a), 2.0, "AVERAGE - 1 element (integer)")
    check(bf.average(average1b), 2.2, "AVERAGE - 1 element (float)")
    check(bf.average(average2), 2.0, "AVERAGE - 2 elements")
    check(bf.average(average3), 19.25, "AVERAGE - Many elements, mixed types")


def test_types():
    types1 = [2]
    types2 = [2, "3"]
    types3 = [4, 4.0, "4"]
    types4 = [-300000, 32768.1, "25624642"]
    check(bf.types(types1), [type(2)], "TYPES - 1 element")
    check(bf.types(types2), [type(2), type("3")], "TYPES - 2 elements")
    check(bf.types(types3), [type(4), type(4.0), type("4")], "TYPES - 3 elements")
    check(
        bf.types(types4),
        [type(-3000000), type(32768.1), type("25624642")],
        "TYPES - Large inputs",
    )


def test_frequency():
    freq1 = [2]
    freq2 = [2, "2", 2.0]
    freq3 = [1, 2, 3, 3, 4, 4, 4]
    freq4 = [64214.0, -15213, "1563", 64214.0]
    check(bf.frequency(freq1), {2: 1}, "FREQUENCY - 1 element")
    check(
        bf.frequency(freq2, cast=False),
        {2: 2, "2": 1},
        "FREQUENCY - same value, different types (cast=False)",
    )
    check(
        bf.frequency(freq2, cast=False),
        {2.0: 3},
        "FREQUENCY - same value, different types (cast=True)",
    )
    check(bf.frequency(freq3), {1: 1, 2: 1, 3: 2, 4: 3}, "FREQUENCY - 7 elements")
    check(
        bf.frequency(freq4),
        {64214.0: 2, -15213: 1, "1563": 1},
        "FREQUENCY - Large inputs",
    )


def test_mode():
    # True numerical mode
    mode1 = [1]
    mode2 = [1, 2, 3]
    mode3 = [1, 1, 2, 3]
    mode4 = [1, 6, 24, 62, 2, 3563, 1]
    check(bf.mode(mode1), 1, "MODE - 1 element")
    check(bf.mode(mode2), None, "MODE - Uniform dataset")
    check(bf.mode(mode3), 1, "MODE - 4 elements")
    check(bf.mode(mode4), 1, "MODE - Large dataset")


def test_median():
    median1 = [1]
    median2 = [1, 2, 3]
    median3 = [1, 2, 3, 4]
    median4 = [1, 7, 2, 5, 27, 3]  # 4
    check(bf.median(median1), 1, "MEDIAN - 1 element")
    check(bf.median(median2), 2, "MEDIAN - 3 elements")
    check(bf.median(median3), 2.5, "MEDIAN - 4 elements")
    check(bf.median(median4), 4.0, "MEDIAN - 6 elements, unordered")


def test_quartiles():
    quartiles1 = [1]
    quartiles2 = [1, 2]
    quartiles3 = [1, 2, 3]
    quartiles4 = [1, 2, 3, 4, 5, 6]
    quartiles5 = [1, 7, 37, 2, 4, 73, 9]
    check(bf.quartiles(quartiles1), (1, 1, 1, 1, 1), "QUARTILES - 1 element")
    check(bf.quartiles(quartiles2), (1, None, 1.5, None, 2), "QUARTILES - 2 elements")
    check(bf.quartiles(quartiles3), (1, 1, 2, 3, 3), "QUARTILES - 3 elements")
    check(
        bf.quartiles(quartiles4),
        (1, 2, 3.5, 5, 6),
        "QUARTILES - Even number of elements",
    )
    check(
        bf.quartiles(quartiles5),
        (1, 2, 7, 37, 73),
        "QUARTILES - Odd number of elements",
    )


def test_add_num():
    check(math.add_num(5, 4), 9, "ADD_NUM - Integer 1")
    check(math.add_num(9, 130), 139, "ADD_NUM - Integer 2")
    check(math.add_num(1.0, 0.5), 1.5, "ADD_NUM - Float 1")
    check(math.add_num(1.4, 0.1), 1.5, "ADD_NUM - Float 2")
    check(math.add_num(1, 0.5), 1.5, "ADD_NUM - Integer & Float")


def test_multiply_matrices():
    test_matrix_1 = [[1, 2]]
    test_matrix_2 = [[1], [2]]
    check(
        mf.multiply(test_matrix_1, test_matrix_2),
        [[5.0]],
        "MULTIPLY - 1x2 and 2x1 matrices",
    )
    test_matrix_4 = [[1, 2], [3, 4]]
    test_matrix_5 = [[1, 3], [2, 3]]
    check(
        mf.multiply(test_matrix_4, test_matrix_5),
        [[5.0, 9.0], [11.0, 21.0]],
        "MULTIPLY - 2x2 and 2x2 matrices",
    )


def test_add_matrices():
    test_matrix_1 = [[1, 2]]
    test_matrix_2 = [[1, 2]]
    check(
        mf.add(test_matrix_1, test_matrix_2),
        [[2.0, 4.0]],
        "ADD - 1x2 and 1x2 matrices",
    )
    test_matrix_1 = [[1, 2], [1, 2]]
    test_matrix_2 = [[1, 2], [1, 2]]
    check(
        mf.add(test_matrix_1, test_matrix_2),
        [[2.0, 4.0], [2.0, 4.0]],
        "ADD - 2x2 and 2x2 matrices",
    )


def test_subtract_matrices():
    test_matrix_1 = [[1, 2]]
    test_matrix_2 = [[1, 2]]
    check(
        mf.subtract(test_matrix_1, test_matrix_2),
        [[0.0, 0.0]],
        "SUBSTRACT - 1x2 and 1x2 matrices",
    )
    test_matrix_1 = [[1, 2], [0, 1]]
    test_matrix_2 = [[1, 2], [1, 2]]
    check(
        mf.subtract(test_matrix_1, test_matrix_2),
        [[0.0, 0.0], [-1.0, -1.0]],
        "SUBSTRACT - 2x2 and 2x2 matrices",
    )


def test_divide_matrices():
    test_matrix_1 = [[1, 2]]
    test_matrix_2 = [[1, 2]]
    check(
        mf.divide(test_matrix_1, test_matrix_2),
        [[1.0, 1.0]],
        "DIVIDE - 1x2 and 1x2 matrices",
    )
    test_matrix_1 = [[1, 2], [0, 1]]
    test_matrix_2 = [[1, 2], [1, 2]]
    check(
        mf.divide(test_matrix_1, test_matrix_2),
        [[1.0, 1.0], [0.0, 0.5]],
        "DIVIDE - 2x2 and 2x2 matrices",
    )


def test_element_wise_multiply_matrices():
    test_matrix_1 = [[1, 2]]
    test_matrix_2 = [[1, 2]]
    check(
        mf.element_wise_multiply(test_matrix_1, test_matrix_2),
        [[1.0, 4.0]],
        "ELEMENT-WISE-MULTIPLY - 1x2 and 1x2 matrices",
    )
    test_matrix_1 = [[1, 2], [0, 1]]
    test_matrix_2 = [[1, 2], [1, 2]]
    check(
        mf.element_wise_multiply(test_matrix_1, test_matrix_2),
        [[1.0, 4.0], [0.0, 2.0]],
        "ELEMENT-WISE-MULTIPLY - 2x2 and 2x2 matrices",
    )


def run_all():
    print("Test #1")
    test_add()
    print("Test #2")
    test_highest_frequency()
    print("Test #3")
    test_add_advanced()
    print("Test #4")
    test_determine_mode()
    print("Test #5")
    test_determine_mode_advanced()
    print("Test #6")
    test_skew()
    print("Test #7")
    test_determinant()
    print("Test #8")
    test_average()
    print("Test #9")
    test_types()
    print("Test #10")
    test_frequency()
    print("Test #11")
    test_mode()
    print("Test #12")
    test_median()
    print("Test #13")
    test_quartiles()
    print("Test #14")
    test_add_num()
    print("Test #15")
    test_multiply_matrices()
    print("Test #16")
    test_add_matrices()
    print("Test #17")
    test_subtract_matrices()
    print("Test #18")
    test_element_wise_multiply_matrices()
    print("Test #18")
    test_divide_matrices()

    print("----------------------------------")
    print("BEGINNING HISTOGRAM CHECK")
    test_graph_frequency_histogram()
    print("HISTOGRAM CHECK COMPLETE")
    print("BEGINNING SCATTER PLOT CHECK")
    test_graph_scatter()
    print("SCATTER PLOT CHECK COMPLETE")


"""
This below function will run all given tests
Naturally, by running this file, this function will be called
If you receive an error, please create an issue on the Github page
"""
run_all()
