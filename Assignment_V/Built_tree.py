from collections import deque

# ============================================================
# 以下皆為GPT生成
# Data Structures: Binary Trees (Simple vs Complete)
# Requirements:
# - TreeNode with value, left, right
# - No external packages (standard library OK)
# - Build:
#   (1) Simple binary tree via manual left/right connections
#   (2) Complete binary tree from a list using level-order fill
# - Visualize structure (not traversal-only)
# ============================================================


class TreeNode:
    """Basic binary tree node."""
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


# ------------------------------------------------------------
# 1) Build a "simple" binary tree by manually connecting nodes
# ------------------------------------------------------------
def build_simple_binary_tree(values: list[int]) -> TreeNode:
    """
    Build a simple (arbitrary-shape) binary tree by manually wiring nodes.

    NOTE:
    - This is intentionally NOT a BST,
    - NOT necessarily complete,
    - and NOT necessarily balanced.
    We just create a shape that is obviously different from a complete tree.
    """
    nodes = [TreeNode(v) for v in values]
    root = nodes[0]  # Use the first value as root

    # Hand-crafted arbitrary structure (on purpose):
    #
    # 37
    # ├─L: 142
    # │   ├─L: 89
    # │   │   ├─L: 176
    # │   │   └─R: 11
    # │   └─R: 63
    # │       └─R: 72
    # └─R: 5
    #     ├─L: 117
    #     │   ├─L: 24
    #     │   │   └─L: 58
    #     │   └─R: 133
    #     └─R: 151
    #         ├─L: 92
    #         └─R: 39
    #
    # (The remaining values are not used here; that's fine for a "simple" tree demo.)

    root.left = nodes[1]    # 142
    root.right = nodes[2]   # 5

    nodes[1].left = nodes[3]    # 89
    nodes[1].right = nodes[4]   # 63

    nodes[3].left = nodes[7]    # 176
    nodes[3].right = nodes[11]  # 11

    nodes[4].right = nodes[13]  # 72

    nodes[2].left = nodes[5]    # 117
    nodes[2].right = nodes[12]  # 151

    nodes[5].left = nodes[6]    # 24
    nodes[5].right = nodes[9]   # 133

    nodes[6].left = nodes[8]    # 58

    nodes[12].left = nodes[10]  # 92
    nodes[12].right = nodes[14] # 39

    return root


# ------------------------------------------------------------
# 2) Build a complete binary tree from list (level-order fill)
# ------------------------------------------------------------
def build_complete_binary_tree(values: list[int]) -> TreeNode | None:
    """
    Build a complete binary tree by level-order insertion from a list.

    Rule:
    - Fill each level from left to right with no gaps.

    Implementation idea:
    - Create nodes in order.
    - For node at index i:
        left child index  = 2*i + 1
        right child index = 2*i + 2
    """
    if not values:
        return None

    nodes = [TreeNode(v) for v in values]
    n = len(nodes)

    for i in range(n):
        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < n:
            nodes[i].left = nodes[left_i]
        if right_i < n:
            nodes[i].right = nodes[right_i]

    return nodes[0]


# ------------------------------------------------------------
# Visualization helpers
# ------------------------------------------------------------
def print_tree_sideways(root: TreeNode | None) -> None:
    """
    Print the tree rotated 90 degrees (sideways).
    - Right subtree is printed above
    - Left subtree is printed below
    This makes parent/child + left/right structure very clear.
    """
    def _print(node: TreeNode | None, prefix: str, is_left: bool) -> None:
        if node is None:
            return

        # Print right first (so it appears on top)
        _print(node.right, prefix + ("│   " if is_left else "    "), False)

        # Print current node
        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(node.value))

        # Print left next (so it appears below)
        _print(node.left, prefix + ("    " if is_left else "│   "), True)

    if root is None:
        print("(empty tree)")
        return

    _print(root, "", True)


def print_levels(root: TreeNode | None) -> None:
    """
    Print level-order, one level per line.
    This is a clean way to compare shapes of trees.
    """
    if root is None:
        print("(empty tree)")
        return

    q = deque([root])
    level = 0

    while q:
        size = len(q)
        line = []
        all_none = True

        for _ in range(size):
            node = q.popleft()
            if node is None:
                line.append("None")
                # We do NOT expand None further, to avoid infinite levels
            else:
                all_none = False
                line.append(str(node.value))
                q.append(node.left)
                q.append(node.right)

        # Stop if the whole level is None (means no more real nodes)
        if all_none:
            break

        print(f"Level {level}: " + "  ".join(line))
        level += 1


# ------------------------------------------------------------
# Demo with given sample data
# ------------------------------------------------------------
if __name__ == "__main__":
    data = [37, 142, 5, 89, 63, 117, 24, 176, 58, 133, 92, 11, 151, 72, 39, 184, 7, 101, 54, 160]

    simple_root = build_simple_binary_tree(data)
    complete_root = build_complete_binary_tree(data)

    print("============================================================")
    print("Simple Binary Tree (manual wiring, arbitrary shape)")
    print("Sideways view (right on top):")
    print_tree_sideways(simple_root)

    print("\nLevel-order (one level per line):")
    print_levels(simple_root)

    print("\n============================================================")
    print("Complete Binary Tree (built from list by level-order fill)")
    print("Sideways view (right on top):")
    print_tree_sideways(complete_root)

    print("\nLevel-order (one level per line):")
    print_levels(complete_root)
