# Luck check

def luck_check(st):
    numbers = "1234567890"
    for char in st:
        if char not in numbers:
            raise ValueError
        
    length = len(st) // 2
    sum1 = 0
    sum2 = 0    
    if len(st) % 2 != 0:
        for num in st[: length]:
            sum1 += int(num)
        for num in st[length + 1: ]:
            sum2 += int(num)
        return sum1 == sum2
    else:
        for num in st[: length]:
            sum1 += int(num)
        for num in st[length: ]:
            sum2 += int(num)
        return sum1 == sum2