import curses

def main(scr):
  curses.curs_set(0)
  w = scr.getmaxyx()[1]

  code_lines = [
    'def binary_search(a, key):',
    '  l, r = 0, len(a) - 1',
    '  while l <= r:',
    '    mid = (l + r) // 2',
    '    if key == a[mid]:',
    '      return mid',
    '    if key < a[mid]:',
    '      r = mid - 1',
    '    else:',
    '      l = mid + 1',
    '  return -1',
  ]
  max_code_width = max(map(len, code_lines))
  left = max_code_width + 7
  top = len(code_lines) + 1

  for y, code_line in enumerate(code_lines):
    scr.addstr(y, 2, '|')
    scr.addstr(y, 4, code_line)
    scr.addstr(y, max_code_width + 5, '|')

  def point_code_line(line_number):
    spaces = ' ' * (w - left)
    for y in range(top - 1):
      if y != line_number:
        scr.addstr(y, 0, ' ')
        scr.addstr(y, left, spaces)
      else:
        scr.addstr(y, 0, '→')
    scr.refresh()
    scr.getch()

  def add_variable(line_number, comment):
    spaces = ' ' * w
    scr.addstr(top + line_number, 0, spaces)
    scr.addstr(top + line_number, 0, comment)

  def add_calculation(line_number, msg):
    scr.addstr(line_number, left, msg)

  def binary_search(a, key):
    add_variable(0, f'a = {a}')
    add_variable(1, f'key = {key}')
    point_code_line(0)

    l, r = 0, len(a) - 1
    add_variable(2, f'l = {l}')
    add_variable(3, f'r = {r}')
    add_calculation(1, f'l = {l}, r = {len(a)} - 1 = {r}')
    point_code_line(1)

    while l <= r:
      add_calculation(2, f'{l} <= {r}, {l <= r}')
      point_code_line(2)

      mid = (l + r) // 2
      add_calculation(3, f'mid = ({l} + {r}) // 2 = {mid}')
      add_variable(4, f'mid = {mid}')
      add_variable(5, f'a[mid] = {a[mid]}')
      add_variable(6, f'Current a = {a[l:r+1]}')
      point_code_line(3)

      add_calculation(4, f'{key} == {a[mid]}, {key == a[mid]}')
      point_code_line(4)
      if key == a[mid]:

        add_calculation(5, f'return {mid}')
        point_code_line(5)
        return mid
      
      add_calculation(6, f'{key} < {a[mid]}, {key < a[mid]}')
      point_code_line(6)
      if key < a[mid]:

        r = mid - 1
        add_calculation(7, f'r = {mid} - 1 = {r}')
        add_variable(3, f'r = {r}')
        point_code_line(7)
      
      else:

        l = mid + 1
        add_calculation(9, f'l = {mid} + 1 = {l}')
        add_variable(2, f'l = {l}')
        point_code_line(9)

    add_calculation(2, f'{l} <= {r}, {l <= r}')
    point_code_line(2)
    point_code_line(10)
    return -1

  a = [1, 3, 4, 7, 8, 12, 15, 17, 19]
  key = 4
  binary_search(a, key)

curses.wrapper(main)