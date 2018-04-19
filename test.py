from unittest import TestCase
from main import GameOfLive

simple_list = [[1, 1, 1, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 1]]

count_list = [[3, 4, 2, 1],
              [3, 4, 3, 1],
              [2, 2, 2, 1],
              [0, 0, 1, 0]]

goal_list = [[1, 0, 1, 0],
             [1, 0, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

class TestGameOfLive(TestCase):
    def test_count_neighbours(self):
        game_of_live = GameOfLive(init_field=simple_list)
        for x in range(4):
            for y in range(4):
                self.assertEqual(count_list[x][y], game_of_live.count_neighbours(x, y),
                                 "Not matching {}, {}".format(x, y))

    def test_print(self):
        game_of_live = GameOfLive(init_field=simple_list)
        print(game_of_live)
        self.assertEqual("Generation 0\n4 4\n"
                         "███ \n"
                         "██  \n"
                         "    \n"
                         "   █",
                         str(game_of_live))

    def test_rules(self):
        game_of_live = GameOfLive(init_field=simple_list)
        game_of_live.next_generation()
        self.assertEqual(goal_list, game_of_live.current_field)

    def test_hash(self):
        game_of_live = GameOfLive(init_field=simple_list)
        print(hash(game_of_live))