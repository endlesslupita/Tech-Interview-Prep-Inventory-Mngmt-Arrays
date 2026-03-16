from solution import zero_duplicate

def test_normal_case_1():
        assert zero_duplicate([3 0, 2]) == [3, 0, 0]

def test_normal_case_2():
        assert zero_duplicate([1, 1, 1, 0]) == [1, 1, 1, 0]

def test_normal_case_3():
        assert zero_duplicate([0, 9, 5, 0, 3, 0, 0, 2, 5, 8]) == [0, 0, 9, 5, 0, 3, 0, 0, 0, 0]

def test_edge_case_1():
#empty list
        assert zero_duplicate([]) == []

def test_edge_case_3():
#one number
        assert zero_duplicate([5]) == [5]

def test_edge_case_3():
#no zeros
        assert zero_duplicate([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

