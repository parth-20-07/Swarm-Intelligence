import os
import model
import time


def main():
    os.system('clear')

    coverage = 0.6
    satisfaction_threshold = 3
    only_1d_sort = True
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.6
    satisfaction_threshold = 4
    only_1d_sort = True
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.6
    satisfaction_threshold = 5
    only_1d_sort = True
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.8
    satisfaction_threshold = 3
    only_1d_sort = True
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.8
    satisfaction_threshold = 4
    only_1d_sort = True
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.8
    satisfaction_threshold = 5
    only_1d_sort = True
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.6
    satisfaction_threshold = 3
    only_1d_sort = False
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.6
    satisfaction_threshold = 4
    only_1d_sort = False
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.6
    satisfaction_threshold = 5
    only_1d_sort = False
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.8
    satisfaction_threshold = 3
    only_1d_sort = False
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.8
    satisfaction_threshold = 4
    only_1d_sort = False
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)

    coverage = 0.8
    satisfaction_threshold = 5
    only_1d_sort = False
    print(
        f"Coverage {coverage}, Satisfaction Threshold {satisfaction_threshold}")
    for i in range(10):
        ts = round(time.time())
        print(
            f"\tRun {i}")
        model.schelling_model(
            coverage, satisfaction_threshold, only_1d_sort, ts)


if __name__ == '__main__':
    main()
