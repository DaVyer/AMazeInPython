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