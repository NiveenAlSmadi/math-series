
# ---------------------------------------------fibonacci function--------------------------------------------------
"""
 fibonacci for sum serise with first value 0 for n=0 and 1 for n =1
 implimenting function using : recursion.

"""
def fibonacci(n):


    if n==0:
        return 0
    elif n==1:
        return 1    
    return fibonacci(n-1)+fibonacci(n-2)




#------------------------------------------------------lucas function -------------------------------------------------



"""

lucas for sum serise with first value 2 for n=0 and 1 for n =1
implimenting function using : recursion.

"""
def lucas(n):


    if n==0:
        return 2
    elif n==1 :
        return 1   
    return lucas(n-1)+lucas(n-2)





# ----------------------------------------------------sum_series function -----------------------------------------------------

"""

 function cheack if the  input  fibonacci or lucas or the sum of both.......
 n  index use to make a serise
 n1  for  determine the base case for index 0
 n2  for determine the base case for index 1

"""
def sum_series(n,n1=0,n2=1):


    if n==0:
        return n1
    elif n==1:
        return n2
    return sum_series(n-1,n1,n2)+sum_series(n-2,n1,n2)      


