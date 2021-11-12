from typing import Set, Tuple


def classify_uniques(word: str) -> Tuple[Set[str], Set[str]]:
    """
    Classifies the letters of a word into unique and duplicated chars
    """

    unique_letters = [char for char in word if word.count(char) == 1]
    duplicate_letters = [char for char in word if word.count(char) > 1]

    return set(unique_letters), set(duplicate_letters)


def main():
    assert classify_uniques("anna") == (set(), {"a", "n"})
    assert classify_uniques("hackathon") == (
        {'t', 'k', 'c', 'o', 'n'}, {'h', 'a'})
    print("Challenge 3 is Good! ")


if __name__ == "__main__":
    main()
