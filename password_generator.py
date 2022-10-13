import random

def password(a, b, c, d, e, length, count_password):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    password = ''
    lst_passw = []

    def generate_password(length, chars):
        password = ''
        for _ in range(int(length)):
            password += random.choice(chars)
        return password


    if a == '1':
        chars += digits
    if b == '1':
        chars += lowercase_letters
    if c == '1':
        chars += uppercase_letters
    if d == '1':
        chars += punctuation
    if e == '1':
        for c in 'il1Lo0':
            chars = chars.replace(c, '')

    for _ in range(int(count_password)):
        lst_passw.append(generate_password(length, chars))

    return lst_passw