def get_first_unique_char_index(word: str) -> int:
    """
    Gets the index of the first unique character
    If there is no unique character, return -1

    For example, if the word is 'servers' it should return 3,
    since the unique char is 'v' at position '3'.

    In another example, if the word is 'anna' it should return -1,
    since there is not unique char

    Args:
        word: a string representing a word

    Returns:
        int: index of the first unique char
    """
    unique_letters = [char for char in word if word.count(char) == 1]

    if len(unique_letters) == 0:
        return -1

    return word.index(unique_letters[0])


def main():
    assert get_first_unique_char_index(
        "hackathon") == 2, "The first unique char is 'c' in position 2"

    assert get_first_unique_char_index(
        "falafal") == -1, "The work falafal has no unique chars!"

    print("Challenge 1 is good!")


if __name__ == "__main__":
    main()
