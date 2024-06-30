# Python code​​​​​​‌​‌‌​‌​‌​‌‌‌​‌​‌​‌‌‌‌‌‌​​ below

def factorial(num):
    if type(num) is not int or num < 0:
        return None

    result = 1
    for i in range(num, 0, -1):
        result *= i
    
    return result