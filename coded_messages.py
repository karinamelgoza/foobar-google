def solution(l, t):
    d = {}
    for index, value in enumerate(l):
        d[index] = value
    total = 0
    index = 0
    sub_list = []
    while total != t:
        for num in list(d.items())[index:]:
            sub_list.append(num)
            total += int(num[1])
            if total == t:
                break
        if total == t:
            break
        index += 1
        total = 0
        sub_list = []
        if index > len(l):
            sub_list = [-1, -1]
            break
    try:
        return sub_list[0][0], sub_list[-1][0]
    except:
        return sub_list
