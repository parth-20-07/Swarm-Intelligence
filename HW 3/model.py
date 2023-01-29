import os
import numpy as np
from matplotlib import pyplot as plt
import random

# ---------------------------------------------------------------------------- #
#                               COLOR INFORMATION                              #
# ---------------------------------------------------------------------------- #
# BLACK -> EMPTY CELL
# GREY -> NEIGHBOUR 1
# WHITE -> NEIGHBOUR 2

# ---------------------------------------------------------------------------- #
#                             VARIABLE DECLARATION                             #
# ---------------------------------------------------------------------------- #
grid_width = 50  # Screen Width
grid_height = 50  # Screen Height
# Initialize the Grid with zeros
grid = np.zeros((grid_width, grid_height), dtype=int)
# Creating a duplicate grid for verification
last_iteration_grid = np.zeros((grid_width, grid_height), dtype=int)
empty_cells = []  # A list of all the empty cell locations to improve performance


# ---------------------------------------------------------------------------- #
#                                CODE DEFINITION                               #
# ---------------------------------------------------------------------------- #
def place_object_randomly(object):
    """Generates a random (y,x) location from the grid and checks if it is occupied.
    Place the *object* if the location is empty.

    Args:
        object (integer): The character to place.

    Returns:
        bool: True -> Space is empty and object is placed,
                False -> Space is preoccupied
    """
    x, y = (random.randint(0, grid_width-1), random.randint(0, grid_height-1))
    if (grid[y, x] != 0):
        return False
    else:
        grid[y, x] = object
    return True


def initialize_basics_requirements(coverage):
    """Setup the basics needed to perform schelling's model
    1. Clear the empty list
    2. Calculate the number of characters to place in grid

    Args:
        coverage (float): The coverage to be performed in grid. Range: (0,1)
    """
    empty_cells.clear()
    object_placement_count = round(coverage*grid_height*grid_width/2)

    # Setting all values to Grey
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            grid[y, x] = 0

    y = 0
    while (y < object_placement_count):
        if (place_object_randomly(1)):  # Place Object 1
            y += 1

    y = 0
    while (y < object_placement_count):
        if (place_object_randomly(2)):  # Place Object 2
            y += 1


def is_happy(cell, satisfaction_threshold, new_neighbour_search=False, Object=0):
    """Check if the object is satisfied or not.

    Args:
        cell (integer,integer): (y,x) grid coordinates to check the happiness of.
        satisfaction_threshold (integer): The minimum number of neighbours needed for satisfaction
        new_neighbour_search (bool, optional): True, search is for new location at a empty cell. Defaults to False.
        Object (int, optional): The Neighbours to check for when performing check at am empty cell. Defaults to 0.

    Returns:
        bool: True -> Satisfied
                False -> Not Satisfied
    """
    satisfaction_level = 0
    y, x = cell

    if not (new_neighbour_search):
        # Set the resident as the current cell who's happiness needs to be checked.
        resident = grid[y][x]
    else:
        # Set the resident as the object value when the happiness around the empty cell needs to be checked.
        resident = Object

    if (y > 0 and y < grid_height-1):
        # Not top and bottom edge
        if (x > 0 and x < grid_width-1):
            # Not corner location
            if (grid[y-1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y-1, x] == resident):
                satisfaction_level += 1
            if (grid[y-1, x+1] == resident):
                satisfaction_level += 1
            if (grid[y, x-1] == resident):
                satisfaction_level += 1
            if (grid[y, x+1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x] == resident):
                satisfaction_level += 1
            if (grid[y+1, x+1] == resident):
                satisfaction_level += 1

        elif (x == 0):
            # Left Edge
            if (grid[y-1, x] == resident):
                satisfaction_level += 1
            if (grid[y-1, x+1] == resident):
                satisfaction_level += 1
            if (grid[y, x+1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x] == resident):
                satisfaction_level += 1
            if (grid[y+1, x+1] == resident):
                satisfaction_level += 1

        elif (x == grid_width-1):
            # Right Edge
            if (grid[y-1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y-1, x] == resident):
                satisfaction_level += 1
            if (grid[y, x-1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x] == resident):
                satisfaction_level += 1

    elif (y == 0):
        # Top Edge
        if (x > 0 and x < grid_width-1):
            # Not Left and Right Edge
            if (grid[y, x-1] == resident):
                satisfaction_level += 1
            if (grid[y, x+1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x] == resident):
                satisfaction_level += 1
            if (grid[y+1, x+1] == resident):
                satisfaction_level += 1

        elif (x == 0):
            # Top Left Corner
            if (grid[y, x+1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x] == resident):
                satisfaction_level += 1
            if (grid[y+1, x+1] == resident):
                satisfaction_level += 1
        elif (x == grid_width-1):
            # Top Right Corner
            if (grid[y, x-1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y+1, x] == resident):
                satisfaction_level += 1

    elif (y == grid_height-1):
        # Bottom Edge
        if (x > 0 and x < grid_width-1):
            # Not Left and Right Edges
            if (grid[y-1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y-1, x] == resident):
                satisfaction_level += 1
            if (grid[y-1, x+1] == resident):
                satisfaction_level += 1
            if (grid[y, x-1] == resident):
                satisfaction_level += 1
            if (grid[y, x+1] == resident):
                satisfaction_level += 1

        elif (x == 0):
            # Bottom Left Corner
            if (grid[y-1, x] == resident):
                satisfaction_level += 1
            if (grid[y-1, x+1] == resident):
                satisfaction_level += 1
            if (grid[y, x+1] == resident):
                satisfaction_level += 1

        elif (x == grid_width-1):
            # Bottom Right Corner
            if (grid[y-1, x-1] == resident):
                satisfaction_level += 1
            if (grid[y-1, x] == resident):
                satisfaction_level += 1
            if (grid[y, x-1] == resident):
                satisfaction_level += 1

    if (satisfaction_level >= satisfaction_threshold):
        return True
    else:
        return False


def find_new_neighbour(cell, satisfaction_threshold, only_1d_search=False):
    """Find New Neighbours

    Args:
        cell (int,int): (y,x) value for the cell
        satisfaction_threshold (int): The minimum number of similar neighbours needed for satisfaction
        only_1d_search (bool, optional): True -> Search accross the whole grid. Defaults to False, search only in current row.

    Returns:
        bool: True -> Location Found
                False -> Location Not Found
        (int,int): (y,x) -> Location where it is satisfied
    """
    neighbour_found = False
    location = np.array((1, 2), dtype=int)
    y, x = cell

    for i in range(len(empty_cells)):
        if (only_1d_search):
            if (y == empty_cells[i][0]):
                if (is_happy(empty_cells[i], satisfaction_threshold, True, Object=int(grid[y, x]))):
                    neighbour_found = True
                    location = empty_cells[i]
                    break

            elif (cell[0] < empty_cells[i][0]):
                break

        else:
            if (is_happy(empty_cells[i], satisfaction_threshold, True, int(grid[y, x]))):
                neighbour_found = True
                location = empty_cells[i]
                break

    return neighbour_found, location


def schelling_model(coverage, satisfaction_threshold, only_1d_sort, time_stamp):
    """Initialize the Schelling Model to visualize Seggregation

    Args:
        coverage (float): Coverage of neighbours (0,1)
        satisfaction_threshold (int): Minimum Number of Neighbours required for Satisfaction
        only_1d_sort (bool): True -> Search in the same row for new location
                                False -> Search accross the whole grid for new location
        time_stamp (int): To save the images uniquely.
    """
    initialize_basics_requirements(coverage=coverage)

    # Collect the location of all empty cells in the grid
    for y in range(grid_height):
        for x in range(grid_width):
            if (grid[y][x] == 0):
                empty_cells.append((y, x))

    find_type = ''
    if (only_1d_sort):
        find_type = '1D'
    else:
        find_type = '2D'

    # Create Folder to save images
    folder_name = f"{find_type}/'Coverage {coverage}'/'S {satisfaction_threshold}'/'TS {time_stamp}'"
    os.system(f'mkdir -p {folder_name}')

    # Initial Image
    file_name = f"{find_type}/Coverage {coverage}/S {satisfaction_threshold}/TS {time_stamp}/Base Figure.png"
    plt.imshow(grid, vmin=0, vmax=2, cmap='gray')
    plt.savefig(file_name)

    iteration_number = 0
    while True:
        last_iteration_grid[:] = grid  # Make a copy of the grid

        for y in range(grid_height):
            for x in range(grid_width):  # Go to each location in the grid

                # Check if the object at the location is satisfied
                if not (is_happy((y, x), satisfaction_threshold)):
                    found_neighbour, location = find_new_neighbour(
                        (y, x), satisfaction_threshold, only_1d_sort)  # Find new location for unsatisfied object

                    if (found_neighbour):
                        # Move the object to new location
                        grid[location] = grid[y, x]
                        grid[y, x] = 0  # Clear the old location
                        # Add the old location to empty cell list
                        empty_cells.append((y, x))
                        # Remove the updated location from the empty cell list
                        empty_cells.remove(location)

        file_name = f"{find_type}/Coverage {coverage}/S {satisfaction_threshold}/TS {time_stamp}/Iteration {iteration_number+1}.png"
        plt.imshow(grid, vmin=0, vmax=2, cmap='gray')
        plt.savefig(file_name)
        print(f"\t\tIteration {iteration_number} Finished!")

        # Compare the new grid with the copy of last saved grid image
        comparision = last_iteration_grid == grid

        if (comparision.all()):  # If the grids are identical, the max satisfaction possible is reached
            print("\t\tMax Satisfaction Reached!")
            break
        else:  # If not identical, give it one more try for satisfaction achievement
            last_iteration_grid[:] = grid
            iteration_number += 1

    # Combine all the images saved into a .gif
    os.system(
        f'cd {folder_name} && convert -delay 50 -loop 0 *.png schelling_model.gif')
