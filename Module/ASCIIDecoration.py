import pyfiglet
from termcolor import colored


msg = input("Enter the msg: ")
color = input("Enter the color: ")


valid_colors = ['red', 'green', 'yellow', 'magenta', 'cyan']

if color not in valid_colors:
    color = 'magenta'

decorated_text = pyfiglet.figlet_format(msg)

final_output = colored(decorated_text, color, attrs=['blink'])

print(final_output)
