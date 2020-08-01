import os


stack = []
line_num = [0]
calc_text = ['']
print_string = ['']


def render():
    os.system('cls')

    print('• CODE')
    for code_line_number, code_line in enumerate(code_lines):
        print('→ ' if code_line_number == line_num[0] else '  ', end='')
        print(code_line)

    print('\n• CALCULATIONS')
    print(calc_text[0])

    print('\n• VARIABLES')
    if stack:
        for key, value in stack[-1].items():
            print(f'{key} = {value}')

    print('\n• PRINT OUTPUT')
    print(print_string[0])

    print('\n• RECURSION STACK')
    print(stack)

    input()
