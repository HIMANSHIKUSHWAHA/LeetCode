class Solution:
    def __init__(self):
        self.segTree = []

    def buildSegTree(self, baskets, i, l, r):
        if l == r:
            self.segTree[i] = baskets[l]
            return
        mid = l + (r - l) // 2
        self.buildSegTree(baskets, 2 * i + 1, l, mid)
        self.buildSegTree(baskets, 2 * i + 2, mid + 1, r)
        self.segTree[i] = max(self.segTree[2 * i + 1], self.segTree[2 * i + 2])

    def querySegTree(self, i, l, r, val):
        # No Basket Available
        if self.segTree[i] < val:
            return False

        # Found valid basket
        if l == r:
            self.segTree[i] = -1  # Mark as used
            return True

        mid = l + (r - l) // 2
        placed = False

        if self.segTree[2 * i + 1] >= val:
            placed = self.querySegTree(2 * i + 1, l, mid, val)
        else:
            placed = self.querySegTree(2 * i + 2, mid + 1, r, val)

        self.segTree[i] = max(self.segTree[2 * i + 1], self.segTree[2 * i + 2])
        return placed

    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        self.segTree = [-1] * (4 * n)
        self.buildSegTree(baskets, 0, 0, n - 1)

        unplaced = 0
        for qty in fruits:
            if not self.querySegTree(0, 0, n - 1, qty):
                unplaced += 1

        return unplaced
