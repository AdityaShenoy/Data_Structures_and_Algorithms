import curses

def main(scr):
  curses.curs_set(0)
  w = scr.getmaxyx()[1]

  code_lines = [
    'def fibo(n):',
    '  if n in [0, 1]:',
    '    return n',
    '  return fibo(n - 1) + fibo(n - 2)',
  ]
  max_code_width = max(map(len, code_lines))

  for y, code_line in enumerate(code_lines):
    scr.addstr(y, 2, '|')
    scr.addstr(y, 4, code_line)
    scr.addstr(y, max_code_width + 5, '|')

  def point_code_line(line_number):
    for y in range(len(code_lines)):
      scr.addstr(y, 0, '→' if y == line_number else ' ')
    scr.refresh()
    scr.getch()

  def clear_comments():
    spaces = ' ' *  (w - max_code_width - 7)
    for y in range(len(code_lines)):
      scr.addstr(y, max_code_width + 7, spaces)

  def add_comment(line_number, comment):
    spaces = ' ' *  (w - max_code_width - 7)
    scr.addstr(line_number, max_code_width + 7, spaces)
    scr.addstr(line_number, max_code_width + 7, comment)


  def revert_comments(stack):
    spaces = ' ' *  (w - max_code_width - 7)
    for y in range(len(code_lines)):
      add_comment(y, stack[-1].get(y, spaces))

  stack = []

  def fibo(n):
    
    stack.append(dict())
    clear_comments()

    stack[-1][0] = f'n = {n}'
    add_comment(0, stack[-1][0])
    point_code_line(0)

    stack[-1][1] = f'{n in [0, 1]}'
    add_comment(1, stack[-1][1])
    point_code_line(1)
    if n in [0, 1]:

      stack.pop()
      add_comment(2, f'Returning {n}')
      point_code_line(2)
      return n
    
    stack[-1][3] = f'Calling fibo(n - 1) = fibo({n - 1})'
    add_comment(3, stack[-1][3])
    point_code_line(3)
    fibo1 = fibo(n - 1)
    revert_comments(stack)

    stack[-1][3] = f'Calling fibo(n - 2) = fibo({n - 2})'
    add_comment(3, stack[-1][3])
    point_code_line(3)
    fibo2 = fibo(n - 2)
    revert_comments(stack)

    stack.pop()
    add_comment(3, 'Returning fibo(n - 1) + fibo(n - 2) = ' + \
      f'{fibo1} + {fibo2} = {fibo1 + fibo2}')
    point_code_line(3)
    return fibo1 + fibo2
  
  fibo(3)

curses.wrapper(main)