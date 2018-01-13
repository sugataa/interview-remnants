from increment import increment

# You can run these tests on the command line as follows:
# pytest test_increment.py
#
# Individual tests can be selected with the -k flag:
# pytest -k test_increment_zero test_increment.py
#
def test_increment_from_zero():
    assert increment([0]) == [1]

def test_increment_to_zero():
    assert increment([-1]) == [0]

def test_increment_negative():
    assert increment([-1, 9]) == [-1, 8]

def test_increment_positive():
    assert increment([1, 8]) == [1, 9]

def test_increment_rollover_msd():
    assert increment([2, 9, 9, 9]) == [3, 0, 0, 0]

def test_increment_rollover_lsd():
    assert increment([1, 9, 9]) == [2, 0, 0]

def test_increment_rollover_msd_and_lsd_positive():
    assert increment([9, 9, 9]) == [1, 0, 0, 0]

def test_increment_rollover_msd_and_lsd_negative():
    assert increment([-1, 0, 0, 0]) == [-9, 9, 9]

def test_increment_rollover_middle():
    assert increment([1, 8, 9]) == [1, 9, 0]
