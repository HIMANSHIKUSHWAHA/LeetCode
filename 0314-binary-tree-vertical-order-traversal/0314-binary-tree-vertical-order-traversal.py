from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_map = defaultdict(list)  # col -> list of node values
        queue = deque([(root, 0)])   # (node, column)
        min_col, max_col = 0, 0

        while queue:
            node, col = queue.popleft()
            col_map[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
                min_col = min(min_col, col - 1)
            if node.right:
                queue.append((node.right, col + 1))
                max_col = max(max_col, col + 1)

        return [col_map[c] for c in range(min_col, max_col + 1)]
