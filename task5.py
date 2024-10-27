import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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

def draw_tree(tree_root, bfs_nodes, dfs_nodes):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    initial_color = 'skyblue'

    # BFS Traversal
    plt.figure(figsize=(16, 8))
    plt.subplot(1, 2, 1)
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=initial_color)
    plt.title('BFS Traversal')

    for step, node in enumerate(bfs_nodes, 1):
        node.color = color_gradient(step, len(bfs_nodes))
        tree.nodes[node.id]['color'] = node.color
        colors = [tree.nodes[n]['color'] for n in tree.nodes]
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.pause(0.5)

    # Reset colors to initial color
    for node in tree.nodes:
        tree.nodes[node]['color'] = initial_color

    # DFS Traversal
    plt.subplot(1, 2, 2)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=initial_color)
    plt.title('DFS Traversal')

    for step, node in enumerate(dfs_nodes, 1):
        node.color = color_gradient(step, len(dfs_nodes))
        tree.nodes[node.id]['color'] = node.color
        colors = [tree.nodes[n]['color'] for n in tree.nodes]
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.pause(0.5)

    plt.show()

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def array_to_heap_tree(arr):
    if not arr:
        return None
    n = len(arr)
    build_heap(arr)
    nodes = [Node(arr[i]) for i in range(n)]
    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def color_gradient(step, total_steps):
    hsv_color = (step / total_steps, 0.8, 0.8)
    rgb_color = colorsys.hsv_to_rgb(*hsv_color)
    return '#%02x%02x%02x' % tuple(int(c * 255) for c in rgb_color)

def bfs(root):
    queue = [root]
    visited_nodes = []
    while queue:
        node = queue.pop(0)
        visited_nodes.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited_nodes

def dfs(root):
    stack = [root]
    visited_nodes = []
    while stack:
        node = stack.pop()
        visited_nodes.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited_nodes

def main():
    arr = [0, 4, 1, 5, 10, 3]
    root = array_to_heap_tree(arr)
    bfs_nodes = bfs(root)
    dfs_nodes = dfs(root)
    draw_tree(root, bfs_nodes, dfs_nodes)

if __name__ == "__main__":
    main()
