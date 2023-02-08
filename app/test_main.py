from main import analyzer

def test_true_positive():
    assert analyzer("test_cases/true_positive_1.py") == 0
    assert analyzer("test_cases/true_positive_2.py") == 0
    assert analyzer("test_cases/true_positive_3.py") == 0
    assert analyzer("test_cases/true_positive_4.py") == 0
    assert analyzer("test_cases/true_positive_5.py") == 0
    assert analyzer("test_cases/true_positive_6.py") == 0

def test_true_negative():
    assert analyzer("test_cases/true_negative_1.py") == -1
    assert analyzer("test_cases/true_negative_2.py") == -1


def test_false_positive():
    assert analyzer("test_cases/false_negative.py") == -1