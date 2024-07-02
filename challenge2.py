hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def hexToDec(hexNum):
    result = 0

    for idx, char in enumerate(reversed(hexNum)):
        if char not in hexNumbers:
            return None
        result += (hexNumbers[char] * (16 ** idx))
    
    return result