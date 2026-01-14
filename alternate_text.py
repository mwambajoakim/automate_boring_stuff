#!/usr/bin/env python3
import pyperclip
pyperclip.set_clipboard('wl-clipboard')


if __name__ == '__main__':
    print("Script Started...")
    print()
    text = pyperclip.paste()
    alt_text = ''
    make_uppercase = True

    for character in text:
        if make_uppercase:
            alt_text += character.upper()
        else:
            alt_text += character.lower()

        make_uppercase = not make_uppercase
    pyperclip.copy(alt_text)
    print(alt_text)
    print()
    print('End of Script')
