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


def dfs_pre_order(node):
    stack.append(dict())
    stack[-1]['node'] = node.data if node else None
    line_num[0] = 0
    calc_text[0] = f'def dfs_pre_order({node.data if node else None}):'
    render()

    line_num[0] = 1
    calc_text[0] = bool(node)
    render()
    if node:

        print_string[0] += f'{node.data} '
        line_num[0] = 2
        calc_text[0] = f'print({node.data}, end=\' \')'
        render()

        line_num[0] = 3
        calc_text[0] = f'dfs_pre_order({node.data}.left)'
        render()
        dfs_pre_order(node.left)

        line_num[0] = 4
        calc_text[0] = f'dfs_pre_order({node.data}.right)'
        render()
        dfs_pre_order(node.right)

    line_num[0] = 5
    calc_text[0] = ''
    render()
    stack.pop()


code_lines = [
    'def dfs_pre_order(node):',
    '    if node:',
    '        print(node.data, end=\' \')',
    '        dfs_pre_order(node.left)',
    '        dfs_pre_order(node.right)',
    '',
]


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

dfs_pre_order(root)
