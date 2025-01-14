import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user criteria."""
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    # Build the character pool based on user preferences
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    """Main function to interact with the user."""
    print("Welcome to the Password Generator!")
    try:
        # Get user inputs
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
