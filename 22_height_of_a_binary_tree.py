def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1
