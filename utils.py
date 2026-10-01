def is_palindrome(s):
    """Check whether a string reads the same forwards and backwards.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, otherwise False.
    """
    normalized = s.lower()
    return normalized == normalized[::-1]


def count_words(text):
    """Count the words in a string.

    Args:
        text: The string whose words should be counted.

    Returns:
        The number of words in the string.
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a Celsius temperature to Fahrenheit.

    Args:
        c: The temperature in degrees Celsius.

    Returns:
        The temperature in degrees Fahrenheit.
    """
    return (c * 9 / 5) + 32