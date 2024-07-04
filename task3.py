import random
import string

def generate_random_code(length, chars=string.ascii_uppercase + string.digits):
    """Generate a random code of a given length from the given set of characters."""
    return ''.join(random.choice(chars) for _ in range(length))

def generate_code_with_format(format_str, char=string.ascii_uppercase + string.digits):
    """Generate a code based on a specific format.
    
    Format string can contain 'X' for any uppercase letter and '9' for any digit.
    """
    code = []
    for char in format_str:
        if char == 'X':
            code.append(random.choice(string.ascii_uppercase))
        elif char == '9':
            code.append(random.choice(string.digits))
        else:
            code.append(char)
    return ''.join(code)


if __name__ == "__main__":
    random_code = generate_random_code(10)
    print(f"Random alphanumeric code: {random_code}")

    format_code = generate_code_with_format("XX-999-XX")
    print(f"Code with specific format: {format_code}")

    numeric_code = generate_random_code(8, chars=string.digits)
    print(f"Random numeric code: {numeric_code}")
