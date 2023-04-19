# -- recorrer matriz de forma alterna
# -- convertir de string a numero
# -- comprobar si es substring de otro string

# 1234
# 5678
# 9876
# 1234 8765 9876

# "1234" = 1234
# "12.5" = 12.5

# "asdfgh" "ads"


def matrix_alterna(matrix: list):
    fila = 0
    col = 0

    while fila < len(matrix):
        if fila % 2 == 0:
            print(f"{matrix[fila]}")
        else:
            print(f"{matrix[fila][::-1]}")
        fila += 1


def string_to_num(num_string: str):
    num_int = 0

    if "." not in num_string:
        index = len(num_string) - 1
        while index >= 0:
            num_int += int(num_string[index]) * (10 ** (len(num_string) - index - 1))
            index -= 1
    else:
        num_string = num_string.split(".")
        num_int = string_to_num(num_string[0]) + float(f".{num_string[1]}")

    return num_int


def string_contains_substring(string: str, sub_string: str):
    index = 0
    step = len(sub_string)

    while index < len(string):
        if sub_string == string[index:index + step]:
            return True
        index += 1

    return False


if __name__ == "__main__":
    matrix_alterna([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
    print(string_to_num("123.4"))
    print(string_contains_substring("fghasdjkl", "gha"))
