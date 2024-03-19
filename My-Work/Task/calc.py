def add(num1, num2):
    """this method defines the addition of two values"""
    return (num1 + num2)

def sub(num1,num2):
    """this method defines the subtrction of two values"""
    return(num1-num2)

def mul(num1,num2):
    """this method defines the multipiation of two values"""
    if num1 < num2:
        print("No negative values to be entered")
    return(num1*num2)

def division(num1,num2):
    """this method defines the division of two values """
    if num2==0:
        print("Zero Division Error")
    return(num1/num2)

def percent(num1,num2):
    """this method defines the percentage of two values"""
    return(num1/100*num2)
