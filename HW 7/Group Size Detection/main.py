import os
import model


def main():
    os.system('clear')
    os.system('rm Docs/log.csv')
    prob_list = []
    refac_list = []
    max_list = []
    width = 5
    height = 5
    step = 0.1
    for r in range(10):
        for p in range(1, 100, 1):
            prob = p/100
            data = model.group_detection_model(
                width, height, prob, r)
            prob_list.append(data[0])
            refac_list.append(data[1])
            max_list.append(data[2])


if __name__ == '__main__':
    main()
