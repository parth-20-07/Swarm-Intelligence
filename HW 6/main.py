import os
import model
import time


def main():
    os.system('clear')
    constant = 0.5
    while True:
        constant += 0.1
        print(f"K {constant}")
        model.coupled_oscillation_model(constant)
        if (constant == 1):
            break


if __name__ == '__main__':
    main()
