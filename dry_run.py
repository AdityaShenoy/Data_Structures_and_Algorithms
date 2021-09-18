from IPython.display import clear_output


class Debugger:
    def __init__(self, code_lines, auto_step=0):
        self.stack = [dict()]
        self.print_string = ''
        self.code_lines = code_lines
        self.auto_step = auto_step

    def render(self, line_num, vars=dict(), calc_text='', print_string=''):
        clear_output()
        self.stack[-1] = {**self.stack[-1], **vars}

        print('• CODE')
        for code_line_number, code_line in enumerate(self.code_lines):
            print(('→ ' if code_line_number == line_num else '  ') + code_line)

        print('\n• VARIABLES')
        if self.stack:
            for key, value in self.stack[-1].items():
                print(f'{key} = {value}')

        if calc_text:
            print('\n• CALCULATIONS')
            print(calc_text)

        self.print_string += print_string
        if self.print_string:
            print('\n• PRINT OUTPUT')
            print(self.print_string)

        if len(self.stack) > 1:
            print('\n• RECURSION STACK')
            print(self.stack)

        input('Press enter to continue')
