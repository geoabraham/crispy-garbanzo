def check_balance(brackets):
    balanced = 0
    for bracket in brackets:
        if bracket == '[':
            balanced += 1
        elif bracket == ']':
            balanced -= 1

    return balanced == 0


bracket_string = '[[[[]]]]'

print(check_balance(bracket_string))
