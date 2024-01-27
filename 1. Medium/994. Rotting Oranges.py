class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH = 1
        ROTTEN = 2
        MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        rottenOranges = collections.deque()
        freshOranges = set()
        minute = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == ROTTEN:
                    rottenOranges += ((row, col, minute),)
                elif grid[row][col] == FRESH:
                    freshOranges.add((row, col))

        while rottenOranges:
            x, y, minute = rottenOranges.popleft()

            for dx, dy in MOVES:
                if 0 <= x + dx < ROWS and 0 <= y + dy < COLS:
                    if grid[x + dx][y + dy] == FRESH:
                        grid[x + dx][y + dy] = ROTTEN
                        rottenOranges += ((x + dx, y + dy, minute + 1),)
                        freshOranges.remove((x + dx, y + dy))

        return minute if not freshOranges else -1
