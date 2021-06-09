
#importing 

from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series



#test version

def test_version():
    assert __version__ == '0.1.0'



# Testing for Fibancci function 
def test_fibonacci_0():
    excepted =0 
    actual = fibonacci(0)
    assert excepted == actual

def test_fibonacci_1() :
    excepted =1 
    actual = fibonacci(1)
    assert excepted == actual

def test_fibonacci_2() :
    excepted =1 
    actual = fibonacci(2)
    assert excepted == actual   

def test_fibonacci_3() :
    excepted =2 
    actual = fibonacci(3)
    assert excepted == actual     




# Testing for Lucas function 
def test_lucas_0():
    excepted =2 
    actual = lucas(0)
    assert excepted == actual

def test_lucas_1() :
    excepted =1 
    actual = lucas(1)
    assert excepted == actual

def test_lucas_2() :
    excepted =3 
    actual = lucas(2)
    assert excepted == actual   

def test_lucas_3() :
    excepted =4 
    actual = lucas(3)
    assert excepted == actual   



# Testing for sum_series function  
def test_sum_series_0():
    excepted =1
    actual = sum_series(1)
    assert excepted == actual

def test_sum_series_1() :
    excepted = 1
    actual = sum_series(2)
    assert excepted == actual

def test_sum_series_2() :
    excepted = 9
    actual = sum_series(3,3,3)
    assert excepted == actual   

def test_sum_series_3() :
    excepted = 20
    actual = sum_series(4,4,4)
    assert excepted == actual   



   


