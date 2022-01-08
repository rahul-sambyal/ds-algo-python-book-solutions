def minmax(data):
    min = data[0]
    max = data[0]
    for num in data[1:]:
        if num < min:
            min = num
        if num > max:
            max = num
    return (min, max)
