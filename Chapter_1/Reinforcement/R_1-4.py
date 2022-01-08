def sum_of_squares(n):
    sum = 0
    for i in range(2, n, 2):
        sum += i*i
    return sum
