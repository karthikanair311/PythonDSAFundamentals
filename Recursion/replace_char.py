"""
Python Script to Replace Characters in a String Using Recursion

This script defines a function `replaceChar` that replaces all occurrences of a specified character with another character in a string, using recursion.
It demonstrates the use of recursion in Python for character replacement within a string and includes various examples of how to use the function.

Functions:
    replaceChar(s, a, b): Replace all occurrences of character 'a' with 'b' in string 's'.
"""

def replaceChar(s, a, b):
    """
    Replace all occurrences of character 'a' with 'b' in string 's', using recursion.

    Parameters:
    - s (str): The string in which the replacement is to be performed.
    - a (str): The character to be replaced.
    - b (str): The character to replace with.

    Returns:
    str: A new string where all occurrences of 'a' have been replaced with 'b'.

    Examples:
    - replaceChar("hello world", "o", "x") returns "hellx wxrld"
    - replaceChar("dacdxcd", "c", "x") returns "daxdxxd"
    """
    if len(s) == 0:
        return s
    smallerOutput = replaceChar(s[1:], a, b)
    if s[0] == a:
        return b + smallerOutput
    else:
        return s[0] + smallerOutput

if __name__ == "__main__":
    # Example usage of the replaceChar function
    string_to_be_replaced = "dacdxcd"
    print(f"Replacing 'c' with 'x' in '{string_to_be_replaced}': {replaceChar(string_to_be_replaced, 'c', 'x')}")

    # Additional Examples
    example_string = "balloon"
    print(f"Replacing 'l' with 'z' in '{example_string}': {replaceChar(example_string, 'l', 'z')}")

    example_string = "abcdefgh"
    print(f"Replacing 'a' with 'q' in '{example_string}': {replaceChar(example_string, 'a', 'q')}")

    example_string = "123456789"
    print(f"Replacing '5' with '0' in '{example_string}': {replaceChar(example_string, '5', '0')}")
