import math


def solution(area):
    panels = []
    while math.sqrt(area) != 1:
        panels.append(int(math.sqrt(area))**2)
        area = area - int(math.sqrt(area))**2
        if area == 0:
            break

    panels.append(area)

    if 0 in panels:
        panels.remove(0)

    return tuple(panels)


if __name__ == '__main__':
    print(solution(12))
