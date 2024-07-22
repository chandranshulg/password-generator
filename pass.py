import random
import string

def get_user_input():
    length = int(input("Enter the desired password length: "))

    use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    exclude_ambiguous = input("Exclude ambiguous characters? (yes/no): ").strip().lower() == 'yes'

    return length, use_lowercase, use_uppercase, use_digits, use_special, exclude_ambiguous

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True, exclude_ambiguous=False):
    if not (use_lowercase or use_uppercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected")

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    ambiguous = 'Il1O0'

    if exclude_ambiguous:
        lower = ''.join(c for c in lower if c not in ambiguous)
        upper = ''.join(c for c in upper if c not in ambiguous)
        digits = ''.join(c for c in digits if c not in ambiguous)
        special = ''.join(c for c in special if c not in ambiguous)

    all_characters = (
        (lower if use_lowercase else '') +
        (upper if use_uppercase else '') +
        (digits if use_digits else '') +
        (special if use_special else '')
    )

    if len(all_characters) == 0:
        raise ValueError("No character sets selected")

    password = random.choices(all_characters, k=length)
    
    random.shuffle(password)

    return ''.join(password)

length, use_lowercase, use_uppercase, use_digits, use_special, exclude_ambiguous = get_user_input()
password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special, exclude_ambiguous)
print("Generated password:", password)
