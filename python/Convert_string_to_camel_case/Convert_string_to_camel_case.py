def to_camel_case(text):
    text = text.replace('-', ' ').replace('_', ' ')  # Replace delimiters with spaces
    words = text.split()  # Split into words
    return words[0] + ''.join(word.capitalize() for word in words[1:]) if words else ""  # Combine with camel case
