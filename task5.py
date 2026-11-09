import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

def dfs(root):
  if root is None:
    return []

  stack = [root]
  order = []

  while stack:
    node = stack.pop()
    order.append(node)

    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)

  return order

def bfs(root):
  if root is None:
    return []

  queue = deque([root])
  order = []

  while queue:
    node = queue.popleft()
    order.append(node)

    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)

  return order

def visualize_traversal(root, order, title):
  if not order:
    print(f"{title} traversal order is empty.")
    return

  # Цей цикл тільки скидає кольори.
  for node in order:
    node.color = "#D3D3D3"

  tree = nx.DiGraph()
  pos = {root.id: (0, 0)}
  add_edges(tree, root, pos)

  labels = {
    node_id: data["label"]
    for node_id, data in tree.nodes(data=True)
  }

  fig, ax = plt.subplots(figsize=(8, 5))

  for step, node in enumerate(order):
    if not plt.fignum_exists(fig.number):
      return

    brightness = 50 + int(
      180 * step / max(1, len(order) - 1)
    )

    node.color = f"#{brightness:02x}{brightness:02x}FF"
    tree.nodes[node.id]["color"] = node.color

    colors = [
      data["color"]
      for _, data in tree.nodes(data=True)
    ]

    ax.clear()

    nx.draw(
      tree,
      pos=pos,
      labels=labels,
      arrows=False,
      node_size=2500,
      node_color=colors,
      ax=ax,
    )

    ax.set_title(
      f"{title}: step {step + 1}/{len(order)}, "
      f"visiting node {node.val}"
    )
    ax.margins(0.2)
    plt.pause(0.7)

  plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
# draw_tree(root)

dfs_order = dfs(root)
print("DFS traversal order:", [node.val for node in dfs_order])
visualize_traversal(root, dfs_order, "DFS")

bfs_order = bfs(root)
print("BFS traversal order:", [node.val for node in bfs_order])
visualize_traversal(root, bfs_order, "BFS")