import random
import string

def generate(length, num_count, alpha_count, special_count, excluded):
    # Initialize an empty string
    result = ""

    # Generate random numbers
    numbers = [random.choice(string.digits) for _ in range(num_count)]
    result += ''.join(numbers)

    # Generate random alphabets (both lowercase and uppercase combined)
    alphabets = [random.choice(string.ascii_letters) for _ in range(alpha_count)]
    result += ''.join(alphabets)

    # Generate random special characters
    special_chars = [random.choice(string.punctuation) for _ in range(special_count)]
    result += ''.join(special_chars)

    # Create a list of appropriate characters
    apt_chars = ''.join(c for c in string.printable if c not in excluded)
    
    # Filter the generated string
    result = ''.join(c for c in result if c not in excluded)
    
    # Adjusts the remaining length    
    remaining_length = length - len(result)

    # Generates the string excluding the characters
    random_chars = [random.choice(apt_chars) for _ in range(remaining_length)]
    result += ''.join(random_chars)

    # Shuffle the string to ensure randomness
    result = ''.join(random.sample(result, length))

    return result

# Example usage
length = 20
x = 3  # Number of numbers
y = 4  # Number of combined alphabets (lowercase and uppercase)
z = 7  # Number of special characters
excluded = ["1", "2", "*", 1]

result = generate(length, x, y, z, excluded)
print(result)
