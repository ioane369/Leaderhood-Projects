# Anagram Detection

def is_anagram(test, original):
    if len(test) != len(original):
        return False
    
    for char in test.lower():
        if char not in original.lower():
            return False
    return True