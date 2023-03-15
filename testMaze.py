from SAEMaze import Maze

"""
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

print()
print("==========FIN TEST FILL==========")

print("==========DEBUT TEST REMOVE WALL==========")
print()

laby.remove_wall((0, 0), (0, 1))
print(laby)

print()
print("==========FIN TEST REMOVE WALL==========")


print()

print("==========DEBUT TEST EMPTY==========")
print()

laby.empty()
laby.add_wall((0, 0), (0, 1))
laby.add_wall((0, 1), (1, 1))
print(laby)

print()
print("==========FIN TEST EMPTY==========")


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

print("==========DEBUT TEST GEN FUSION==========")
print()

laby = Maze.gen_fusion(15, 15)
print(laby)

print()
print("==========FIN TEST GEN FUSION==========")
print()

print("==========DEBUT TEST GEN EXPLORATION==========")
print()

laby = Maze.gen_exploration(15, 15)
print(laby)

print()
print("==========FIN TEST GEN EXPLORATION==========")
print()

print("==========DEBUT TEST WILSON==========")
print()

laby = Maze.gen_wilson(12, 12)
print(laby)

print()
print("==========FIN TEST WILSON==========")
print()

print("==========DEBUT TEST OVERLAY==========")
print()

laby = Maze(4,4, empty = True)
print(laby.overlay({
    (0, 0):'c',
    (0, 1):'o',
    (1, 1):'u',
    (2, 1):'c',
    (2, 2):'o',
    (3, 2):'u',
    (3, 3):'!'}))

laby = Maze(4,4, empty = True)
path = {(0, 0): '@',
        (1, 0): '*',
        (1, 1): '*',
        (2, 1): '*',
        (2, 2): '*',
        (3, 2): '*',
        (3, 3): '§'}
print(laby.overlay(path))

print()
print("==========FIN TEST OVERLAY==========")
print()

print("==========DEBUT RESOLUTION DFS==========")
print()

laby = Maze.gen_fusion(15, 15)
solution = laby.solve_dfs((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(6, 6)] = 'A'
print(laby.overlay(str_solution))

print()
print("==========FIN RESOLUTION DFS==========")
print()

print("==========DEBUT RESOLUTION BFS==========")
print()

laby = Maze.gen_exploration(15, 15)
solution = laby.solve_bfs((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))

print()
print("==========FIN RESOLUTION BFS==========")
print()
"""






