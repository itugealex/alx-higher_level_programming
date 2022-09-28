#!/usr/bin/python3
"""writes string to a text file"""

def write_file(filename = "", text = ""):
    """writes file
    Args:
        filename: name of the file to write.
        text: text to write to file.
    Returns:
        Number of characters written.
    """
    with open(file, encoding = "utf-8") as f:
        f.write(text)
    return len(text)
