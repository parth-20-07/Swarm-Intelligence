import os
import numpy as np
import random
import csv

# ---------------------------------------------------------------------------- #
#                               COLOR INFORMATION                              #
# ---------------------------------------------------------------------------- #
# BLACK -> EMPTY CELL
# WHITE -> FLASHING

# ---------------------------------------------------------------------------- #
#                                CODE DEFINITION                               #
# ---------------------------------------------------------------------------- #


def neighbor_flashed(y, x, grid):    # 4 Neighbors Flashed
    n_flashed = False
    if (y > 0):
        if (grid[y-1][x]):
            n_flashed = True
    if (y < len(grid)-1):
        if (grid[y+1][x]):
            n_flashed = True
    if (x > 0):
        if (grid[y][x-1]):
            n_flashed = True
    if (x < len(grid[0])-1):
        if (grid[y][x+1]):
            n_flashed = True
    return n_flashed


# def neighbor_flashed(y, x, grid):  # 8 Neighbors Flashed
#     n_flashed = False
#     if (y > 0):
#         if (grid[y-1][x]):
#             n_flashed = True
#         if (x > 0):
#             if (grid[y-1][x-1]):
#                 n_flashed = True
#         if (x < len(grid[0])-1):
#             if (grid[y-1][x+1]):
#                 n_flashed = True
#     if (y < len(grid)-1):
#         if (grid[y+1][x]):
#             n_flashed = True
#         if (x > 0):
#             if (grid[y+1][x-1]):
#                 n_flashed = True
#         if (x < len(grid[0])-1):
#             if (grid[y+1][x+1]):
#                 n_flashed = True
#     if (x > 0):
#         if (grid[y][x-1]):
#             n_flashed = True
#     if (x < len(grid[0])-1):
#         if (grid[y][x+1]):
#             n_flashed = True
#     return n_flashed


def check_all_done(grid):
    all_done = True
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (not grid[y][x]):
                all_done = False
    return all_done


def group_detection_model(width, height, probability, refractory_timer):
    steps_for_completion = int(1/probability)
    iterations = 0

    # False->Non-Initiated, True->Initiated
    initiated = [[False]*width]*height

    # True->Susceptible, False->Refractory
    state = [[True]*width]*height  # Make all susceptible

    # True->Flashed, False->Not Flashed
    flash = [[False]*width]*height
    size = [[0]*width]*height
    refrac_timer = [[0]*width]*height
    done_counter = [[0]*width]*height
    done_grid = [[False]*width]*height

    while (not check_all_done(done_grid) and (iterations < steps_for_completion*10)):
        iterations += 1
        for y in range(height):
            for x in range(width):
                if (state[y][x]):  # if(state == susceptible)
                    # if(neighbor signalled)
                    if (neighbor_flashed(y, x, flash)):
                        done_counter[y][x] = 0
                        done_grid[y][x] = False
                        flash[y][x] = True  # emit signal
                        state[y][x] = False  # state = Refractory
                        refrac_timer[y][x] = refractory_timer
                        size[y][x] += 1
                    elif ((not initiated[y][x]) and ((random.randrange(0, 100)/100) < probability)):
                        flash[y][x] = True  # emit signal
                        state[y][x] = False  # state = Refractory
                        refrac_timer[y][x] = refractory_timer
                        initiated[y][x] = True
                        size[y][x] += 1
                else:
                    if (flash[y][x]):
                        done_counter[y][x] += 1
                        if (done_counter[y][x] > steps_for_completion):
                            done_grid[y][x] = True
                    refrac_timer[y][x] -= 1
                    if (refrac_timer[y][x] <= 0):
                        state[y][x] = True  # state = Susceptible

    # for y in range(height):
    #     row = ""
    #     for x in range(width):
    #         row += f"{size[y][x]}\t"
    #     print(f'|{row}|\n')
    max = 0
    for y in range(height):
        for x in range(width):
            if (size[y][x] > max):
                max = size[y][x]
    print(
        f"W: {width}, H: {height}, P: {probability}, R: {refractory_timer}, Max: {max}")
    print("-----------------------------------------------------------------------------------------")
    with open('./Docs/log.csv', 'a') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        data = [refractory_timer, probability, max]
        writer.writerow(data)
    return data


# def main():
#     os.system('clear')
#     group_detection_model(
#         width=5, height=5, probability=0.2, refractory_timer=10)


# if __name__ == '__main__':
#     main()
