def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            level_sum = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                level_sum += node.val
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(level_sum/n)
        return res
