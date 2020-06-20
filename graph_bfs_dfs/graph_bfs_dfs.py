class Node:

  def __init__(self, value):
    self.value = value
    self.neighbors = []

class Graph:

  def __init__(self):
    self.nodes = dict()
  
  def add_edge(self, node1, node2):
    if node1 not in self.nodes:
      self.nodes[node1] = Node(node1)
    if node2 not in self.nodes:
      self.nodes[node2] = Node(node2)
    self.nodes[node1].neighbors.append(self.nodes[node2])
  
  def bfs(self, start, key):
    if start not in self.nodes:
      print('Start node is not present in the graph')
      return
    
    queue = [self.nodes[start]]
    visited = {self.nodes[start]}

    while queue:

      node = queue.pop(0)

      print(node.value, end=' ')
      if node.value == key:
        print('\nKey found')
        return

      for neighbor in node.neighbors:
        if neighbor not in visited:
          queue.append(neighbor)
          visited.add(neighbor)
    
    print('\nKey not present in the graph')
  
  def dfs(self, start, key):
    if start not in self.nodes:
      print('Start node is not present in the graph')
      return
    
    stack = [self.nodes[start]]
    visited = {self.nodes[start]}

    while stack:

      node = stack.pop()

      print(node.value, end=' ')
      if node.value == key:
        print('\nKey found')
        return

      for neighbor in node.neighbors:
        if neighbor not in visited:
          stack.append(neighbor)
          visited.add(neighbor)
    
    print('\nKey not present in the graph')

g = Graph()

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)]

for node1, node2 in edges:
  g.add_edge(node1, node2)
  g.add_edge(node2, node1)

for node in g.nodes.values():
  print(node.value, [n.value for n in node.neighbors])

g.bfs(1, 7)