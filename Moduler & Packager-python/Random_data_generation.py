import random
import string


def generate_random_number():
    return random.randint(1, 100)

def generate_random_list():
    length = int(input("Enter the length of the list: "))
    return [random.randint(1, 100) for _ in range(length)]

def create_random_password():
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_otp():
    return ''.join(random.choices(string.digits,k=6))

def main():
    while True:
        print("Random Date Generator")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("=" * 30)
            print("Random Number:-",generate_random_number())
            print("=" * 30)
        elif choice == 2:
            print("=" * 30)
            print("Random List:-",generate_random_list())
            print("=" * 30)
        elif choice == 3:
            print("=" * 30)
            print("Random Passsword:-",create_random_password())
            print("=" * 30)
        elif choice == 4:
            print("=" * 30)
            print("Random OTP:-",generate_random_otp())
            print("=" * 30)
        elif choice == 5:
            break
        else:
            print("=" * 30)
            print("Invalid choice")
            print("=" * 30)

if __name__ == "__main__":
    main()