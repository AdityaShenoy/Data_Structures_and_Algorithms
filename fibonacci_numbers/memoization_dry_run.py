import curses

def main(scr):
  curses.curs_set(0)
  w = scr.getmaxyx()[1]

  code_lines = [
    'def fibo(n):',
    '  return fibo_memo(n, dict())',
    '',
    'def fibo_memo(n, dp):',
    '  if n in dp:',
    '    return dp[n]',
    '  if n in [0, 1]:',
    '    dp[n] = n',
    '  else:',
    '    dp[n] = fibo_memo(n - 1, dp) + fibo_memo(n - 2, dp)',
    '  return dp[n]',
  ]
  global_lines = [0, 1]
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
      if y not in global_lines:
        scr.addstr(y, max_code_width + 7, spaces)

  def add_comment(line_number, comment):
    spaces = ' ' *  (w - max_code_width - 7)
    scr.addstr(line_number, max_code_width + 7, spaces)
    scr.addstr(line_number, max_code_width + 7, comment)


  def revert_comments(stack):
    spaces = ' ' *  (w - max_code_width - 7)
    for y in range(len(code_lines)):
      if y not in global_lines:
        add_comment(y, stack[-1].get(y, spaces))


  def fibo(n):
    add_comment(0, f'n = {n}')
    point_code_line(0)

    return fibo_memo(n, dict())

  stack = []

  def fibo_memo(n, dp):
    clear_comments()
    stack.append(dict())
    stack[-1][3] = f'n = {n}, dp contains results of {list(dp.keys())}'
    add_comment(3, stack[-1][3])
    point_code_line(3)

    stack[-1][4] = f'{n in dp}'
    add_comment(4, stack[-1][4])
    point_code_line(4)
    if n in dp:

      stack.pop()
      add_comment(5, f'Returning {dp[n]}')
      point_code_line(5)
      return dp[n]
    
    stack[-1][6] = f'{n in [0, 1]}'
    add_comment(6, stack[-1][6])
    point_code_line(6)
    if n in [0, 1]:

      dp[n] = n
      stack[-1][7] = f'Added {n}\'s result to dp'
      add_comment(1, f'{dp}')
      add_comment(7, stack[-1][7])
      point_code_line(7)

    else:

      stack[-1][9] = f'Calling fibo_memo(n - 1, dp) = fibo({n - 1}, dp)'
      add_comment(9, stack[-1][9])
      point_code_line(9)
      fibo1 = fibo_memo(n - 1, dp)
      revert_comments(stack)

      stack[-1][9] = f'Calling fibo_memo(n - 2, dp) = fibo({n - 2}, dp)'
      add_comment(9, stack[-1][9])
      point_code_line(9)
      fibo2 = fibo_memo(n - 2, dp)
      revert_comments(stack)

      dp[n] = fibo1 + fibo2
      stack[-1][9] = f'Added {n}\'s result {fibo1} + {fibo2} = {dp[n]} to dp'
      add_comment(1, f'{dp}')
      add_comment(9, stack[-1][9])
      point_code_line(9)
    
    stack.pop()
    add_comment(10, f'Returning {dp[n]}')
    point_code_line(10)
    return dp[n]
  
  fibo(3)

curses.wrapper(main)