# Isabelle Carminati

def encode_function(encode_password):
    new_encoded_password = ''
    for char in encode_password:
        char = int(char)
        new_char = char + 3
        new_char = str(new_char)
        new_encoded_password += new_char
    return new_encoded_password

def main():
    # The password encoder should take in an 8-digit password in string format containing only integers.
    # After passing the password into the encoder, the encoder stores the encoded password to a new
    # variable, with each digit being shifted up by 3 numbers.
    # Examples:
    # “12345555” will become “45678888” after encoding.
    # “00009962” will become “33332295” after encoding
    stored_encode = ''
    while True:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        menu_selection = int(input('Please enter an option: '))

        if menu_selection == 1:
            user_password = (input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
            print()
            stored_encode = encode_function(user_password)
        if menu_selection == 2:

        if menu_selection == 3:
            break


if __name__ == '__main__':
    main()
