class AVLTree:
    def __init__(self, value: int | None = None) -> None:
        self.value: int | None = value
        self.left: AVLTree | None = None
        self.right: AVLTree | None = None
        self.height: int = 0 if value is None else 1

    def isempty(self) -> bool:
        return self.value is None

    def _height(self, node):
        return 0 if node is None or node.isempty() else node.height

    def _update_height(self):
        self.height = 1 + max(self._height(self.left), self._height(self.right))

    def _balance_factor(self):
        return self._height(self.left) - self._height(self.right)

    def _rotate_right(self):
        v, tl, tr = self.value, self.left, self.right
        self.value = tl.value
        self.left = tl.left
        self.right = AVLTree(v)
        self.right.left = tl.right
        self.right.right = tr
        self.right._update_height()
        self._update_height()

    def _rotate_left(self):
        v, tl, tr = self.value, self.left, self.right
        self.value = tr.value
        self.right = tr.right
        self.left = AVLTree(v)
        self.left.left = tl
        self.left.right = tr.left
        self.left._update_height()
        self._update_height()

    def _rebalance(self):
        bf = self._balance_factor()
        if bf > 1:
            if self.left._balance_factor() < 0:
                self.left._rotate_left()
            self._rotate_right()
        elif bf < -1:
            if self.right._balance_factor() > 0:
                self.right._rotate_right()
            self._rotate_left()

    def insert(self, v: int) -> None:
        if self.isempty():
            self.value = v
            self.height = 1
            return
        if v < self.value:
            if self.left is None:
                self.left = AVLTree(v)
            else:
                self.left.insert(v)
        elif v > self.value:
            if self.right is None:
                self.right = AVLTree(v)
            else:
                self.right.insert(v)
        else:
            return
        self._update_height()
        self._rebalance()

    def inorder(self) -> list[int]:
        if self.isempty():
            return []
        left = self.left.inorder() if self.left else []
        right = self.right.inorder() if self.right else []
        return left + [self.value] + right

    def preorder(self) -> list[int]:
        if self.isempty():
            return []
        left = self.left.preorder() if self.left else []
        right = self.right.preorder() if self.right else []
        return [self.value] + left + right

    def postorder(self) -> list[int]:
        if self.isempty():
            return []
        left = self.left.postorder() if self.left else []
        right = self.right.postorder() if self.right else []
        return left + right + [self.value]


if __name__ == "__main__":
    tree = AVLTree()
    for x in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(x)
    assert tree.inorder() == [1, 2, 3, 4, 5, 6, 7]
    assert tree.preorder() == [4, 2, 1, 3, 6, 5, 7]
    assert tree.postorder() == [1, 3, 2, 5, 7, 6, 4]
    print("All checks passed.")
