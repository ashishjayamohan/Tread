from pocha import describe, it

import scripts.vectorization_functions as vf

def assert_raises(*exceptions):
    def decorator(fn):
        def func_wrapper(*args, **kwargs):
            threw = False
            try:
                fn(*args, **kwargs)
            except exceptions:
                threw = True
            assert threw
        return func_wrapper
    return decorator

class Almost:
    def __init__(self, n, tol=1e-12):
        self._num = n
        self.tol = tol
    def __eq__(self, other):
        diff = self._num - other
        if diff < 0: diff = -diff
        return diff < self.tol

@describe('Basic Functions')
def test_basic_functions():
    import scripts.basic_functions as bf
    @describe('Add')
    def test_add():
        @it('Empty Array')
        def _():
            assert bf.add([]) == 0
        @it('Ints')
        def _():
            assert bf.add([5, 3, 1, 4, 2], mode='int') == 15
        @it('Floats')
        def _():
            assert bf.add([5.0, 2.5, 1.5, 4.0, 2.0], mode='float') == 15.0
        @it('Strings')
        def _():
            assert bf.add(['4.5', '3.5', '1', '4.0', '2'], mode='str') == 15.0
        @it('Mixed')
        def _():
            assert bf.add(['5', 3.0, 1, '4.0', 2.0], mode='mixed') == 15.0
    @describe('Average')
    def test_average():
        @it('Empty Array')
        def _():
            assert bf.average([]) == 0.0
        @it('One Element (int)')
        def _():
            assert bf.average([1]) == 1.0
        @it('One Element (float)')
        def _():
            assert bf.average([1.0]) == 1.0
        @it('Two Elements')
        def _():
            assert bf.average([1, 3]) == 2.0
        @it('Many Elements')
        def _():
            assert bf.average([1, 2, 3, 4, 5, 6]) == 3.5
    @describe('Types')
    def test_types():
        @it('Empty Array')
        def _():
            assert bf.types([]) == []
        @it('One Element')
        def _():
            assert bf.types([3]) == [type(3)]
        @it('Two Elements')
        def _():
            assert bf.types([3, '3']) == [type(3), type('3')]
        @it('Many Elements')
        def _():
            assert bf.types([3, '3', 3.0, [1, 2, 3], {'a': 1}]) == [type(3), type('3'), type(3.0), type([1, 2, 3]), type({'a': 1})]
    @describe('Highest Frequency')
    def test_highest_frequency():
        @it('Empty Array')
        def _():
            assert bf.highest_frequency([]) is None
        @it('One Element')
        def _():
            assert bf.highest_frequency([1]) == ((1,), 1)
        @it('Two Elements (Same)')
        def _():
            assert bf.highest_frequency([1, 1]) == ((1,), 2)
        @it('Two Elements (Different)')
        def _():
            assert bf.highest_frequency([1, 2]) == ((1, 2), 1)
        @it('Many Elements')
        def _():
            assert bf.highest_frequency([1, 5, 2, 3, 1, 4, 1, 5, 5]) == ((1, 5), 3)
    @describe('Frequency')
    def test_frequency():
        @it('Empty Array')
        def _():
            assert bf.frequency([]) == {}
        @it('One Element')
        def _():
            assert bf.frequency([1]) == {1: 1}
        @it('Two Elements (Same)')
        def _():
            assert bf.frequency([1, 1]) == {1: 2}
        @it('Two Elements (Different)')
        def _():
            assert bf.frequency([1, 2]) == {1: 1, 2: 1}
        @it('Same Value, Different Types (cast=False)')
        def _():
            assert bf.frequency([1, 1.0, '1', '1.0'], cast=False) == {1: 1, 1.0: 1, '1': 1, '1.0': 1}
        @it('Same Value, Different Types (cast=True)')
        def _():
            assert bf.frequency([1, 1.0, '1', '1.0'], cast=True) == {1.0: 4}
    @describe('Determine Mode')
    def test_determine_mode():
        @it('Empty Array')
        def _():
            assert bf.determine_mode([]) is None
        @it('One Element (int)')
        def _():
            assert bf.determine_mode([1]) == 'int'
        @it('One Element (float)')
        def _():
            assert bf.determine_mode([1.0]) == 'float'
        @it('One Element (str)')
        def _():
            assert bf.determine_mode(['1']) == 'str'
        @it('Many Elements (int)')
        def _():
            assert bf.determine_mode([1, 2, 3]) == 'int'
        @it('Many Elements (float)')
        def _():
            assert bf.determine_mode([1.0, 2.0, 3.0]) == 'float'
        @it('Many Elements (str)')
        def _():
            assert bf.determine_mode(['1', '2', '3']) == 'str'
        @it('Many Elements (mixed)')
        def _():
            assert bf.determine_mode([1, 2.0, '3']) == 'mixed'
    @describe('Median')
    def test_median():
        @it('Empty Array')
        def _():
            assert bf.median([]) is None
        @it('One Element (int)')
        def _():
            assert bf.median([1]) == 1
        @it('One Element (float)')
        def _():
            assert bf.median([1.0]) == 1.0
        @it('Two Elements')
        def _():
            assert bf.median([1, 2]) == 1.5
        @it('Many Elements')
        def _():
            assert bf.median([1, 2, 3, 4, 5, 6]) == 3.5
    @describe('Quartiles')
    def test_quartiles():
        @it('Empty Array')
        def _():
            assert bf.quartiles([]) is None
        @it('One Element')
        def _():
            assert bf.quartiles([1]) == (1, 1, 1, 1, 1)
        @it('Two Elements')
        def _():
            assert bf.quartiles([2, 1]) == (1, None, 1.5, None, 2)
        @it('Three Elements')
        def _():
            assert bf.quartiles([1, 3, 2]) == (1, 1, 2, 3, 3)
        @it('Six Elements')
        def _():
            assert bf.quartiles([4, 5, 6, 1, 2, 3]) == (1, 2, 3.5, 5, 6)
        @it('Seven Elements')
        def _():
            assert bf.quartiles([4, 2, 5, 3, 6, 1, 7]) == (1, 2, 4, 6, 7)
    @describe('Mode')
    def test_mode():
        @it('Empty Array')
        def _():
            assert bf.mode([]) == None
        @it('One Element')
        def _():
            assert bf.mode([1]) == 1
        @it('Two Elements (Same)')
        def _():
            assert bf.mode([1, 1]) == 1
        @it('Two Elements (Different)')
        def _():
            assert bf.mode([1, 2]) == None
        @it('Six Elements (Uniform)')
        def _():
            assert bf.mode([1, 2, 3, 4, 5, 6]) == None
        @it('Six Elements (Non-Uniform)')
        def _():
            assert bf.mode([1, 2, 3, 4, 5, 1]) == 1
    @describe('Length')
    def test_length():
        @it('Empty Array')
        def _():
            assert bf.length([]) == 0
        @it('One Element')
        def _():
            assert bf.length([1]) == 1
        @it('Two Elements')
        def _():
            assert bf.length([1, 2]) == 2
        @it('Five Elements')
        def _():
            assert bf.length([1, 2, 3, 4, 5]) == 5
    @describe('Pare Unique')
    def test_pare_unique():
        @it('Empty Array')
        def _():
            assert bf.pare_unique([]) == []
        @it('One Element')
        def _():
            assert bf.pare_unique([1]) == [1]
        @it('Two Elements (Same)')
        def _():
            assert bf.pare_unique([1, 1]) == [1]
        @it('Two Elements (Different)')
        def _():
            assert bf.pare_unique([1, 2]) == [1, 2]
        @it('Six Elements (Same)')
        def _():
            assert bf.pare_unique([1, 1, 1, 1, 1, 1]) == [1]
        @it('Six Elements (Unique)')
        def _():
            assert bf.pare_unique([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

@describe('Math Functions')
def test_math_functions():
    import scripts.math_functions as mf
    @describe('Add')
    def test_add_num():
        @it('1 + 1 = 2')
        def _():
            assert mf.add_num(1, 1) == 2
        @it('2 + 2 = 4')
        def _():
            assert mf.add_num(2, 2) == 4
        @it('2.5 + 3.5 = 6')
        def _():
            assert mf.add_num(2.5, 3.5) == 6
        @it('34,567 + 24,211 = 58,778')
        def _():
            assert mf.add_num(34567, 24211) == 58778
    @describe('Subtract')
    def test_subtract_num():
        @it('1 - 1 = 0')
        def _():
            assert mf.subtract_num(1, 1) == 0
        @it('2 - 3 = -1')
        def _():
            assert mf.subtract_num(2, 3) == -1
        @it('2.5 - 3.5 = -1')
        def _():
            assert mf.subtract_num(2.5, 3.5) == -1
        @it('37,831 - 84,521 = -46,690')
        def _():
            assert mf.subtract_num(37831, 84521) == -46690
    @describe('Absolute Difference')
    def test_abs_diff():
        @it('|3 - 1| = 2')
        def _():
            assert mf.abs_diff(3, 1) == 2
        @it('|5 - 10| = 5')
        def _():
            assert mf.abs_diff(5, 10) == 5
        @it('|28,542 - 61,317| = 32,775')
        def _():
            assert mf.abs_diff(28542, 61317) == 32775
    @describe('Divide')
    def test_divide_num():
        @it('k / 0 raises TypeError')
        @assert_raises(TypeError)
        def _():
            mf.divide_num(3, 0)
        @it('6 / 3 = 2')
        def _():
            assert mf.divide_num(6, 3) == 2
        @it('7 / 2 = 3.5')
        def _():
            assert mf.divide_num(7, 2) == 3.5
        @it('93.6 / 15.6 = 6')
        def _():
            assert mf.divide_num(93.6, 15.6) == 6
        @it('200,662 / 28,666 = 7')
        def _():
            assert mf.divide_num(200662, 28666) == 7
    @describe('Multiply')
    def test_multiply_num():
        @it('12 * 5 = 60')
        def _():
            assert mf.multiply_num(12, 5) == 60
        @it('7 * 7 = 49')
        def _():
            assert mf.multiply_num(7, 7) == 49
        @it('6.1 * 36.55 == 222.955')
        def _():
            from math import isclose
            assert isclose(mf.multiply_num(6.1, 36.55), 222.955)
        @it('5,048 * 729 = 3,679,992')
        def _():
            assert mf.multiply_num(5048, 729) == 3679992
    @describe('Modulo')
    def test_modulo():
        @it('k % 0 raises ZeroDivisionError')
        @assert_raises(ZeroDivisionError)
        def _():
            mf.mod(5, 0)
        @it('7 % 4 = 3')
        def _():
            assert mf.mod(7, 4) == 3
        @it('37 % 3 = 1')
        def _():
            assert mf.mod(37, 3) == 1
        @it('551 % 13 = 5')
        def _():
            assert mf.mod(551, 13) == 5
    @describe('Factorial')
    def test_factorial():
        @it('0! = 1')
        def _():
            assert mf.factorial(0) == 1
        @it('1! = 1')
        def _():
            assert mf.factorial(1) == 1
        @it('2! = 2')
        def _():
            assert mf.factorial(2) == 2
        @it('3! = 6')
        def _():
            assert mf.factorial(3) == 6
        @it('10! = 3628800')
        def _():
            assert mf.factorial(10) == 3628800
    @describe('Choose')
    def test_choose():
        @it('0 choose 0 = 1')
        def _():
            assert mf.choose(0, 0) == 1
        @it('3 choose 2 = 3')
        def _():
            assert mf.choose(3, 2) == 3
        @it('10 choose 4 = 210')
        def _():
            assert mf.choose(10, 4) == 210
        @it('n choose r for r > n raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.choose(2, 3)
        @it('n choose r for n < 0 raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.choose(-3, 2)
        @it('n choose r for r < 0 raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.choose(3, -2)
    @describe('Number of Digits')
    def test_length_num():
        @it('1 => 1')
        def _():
            assert mf.length_num(1) == 1
        @it('-1 => 1')
        def _():
            assert mf.length_num(-1) == 1
        @it('1.1 => 2')
        def _():
            assert mf.length_num(1.1) == 2
        @it('43 => 2')
        def _():
            assert mf.length_num(43) == 2
        @it('-264.012 => 6')
        def _():
            assert mf.length_num(-264.012) == 6
    @describe('Echo')
    def test_echo():
        @it('1')
        def _():
            assert mf.echo(1) == '1'
        @it('-3')
        def _():
            assert mf.echo(-3) == '-3'
        @it('2.5')
        def _():
            assert mf.echo(2.5) == '2.5'
        @it('-123456789.012345')
        def _():
            assert mf.echo(-123456789.012345) == '-123456789.012345'
    @describe('Output')
    def test_output():
        from io import StringIO 
        import sys

        class Capturing(list):
            def __enter__(self):
                self._stdout = sys.stdout
                sys.stdout = self._stringio = StringIO()
                return self
            def __exit__(self, *args):
                self.extend(self._stringio.getvalue().splitlines())
                del self._stringio
                sys.stdout = self._stdout
        with Capturing() as output:
            mf.out(1)
            mf.out(24.5)
            mf.out(-34.77)
            mf.out(1234567)
        @it('1')
        def _():
            assert output[0] == '1'
        @it('24.5')
        def _():
            assert output[1] == '24.5'
        @it('-34.77')
        def _():
            assert output[2] == '-34.77'
        @it('1234567')
        def _():
            assert output[3] == '1234567'
    @describe('Percent')
    def test_percent():
        @it('10% of 40 = 4')
        def _():
            assert mf.percent(10, 40) == 4
        @it('4% of 800 = 32')
        def _():
            assert mf.percent(4, 800) == 32
        @it('92% of 3 = 2.76')
        def _():
            from math import isclose
            assert isclose(mf.percent(92, 3), 2.76)
    @describe('Digit Array')
    def test_digit_arr():
        @it('1')
        def _():
            assert mf.digit_arr(1) == [1]
        @it('-32')
        def _():
            assert mf.digit_arr(-32) == [3, 2]
        @it('32.624')
        def _():
            assert mf.digit_arr(32.624) == [3, 2, 6, 2, 4]

@describe('Matrix Functions')
def test_matrix_functions():
    import scripts.matrix_functions as mf
    @describe('Determinant')
    def test_determinant():
        @it('1x1 Matrix')
        def _():
            assert mf.determinant([[1]]) == 1
            assert mf.determinant([[2.5]]) == 2.5
            assert mf.determinant([[7]]) == 7
        @it('2x2 Matrix')
        def _():
            assert mf.determinant([[1, 2], [3, 4]]) == -2
            assert mf.determinant([[6, 4], [9, 7]]) == 6
            assert mf.determinant([[8, 3], [2, 1]]) == 2
        @it('3x3 Matrix')
        def _():
            assert mf.determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
            assert mf.determinant([[6, 8, 1], [11, 2, 0], [7, 10, 7]]) == -436
            assert mf.determinant([[1, 1, 1], [8, 7, 6], [0, 9, 99]]) == -81
        @it('5x5 Irregular Matrix')
        def _():
            assert mf.determinant([
                [6, 2, 8, 3, 7],
                [2, 8, 1, 8, 1],
                [7, 4, 11, 6, 2],
                [15, 72, 1, 11, 19],
                [22, 44, 94, 67, 1],
            ]) == -1008848
    @describe('Make Matrix (Internal)')
    def test_make_matrix():
        @it('Empty matrix raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.make_matrix([])
        @it('2x2 Matrix')
        def _():
            assert mf.make_matrix([['1', 2], [3.0, '4.0']]) == [[1.0, 2.0], [3.0, 4.0]]
        @it('3x3 Matrix')
        def _():
            assert mf.make_matrix([['1', 2, 3.0], ['4.0', 5, '6'], [7.0, '8', '9.0']]) == [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
        @it('4x4 Matrix')
        def _():
            assert mf.make_matrix([['1', 2, 3.0, '4.0'], [6, '1', 7.0, '8.6'], ['3', '2', 1, -5], [10, 11, 12.0, '-13.2']]) == [[1.0, 2.0, 3.0, 4.0], [6.0, 1.0, 7.0, 8.6], [3.0, 2.0, 1.0, -5.0], [10.0, 11.0, 12.0, -13.2]]
        @it('5x5 Matrix')
        def _():
            assert mf.make_matrix([['1', 2, 3.0, '4.0', 5], [1, '9', '-8', 3, 1.0], [3, 3, 3, 3, 3], [-9, 7, 5, 3, 1.12], ['3.33', 6.2, -1, 9, 9]]) == [[1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 9.0, -8.0, 3.0, 1.0], [3.0, 3.0, 3.0, 3.0, 3.0], [-9.0, 7.0, 5.0, 3.0, 1.12], [3.33, 6.2, -1.0, 9.0, 9.0]]
    @describe('Add')
    def test_add():
        @it('Empty matrix raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.add([], [])
        @it('2x2 Matrix')
        def _():
            assert mf.add([[1, 2], [3, 4]],[[5.2, 2], [-3, -1]]) == [[6.2, 4], [0, 3]]
        @it('3x3 Matrix')
        def _():
            assert mf.add([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 7, 4], [7.1, -2, 0], [11, -7, 2]]) == [[10, 9, 7], [11.1, 3, 6], [18, 1, 11]]
        @it('4x4 Matrix')
        def _():
            assert mf.add([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[1, -2, 3, -4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]) == [[2, 0, 6, 0], [0, 12, 0, 16], [18, 0, 22, 0], [0, 28, 0, 32]]
        @it('5x5 Matrix')
        def _():
            assert mf.add([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10.1], [11, 12, 13, 14, 15], [1.6, 17, 13, 19, 20], [21, -22, 23, 24, 25]], [[7, 7, 7, 7, 7], [8, 8, 8, 8, 8], [9, -9, 9, -9, 9], [3, 4, 5, 6, 7], [11, 12, 13, 14, 14.1]]) == [[8, 9, 10, 11, 12], [14, 15, 16, 17, 18.1], [20, 3, 22, 5, 24], [4.6, 21, 18, 25, 27], [32, -10, 36, 38, 39.1]]
    @describe('Subtract')
    def test_subtract():
        @it('Empty matrix raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.subtract([], [])
        @it('2x2 Matrix')
        def _():
            assert mf.subtract([[1, 2], [3, 4]], [[5.2, 2], [-3, -1]]) == [[-4.2, 0], [6, 5]]
        @it('3x3 Matrix')
        def _():
            assert mf.subtract([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 7, 4], [7.5, -2, 0], [11, -7, 2]]) == [[-8, -5, -1], [-3.5, 7, 6], [-4, 15, 7]]
        @it('4x4 Matrix')
        def _():
            assert mf.subtract([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[1, -2, 3, -4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]) == [[0, 4, 0, 8], [10, 0, 14, 0], [0, 20, 0, 24], [26, 0, 30, 0]]
        @it('5x5 Matrix')
        def _():
            assert mf.subtract([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10.5], [11, 12, 13, 14, 15], [1.6, 17, 13, 19, 20], [21, -22, 23, 24, 25]], [[7, 7, 7, 7, 7], [8, 8, 8, 8, 8], [9, -9, 9, -9, 9], [3, 4, 5, 6, 7], [11, 12, 13, 14, 14.1]]) == [[-6, -5, -4, -3, -2], [-2, -1, 0, 1, 2.5], [2, 21, 4, 23, 6], [-1.4, 13, 8, 13, 13], [10, -34, 10, 10, 10.9]]
    @describe('Divide')
    def test_divide():
        @it('Empty matrix raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.divide([], [])
        @it('2x2 Matrix')
        def _():
            assert mf.divide([[3, 2], [3, 4]], [[2, 2], [-4, -1]]) == [[1.5, 1], [-0.75, -4]]
        @it('3x3 Matrix')
        def _():
            assert mf.divide([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2, 1, 1], [-1, -2, 1], [2, -2, 2]]) == [[0.5, 2.0, 3.0], [-4.0, -2.5, 6.0], [3.5, -4.0, 4.5]]
        @it('4x4 Matrix')
        def _():
            assert mf.divide([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[1, -2, 1, 2], [2, 2, -1, 1], [1, 2, 1, -1], [2, 1, 1, -1]]) == [[1.0, -1.0, 3.0, 2.0], [2.5, 3.0, -7.0, 8.0], [9.0, 5.0, 11.0, -12.0], [6.5, 14.0, 15.0, -16.0]]
        @it('5x5 Matrix')
        def _():
            assert mf.divide([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10.1], [11, 12, 13, 14, 15], [1.6, 17, 13, 19, 20], [21, -22, 23, 24, 25]], [[1, 2, 2, -2, 2], [1, -2, -1, 2, 2], [-2, 1, 1, -2, 1], [-1, 2, 1, -1, -2], [-1, 2, 2, -1, -2]]) == [[1.0, 1.0, 1.5, -2.0, 2.5], [6.0, -3.5, -8.0, 4.5, 5.05], [-5.5, 12.0, 13.0, -7.0, 15.0], [-1.6, 8.5, 13.0, -19.0, -10.0], [-21.0, -11.0, 11.5, -24.0, -12.5]]
    @describe('Multiply')
    def test_multiply():
        @it('Empty matrix raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.multiply([], [])
        @it('2x2 Matrix')
        def _():
            assert mf.multiply([[1, 2], [3, 4]],[[5.5, 2], [-3, -1]]) == [[-0.5, 0], [4.5, 2]]
        @it('3x3 Matrix')
        def _():
            assert mf.multiply([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 7, 4], [7.1, -2, 0], [11, -7, 2]]) == [[56.2, -18, 10], [137.5, -24, 28], [218.8, -30, 46]]
        @it('4x4 Matrix')
        def _():
            assert mf.multiply([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[1, -2, 3, -4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]) == [[-34, 36, -38, 40], [-66, 68, -70, 72], [-98, 100, -102, 104], [-130, 132, -134, 136]]
        @it('5x5 Matrix')
        def _():
            assert mf.multiply([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10.1], [11, 12, 13, 14, 15], [1.6, 17, 13, 19, 20], [21, -22, 23, 24, 25]], [[7, 7, 7, 7, 7], [8, 8, 8, 8, 8], [9, -9, 9, -9, 9], [3, 4, 5, 6, 7], [11, 12, 13, 14, 14.1]]) == [[117, 72, 135, 90, 148.5], [308.1, 183.2, Almost(346.3), 221.4, Almost(375.41)], [497, 292, 555, 350, 599.5], [541.2, 346.2, 619.2, 424.2, 679.2], [525, 160, 623, 258, 698.5]]
    @describe('Element-Wise Multiply')
    def test_element_wise_multiply():
        @it('Empty matrix raises ValueError')
        @assert_raises(ValueError)
        def _():
            mf.element_wise_multiply([], [])
        @it('2x2 Matrix')
        def _():
            assert mf.element_wise_multiply([[1, 2], [3, 4]],[[5.2, 2], [-3, -1]]) == [[5.2, 4], [-9, -4]]
        @it('3x3 Matrix')
        def _():
            assert mf.element_wise_multiply([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 7, 4], [7.1, -2, 0], [11, -7, 2]]) == [[9, 14, 12], [28.4, -10, 0], [77, -56, 18]]
        @it('4x4 Matrix')
        def _():
            assert mf.element_wise_multiply([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[1, -2, 3, -4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]) == [[1, -4, 9, -16], [-25, 36, -49, 64], [81, -100, 121, -144], [-169, 196, -225, 256]]
        @it('5x5 Matrix')
        def _():
            assert mf.element_wise_multiply([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10.1], [11, 12, 13, 14, 15], [1.5, 17, 13, 19, 20], [21, -22, 23, 24, 25]], [[7, 7, 7, 7, 7], [8, 8, 8, 8, 8], [9, -9, 9, -9, 9], [3, 4, 5, 6, 7], [11, 12, 13, 14, 14.1]]) == [[7, 14, 21, 28, 35], [48, 56, 64, 72, 80.8], [99, -108, 117, -126, 135], [4.5, 68, 65, 114, 140], [231, -264, 299, 336, 352.5]]