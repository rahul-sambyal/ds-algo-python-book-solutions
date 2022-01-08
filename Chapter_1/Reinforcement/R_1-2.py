def is_even(k):
    even = True
    while k > 0:
        if even:
            even = False
        elif not even:
            even = True
        k -= 1
    return even
