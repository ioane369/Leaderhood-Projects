# Unique In Order

def unique_in_order(sequence):
    if sequence == "" or sequence == [] or sequence == ():
        return []
    result = [sequence[0]]
    for index in range(1, len(sequence)):
        if sequence[index] != sequence[index - 1]:
            result.append(sequence[index])
    return result