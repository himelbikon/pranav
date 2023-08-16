import random


def generate_password():
    password = ''

    for i in range(10):
        random_char = random.choice(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

        password += random_char

    return password


# print('=============================')
# print('__name__ :', __name__)
# print('=============================')
if __name__ == '__main__':
    print('********************************')
    print('********************************')
    print('********************************')
    print('********************************')
    print('********************************')


# if __name__ == '__main__':
#     print('Program has ended')

# password = password_generator()

# print('=============================')
# print('Your new password is:', password)
# print('=============================')
