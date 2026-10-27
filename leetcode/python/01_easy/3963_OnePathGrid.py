class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []

        wall = "#" * (n-1)
        block = ['.' + wall]
        path = "." * n

        grid = block * (m-1)
        grid.append(path)

        return grid
