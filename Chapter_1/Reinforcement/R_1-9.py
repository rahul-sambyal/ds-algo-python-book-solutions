import random


def choice(data):
    ran = random.randrange(0, len(data))
    return data[ran]
