# Python code​​​​​​‌​‌‌​‌​‌‌‌‌​‌​​‌‌‌‌‌​​‌​‌ below
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)


def square(num):
    # - Get first half of triangle
    result = triangle(num)

    # - Get second half of triangle
    for i in range(num, 0, -1):
        result += num - i
    return result