from typing import List, Tuple
from random import randint
import time
import os

class GameOfLive(object):
    def __init__(self, size: Tuple=None, init_field: List[list]=None):
        self.generation = 0
        if size:
            self.size_x = size[0]
            self.size_y = size[1]
            self._current_field = list()
            for x in range(self.size_x):
                self._current_field.append([])
                for y in range(self.size_y):
                    self._current_field[x].append(randint(0, 1))
        else:
            self._current_field = init_field
            self.size_x = len(self._current_field)
            self.size_y = len(self._current_field[0])
        self._hash_list = [self.hash_of_field(self.current_field)]

    def count_neighbours(self, x_pos: int, y_pos: int) -> int:
        count = 0
        for x in range(x_pos - 1, x_pos + 2):
            for y in range(y_pos - 1, y_pos + 2):
                if self.size_x > x >= 0 and self.size_y > y >= 0:
                    if not (x == x_pos and y == y_pos):
                        if self._current_field[x][y]:
                            count += 1
        return count


    @property
    def current_field(self):
        return self._current_field

    @current_field.setter
    def current_field(self, new_field):
        self._current_field = new_field
        self.generation = 0
        self._hash_list = [self.hash_of_field(self.current_field)]

    def next_generation(self) -> bool:
        new_field = []
        for x in range(self.size_x):
            new_field.append(list())
            for y in range(self.size_y):
                count = self.count_neighbours(x, y)
                new_cell = 0
                if self._current_field[x][y]:
                    if count in (2, 3):
                        new_cell = 1
                else:
                    if count == 3:
                        new_cell = 1
                new_field[x].append(new_cell)
        self.generation += 1
        new_hash = self.hash_of_field(new_field)
        if new_hash not in self._hash_list:
            self._current_field = new_field
            self._hash_list.append(self.hash_of_field(self.current_field))
            return True
        else:
            print(f"{self.generation} same as {self._hash_list.index(new_hash)}")
            return False

    def __str__(self):
        output = []
        output.append("Generation {generation}".format(generation=self.generation))
        output.append(f"{self.size_x} {self.size_y}")
        for x in range(self.size_x):
            line = []
            for y in range(self.size_y):
                if self._current_field[x][y]:
                    line.append("#")
                else:
                    line.append(".")
            output.append(" ".join(line))
        return "\n".join(output)


    def run(self):
        while True:
            print(self)
            if not self.next_generation():
                break
            time.sleep(0.14*2)

    def hash_of_field(self, field: List[list]):
        as_string = []
        for x in range(self.size_x):
            as_string += list(map(str, field[x]))
        return int("".join(as_string))

def random_game():
    game = GameOfLive((30, 30))
    game.run()

def start_big_cycle():
    big = [
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    game = GameOfLive(init_field=big)
    game.run()

if __name__ == "__main__":
    start_big_cycle()
