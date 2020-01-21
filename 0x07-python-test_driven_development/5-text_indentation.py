#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """

    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = "".join([w if w not in ".?:" else w + "\n\n" for w in text])
    newone = "\n".join([l.strip() for l in s.split("\n")])
    print(newone)
