# Program for playing the game of Life.
from lifegrid import LifeGrid


def main():
    init_config = []
    m = 1
    n = 4
    # Constructs the game grid and configure it.
    grid_widz = int(input("Enter width: "))
    grid_height = int(input("Enter height: "))
    num_gens = int(input("Enter number of gens: "))
    i = input("Enter list of coords in tuples (ex: [(1, 1), (1, 2), (2, 2), (3, 2)]: ")[1:-1]
    while n < len(i):
        t = (int(i[m]), int(i[n]))
        init_config.append(t)
        m += 8
        n += 8
    grid = LifeGrid(grid_widz, grid_height)
    grid.configure(init_config)

    # Plays the game.
    draw(grid)
    for i in range(num_gens):
        evolve(grid)
        draw(grid)


def evolve(grid):
    """
    The function that generates the next generation of organisms
    """
    # List for storing the live cells of the next generation.
    live_cells = []

    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(live_cells)


# Prints a text based representation of the game grid.
def draw(grid):
    """
    The function that prints a text based representation of the game grid
    """
    s = ""
    for row in range(grid.num_rows()):
        for col in range(grid.num_cols()):
            if grid.is_live_cell(row, col):
                s += "1 "
            else:
                s += "0 "
        s += "\n"
    print(s)


main()
