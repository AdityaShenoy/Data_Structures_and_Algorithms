import os


class Debugger:
    def __init__(self):
        self.stack = []
        self.line_num = 0
        self.calc_text = ''
        self.print_string = ''
        self.code_lines = []

    def render(self):
        os.system('cls')

        print('• CODE')
        for code_line_number, code_line in enumerate(self.code_lines):
            print('→ ' if code_line_number == self.line_num else '  ',
                  end='')
            print(code_line)

        print('\n• CALCULATIONS')
        print(self.calc_text)

        print('\n• VARIABLES')
        if self.stack:
            for key, value in self.stack[-1].items():
                print(f'{key} = {value}')

        print('\n• PRINT OUTPUT')
        print(self.print_string)

        print('\n• RECURSION STACK')
        print(self.stack)

        input()


dry_run = Debugger()
