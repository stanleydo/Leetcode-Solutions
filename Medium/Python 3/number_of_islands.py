from typing import List


class Solution:

    @staticmethod
    def numIslands(grid: List[List[str]]) -> int:

        if not grid:
            return 0

        available_coordinates = [(x, y) for x in range(len(grid))
                                 for y in range(len(grid[0]))]

        adjacents = Solution.generateAdjacencies(
            available_coordinates, len(grid), len(grid[0]))

        visited = []

        numIslands = 0

        while available_coordinates:
            curX, curY = cur = available_coordinates[0]

            if cur not in visited:
                if grid[curX][curY] == "1":
                    numIslands += 1

                    inner_queue = [cur]
                    while inner_queue:
                        inner_cur = inner_queue.pop(0)
                        if inner_cur not in visited:
                            visited.append(inner_cur)
                            for child in [a for a in adjacents[inner_cur] if a not in visited]:
                                childX, childY = child
                                if grid[childX][childY] == "1":
                                    inner_queue.append(child)
                else:
                    visited.append(cur)

            available_coordinates = list(
                set(available_coordinates) - set(visited))

        return numIslands

    @staticmethod
    def generateAdjacencies(coordinates, rows, cols):

        adjacencies = dict()
        for coord in coordinates:
            adjacents = []
            x, y = coord
            adjacents += [(x + 1, y)] if x + 1 < rows else []
            adjacents += [(x, y + 1)] if y + 1 < cols else []
            adjacents += [(x - 1, y)] if x - 1 >= 0 else []
            adjacents += [(x, y - 1)] if y - 1 >= 0 else []
            adjacencies[coord] = adjacents
        return adjacencies


if __name__ == "__main__":
    test = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"], ["1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"], ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], [
        "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"], ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]
    print(Solution.numIslands(grid=test))
