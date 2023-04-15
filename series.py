

#in recursion
def fibonacci(n):
    """
    we use fabonacci to calculate the summation of the last two numbers, we call the function itself to loop 
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def lucas(n):
    """
    we use lucas to calculate the summation of the last two numbers, we call the function itself to loop 
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(n,a=0,b=1):
    """
    here is a general methon to calculate the summation of the last two numbers and you should specify the first two numbers
    """
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return sum_series(n-1,a,b)+sum_series(n-2,a,b)

result=sum_series(0,2,1)
print(result)