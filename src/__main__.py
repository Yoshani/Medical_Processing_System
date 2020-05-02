from src.authentication.signup import SignUp
from src.app import main

if __name__ == '__main__':

    n = input("Press 1 to login or 2 to signup: ")
    if n == '1':
        main()
    elif n == '2':
        SignUp().create_user()
        print("Login to your account")
        main()
    else:
        print("Invalid input")

