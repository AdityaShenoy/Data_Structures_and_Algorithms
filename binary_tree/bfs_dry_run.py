import os


stack = []
line_number = [0]
calculation_text = ['']
print_string = ['']


def render():
    os.system('cls')

    print('• CODE')
    for code_line_number, code_line in enumerate(code_lines):
        print('→ ' if code_line_number == line_number[0] else '  ', end='')
        print(code_line)

    print('\n• CALCULATIONS')
    print(calculation_text[0])

    print('\n• VARIABLES')
    if stack:
        for key, value in stack[-1].items():
            print(f'{key} = {value}')

    print('\n• PRINT OUTPUT')
    print(print_string[0])

    input()


def bfs(root):
    stack.append(dict())
    stack[-1]['root'] = root.data
    line_number[0] = 0
    calculation_text[0] = f'def bfs({root.data if root else None})'
    render()

    line_number[0] = 1
    calculation_text[0] = bool(root)
    render()
    if root:

        queue = [root]
        stack[-1]['queue'] = [n.data for n in queue]
        line_number[0] = 2
        calculation_text[0] = f'queue = [{root.data}]'
        render()

        line_number[0] = 3
        calculation_text[0] = bool(queue)
        render()
        while queue:

            line_number[0] = 4
            calculation_text[0] = f'node = {[n.data for n in queue]}.pop(0)'
            node = queue.pop(0)
            stack[-1]['queue'] = [n.data for n in queue]
            stack[-1]['node'] = node.data
            render()

            print_string[0] += f'{node.data} '
            line_number[0] = 5
            calculation_text[0] = f'print({node.data}, end=\' \')'
            render()

            line_number[0] = 6
            calculation_text[0] = bool(node.left)
            render()
            if node.left:

                line_number[0] = 7
                calculation_text[0] = f'{[n.data for n in queue]}' +\
                    f'.append({node.left.data})'
                queue.append(node.left)
                stack[-1]['queue'] = [n.data for n in queue]
                render()

            line_number[0] = 8
            calculation_text[0] = bool(node.right)
            render()
            if node.right:

                line_number[0] = 9
                calculation_text[0] = f'{[n.data for n in queue]}' +\
                    f'.append({node.right.data})'
                queue.append(node.right)
                stack[-1]['queue'] = [n.data for n in queue]
                render()

    stack.pop()
    line_number[0] = 10
    calculation_text[0] = ''
    render()


code_lines = [
    'def bfs(root):',
    '    if root:',
    '        queue = [root]',
    '        while queue:',
    '            node = queue.pop(0)',
    '            print(node.data, end=' ')',
    '            if node.left:',
    '                queue.append(node.left)',
    '            if node.right:',
    '                queue.append(node.right)',
    ''
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

bfs(root)
