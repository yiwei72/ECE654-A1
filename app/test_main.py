from main import main_method

def test_true_positive():
    assert main_method("test_cases/true_positive_1.py") == True
    assert main_method("test_cases/true_positive_2.py") == True
    assert main_method("test_cases/true_positive_3.py") == True
    assert main_method("test_cases/true_positive_4.py") == True
    assert main_method("test_cases/true_positive_5.py") == True
    assert main_method("test_cases/true_positive_6.py") == True

def test_true_negative():
    assert main_method("test_cases/true_negative.py") == False
    
def test_false_positive():
    assert main_method("test_cases/false_positive.py") == True

def test_false_positive():
    assert main_method("test_cases/false_negative.py") == False