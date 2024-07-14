# How many are smaller than me?

def smaller(arr):
    result = []
    for index in range(len(arr)):
        count = 0
        for i in range(index + 1, len(arr)):
            if arr[i] < arr[index]:
                count += 1
        result.append(count)
    return result