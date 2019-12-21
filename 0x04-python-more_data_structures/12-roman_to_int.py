#!/usr/bin/python3
def roman_to_int(roman_string):
    def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    numbers = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }
    listado = []
    for valor in roman_string:
        for key, value in numbers.items():
            if valor == key:
                listado.append(value)
    numlet = len(listado)
    if numlet <= 0:
        return None
    result = 0
    for i in range(numlet):
        if i > 0 and listado[i] > listado[i-1]:
            result += listado[i] - 2 * listado[i-1]
        else:
            result += listado[i]
    return result

