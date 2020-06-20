import curses

def main(scr):
  curses.curs_set(0)
  w = scr.getmaxyx()[1]

  code_lines = [
    'node = queue.pop()',
    'print(node.value, end=\' \')',
    'if node.value == key:',
    '  print(\'\\nKey found\')',
    '  return',
    '',
    'for neighbor in node.neighbors:',
    '  if neighbor not in visited:',
    '    queue.append(neighbor)',
    '    visited.add(neighbor)',
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

  class Node:

    def __init__(self, value):
      self.value = value
      self.neighbors = []

  class Graph:

    def __init__(self):
      self.nodes = dict()
    
    def addEdge(self, node1, node2):
      if node1 not in self.nodes:
        self.nodes[node1] = Node(node1)
      if node2 not in self.nodes:
        self.nodes[node2] = Node(node2)
      self.nodes[node1].neighbors.append(self.nodes[node2])
    
    def bfs(self, start, key):
      if start not in self.nodes:
        print('Node not present in the graph')
        return
      
      visited = set()

      queue = [self.nodes[start]]
      visited.add(self.nodes[start])

      print_string = ''
      add_comment(9, f'visited = { {x.value for x in visited} }')

      while queue:

        node = queue.pop()
        add_comment(0, f'queue = {[x.value for x in queue]} node = {node.value}')
        add_comment(2, '')
        add_comment(6, '')
        add_comment(7, '')
        point_code_line(0)

        print_string += f'{node.value} '
        add_comment(1, print_string)
        point_code_line(1)
        
        add_comment(2, f'key = {key}, {node.value == key}')
        point_code_line(2)
        if node.value == key:

          print_string += ' Key found'
          add_comment(1, print_string)
          point_code_line(3)

          point_code_line(4)
          return

        for neighbor in node.neighbors:
          add_comment(6, f'neighbor = {neighbor.value}')
          add_comment(7, f'     ')
          point_code_line(6)

          add_comment(7, f'{neighbor not in visited}')
          point_code_line(7)
          if neighbor not in visited:

            queue.append(neighbor)
            add_comment(0, f'queue = {[x.value for x in queue]} node = {node.value}')
            point_code_line(8)

            visited.add(neighbor)
            add_comment(9, f'visited = { {x.value for x in visited} }')
            point_code_line(9)
    
  g = Graph()

  edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)]
  for node1, node2 in edges:
    g.addEdge(node1, node2)
    g.addEdge(node2, node1)

  g.bfs(1, 6)

curses.wrapper(main)