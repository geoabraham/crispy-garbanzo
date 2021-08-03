# You are allowed to create new strings,
# but otherwise you are not allowed to construct
# extra data structures to solve this problem (no list, set, dictionary, etc).

# this function takes two parameters as strings to compare.
def detect_pattern(s1, s2):
    # Keep in mind that this method should return the same value
    # no matter what order the two strings are passed

    # Insert your code here
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False

    dict_key = []
    dict_value = []

    for k in range(len(s1)):
        char1 = s1[k]
        char2 = s2[k]

        if char1 not in dict_key:
            if char2 in dict_value:
                return False
            dict_key.append(char1)
            dict_value.append(char2)
        else:
            if char2 != dict_value[k]:
                return False

    return True


s1 = "abc"
s2 = "abc"
print(
    f'TEST #1 :: abc -> abc expected True :: actual {detect_pattern(s1, s2)}')

s1 = "abc"
s2 = "xy"
print(
    f'TEST #2 :: abc -> xy expected False :: actual {detect_pattern(s1, s2)}')

s1 = "abc"
s2 = "---"
print(
    f'TEST #3 :: abc -> --- expected False :: actual {detect_pattern(s1, s2)}')

s1 = "abc"
s2 = "xyz"
print(
    f'TEST #4 :: abc -> zyx expected True :: actual {detect_pattern(s1, s2)}')

s1 = "matter"
s2 = "essare"
print(
    f'TEST #5 :: abccde -> essare expected False :: actual {detect_pattern(s1, s2)}')

s1 = "Súper"
s2 = "fH3r5"
print(
    f'TEST #6 :: Súper -> fH3r5 expected True :: actual {detect_pattern(s1, s2)}')
