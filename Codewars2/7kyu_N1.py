# Currying functions: multiply all elements in an array

def multiply_all(arr):
    def multiplier(factor):
        res = []
        for num in arr:
            res.append(num * factor)
        return res
    return multiplier