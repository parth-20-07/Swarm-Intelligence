import os
import numpy as np
from matplotlib import pyplot as plt
import random

# ---------------------------------------------------------------------------- #
#                               COLOR INFORMATION                              #
# ---------------------------------------------------------------------------- #
# BLACK -> EMPTY CELL
# WHITE -> FLASHING

# ---------------------------------------------------------------------------- #
#                             VARIABLE DECLARATION                             #
# ---------------------------------------------------------------------------- #
grid_width = 10  # Screen Width
grid_height = 10  # Screen Height
max_value = 100  # T

# Initialize the Grid with zeros
counter_grid = np.zeros((grid_width, grid_height), dtype=float)
grid = np.zeros((grid_width, grid_height), dtype=int)


# ---------------------------------------------------------------------------- #
#                                CODE DEFINITION                               #
# ---------------------------------------------------------------------------- #
def initialize_basics_requirements():
    # Randomly Put the cells as Empty or Flashing
    for y in range(grid_height):
        for x in range(grid_width):
            counter_grid[y, x] = random.randint(0, max_value)


def check_grid_sum():
    total_sum = 0
    for y in range(grid_height):
        for x in range(grid_width):
            if (grid[y, x] == 1):
                total_sum += 1
    if (total_sum == grid_height+grid_width):
        return True, total_sum
    else:
        return False, total_sum


def coupled_oscillation_model(constant):
    first_sync = True
    counter = 3
    initialize_basics_requirements()

    # Create Folder to save images
    folder_name = f"Images/{constant}"
    os.system(f"mkdir -p {folder_name}")

    # Initial Image
    file_name = f"{folder_name}/Base Figure.png"
    plt.imshow(grid, vmin=0, vmax=2, cmap="gray")
    plt.savefig(file_name)

    for iteration_number in range(20000):
        for y in range(grid_height):
            for x in range(grid_width):
                counter_grid[y, x] += 1

                if (counter_grid[y, x] >= max_value):
                    grid[y, x] = 1
                    counter_grid[y, x] = 0
                else:
                    grid[y, x] = 0

        for y in range(grid_height):
            for x in range(grid_width):
                if (grid[y, x] == 0):
                    neighbors_flashing = False

                    if (y > 0):
                        if (grid[y-1, x] == 1):
                            neighbors_flashing += True
                    if (y < grid_height-1):
                        if (grid[y+1, x] == 1):
                            neighbors_flashing += True
                    if (x > 0):
                        if (grid[y, x-1] == 1):
                            neighbors_flashing += True
                    if (x < grid_width-1):
                        if (grid[y, x+1] == 1):
                            neighbors_flashing += True
                    if (neighbors_flashing):
                        counter_grid[y, x] = counter_grid[y, x] + \
                            (constant*counter_grid[y, x])
                        if (counter_grid[y, x] >= max_value):
                            grid[y, x] = 1
                            counter_grid[y, x] = 0
                        else:
                            grid[y, x] = 0

        if ((iteration_number % 10 == 0) or (iteration_number > 900)):
            file_name = f"{folder_name}/Iteration {iteration_number}.png"
            plt.imshow(grid, vmin=0, vmax=1, cmap="gray")
            plt.savefig(file_name)
        oscillation_sync, sum = check_grid_sum()
        print(f"\t\tIteration {iteration_number}")
        if (oscillation_sync and first_sync):
            counter -= 1
            if (counter == 0):
                first_sync = False
            print(f"First Sync Triggered: {iteration_number}")

    # Combine all the images saved into a .gif
    os.system(
        f"cd {folder_name} && convert -delay 20 -loop 0 *.png coupled_oscillation.gif")


# def main():
#     os.system("clear")
#     coupled_oscillation_model(constant=0.3)


# if __name__ == "__main__":
#     main()
