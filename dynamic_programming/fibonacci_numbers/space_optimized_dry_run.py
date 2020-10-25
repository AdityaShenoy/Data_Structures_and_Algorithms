import curses

def main(scr):
  curses.curs_set(0)
  w = scr.getmaxyx()[1]

  code_lines = [
    'def fibo(n):',
    '  if n in [0, 1]:',
    '    return n',
    '  dp = [0, 1]',
    '  for i in range(2, n+1):',
    '    dp.append(dp[-1] + dp[-2])',
    '    del dp[0]',
    '  return dp[-1]',
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

  def add_comment(line_number, comment):
    spaces = ' ' *  (w - max_code_width - 7)
    scr.addstr(line_number, max_code_width + 7, spaces)
    scr.addstr(line_number, max_code_width + 7, comment)

  def fibo(n):
    add_comment(0, f'n = {n}')
    point_code_line(0)

    add_comment(1, f'{n in [0, 1]}')
    point_code_line(1)
    if n in [0, 1]:

      add_comment(2, f'Returning {n}')
      point_code_line(2)
      return n
    
    dp = [0, 1]
    add_comment(3, f'dp = {dp}')
    point_code_line(3)

    for i in range(2, n+1):
      add_comment(4, f'i = {i}')
      add_comment(5, '')
      add_comment(6, '')
      point_code_line(4)

      dp.append(dp[-1] + dp[-2])
      add_comment(5, f'Appending {dp[-2]} + {dp[-3]} = {dp[-1]} to dp')
      add_comment(3, f'dp = {dp}')
      point_code_line(5)

      del dp[0]
      add_comment(6, f'Deleting 1st element from dp')
      add_comment(3, f'dp = {dp}')
      point_code_line(6)
    
    add_comment(7, f'Returning {dp[-1]}')
    point_code_line(7)
    return dp[-1]
  
  fibo(3)

curses.wrapper(main)