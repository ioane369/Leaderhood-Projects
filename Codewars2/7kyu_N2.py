# Is n divisible by (...)?

def is_divisible(n, *args):
    for arg in args:
        if n % arg != 0:
            return False
    return True