#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.
    Args:
        text (str): The text to be printed.
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in "?:.":
        words = text.replace(delimiter, delimiter + "\n\n")
        text = (delimiter + "\n\n").join([index.strip(" ") for index in words.split(delimiter)])

    print(text)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
