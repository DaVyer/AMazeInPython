from SAEMaze import Maze

laby = Maze(4, 4, True)
print(laby.info())
print(laby)

laby.neighbors = {
    (0, 0): {(1, 0)},
    (0, 1): {(0, 2), (1, 1)},
    (0, 2): {(0, 1), (0, 3)},
    (0, 3): {(0, 2), (1, 3)},
    (1, 0): {(2, 0), (0, 0)},
    (1, 1): {(0, 1), (1, 2)},
    (1, 2): {(1, 1), (2, 2)},
    (1, 3): {(2, 3), (0, 3)},
    (2, 0): {(1, 0), (2, 1), (3, 0)},
    (2, 1): {(2, 0), (2, 2)},
    (2, 2): {(1, 2), (2, 1)},
    (2, 3): {(3, 3), (1, 3)},
    (3, 0): {(3, 1), (2, 0)},
    (3, 1): {(3, 2), (3, 0)},
    (3, 2): {(3, 1)},
    (3, 3): {(2, 3)}
}

print(laby)

laby = Maze(4, 4, empty = True)
print(laby)

laby = Maze(4, 4, empty = False)
print(laby)

laby = Maze(5, 5, empty = True)
print(laby)

laby.add_wall((0,0), (0,1))
print(laby)

print("==========DEBUT TEST FILL==========")
print()

laby = Maze(4, 4, empty = True)
laby.fill()
print(laby)

print("==========FIN TEST FILL==========")
print()

print("==========DEBUT TEST REMOVE WALL==========")
print()

laby.remove_wall((0, 0), (0, 1))
print(laby)

print("==========FIN TEST REMOVE WALL==========")
print()

print()

print("==========DEBUT TEST EMPTY==========")
print()

laby.empty()
laby.add_wall((0, 0), (0, 1))
laby.add_wall((0, 1), (1, 1))
print(laby)

print("==========FIN TEST EMPTY==========")
print()

print("==========DEBUT TEST GET WALL==========")
print()

print(laby.get_walls())

print()
print("==========FIN TEST GET WALL==========")
print()

print("==========DEBUT TEST CONTIGUOUS CELLS==========")
print()

print(laby.get_contiguous_cells((0,1)))

print()
print("==========FIN TEST CONTIGUOUS CELLS==========")
print()

print("==========DEBUT TEST REACHABLE CELLS==========")
print()

print(laby.get_reachable_cells((0,1)))

print()
print("==========FIN TEST REACHABLE CELLS==========")
print()

print("==========DEBUT TEST GEN BTREE==========")
print()

laby = Maze.gen_btree(4,4)
print(laby)

print()
print("==========FIN TEST GEN BTREE==========")
print()

print("==========DEBUT TEST SIDEWINDER==========")
print()

laby = Maze.gen_sidewinder(4, 4)
print(laby)

print()
print("==========FIN TEST SIDEWINDER==========")
print()