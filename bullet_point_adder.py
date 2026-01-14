#!/usr/bin/env python3
import pyperclip
pyperclip.set_clipboard('wl-clipboard')


if __name__ == '__main__':
    text = pyperclip.paste()
    text = text.replace('\\n', '\n')
    lines = text.split('\n')

    for i in range(len(lines)):
        lines[i] = '* ' + lines[i]
    text = '\n'.join(lines)

    print(text)
    pyperclip.copy(text)
