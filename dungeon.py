from hero import Hero


class Dungeon:

    STARTING_POINT = 'S'
    GATEWAY = 'G'
    OBSTACLE = '#'
    WALKABLE_PATH = '.'
    TREASURE = 'T'
    ENEMY = 'E'
    HERO = 'H'

    @staticmethod
    def load_file(path):
        with open(path, "r") as f:
            contents = f.read().split("\n")
            matrix = [list(line) for line in contents if line.strip != ""]
        return Dungeon(matrix)

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(["".join(line) for line in self.matrix])

    def spawn(self, hero):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if self.matrix[row][col] == Dungeon.STARTING_POINT:
                    self.matrix[row][col] = Dungeon.HERO

dung = Dungeon.load_file("map.txt")
h = Hero("name", "title", 20, 10, 1)
print(dung)
dung.spawn(h)
print(dung)
