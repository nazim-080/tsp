coordinats = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]

distances = []
strs = []

for point_2 in coordinats:
    sum_distance = 0
    point_1 = coordinats[0]
    str_1 = f'{point_1} -> '
    if point_2 != point_1:
        distance = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
        sum_distance_2 = sum_distance + distance
        str_2 = str_1 + f'{point_2}[{distance}] -> '
        for point_3 in coordinats:
            if point_3 != point_2 and point_3 != point_1:
                distance = ((point_3[0] - point_2[0]) ** 2 + (point_3[1] - point_2[1]) ** 2) ** 0.5
                sum_distance_3 = sum_distance_2 + distance
                str_3 = str_2 + f'{point_3}[{distance}] -> '
                for point_4 in coordinats:
                    if point_4 != point_3 and point_4 != point_2 and point_4 != point_1:
                        distance = ((point_4[0] - point_3[0]) ** 2 + (point_4[1] - point_3[1]) ** 2) ** 0.5
                        sum_distance_4 = sum_distance_3 + distance
                        str_4 = str_3 + f'{point_4}[{distance}] ->'
                        for point_5 in coordinats:
                            if point_5 != point_4 and point_5 != point_3 and point_5 != point_2 and point_5 != point_1:
                                dist_to_point_1 = ((point_5[0] - point_1[0]) ** 2 + (
                                        point_5[1] - point_1[1]) ** 2) ** 0.5
                                distance = ((point_5[0] - point_4[0]) ** 2 + (point_5[1] - point_4[1]) ** 2) ** 0.5
                                sum_distance_5 = sum_distance_4 + distance
                                sum_distance_5 += dist_to_point_1
                                str_5 = str_4 + f'{point_5}[{distance}] -> {point_1}[{dist_to_point_1}] = ' \
                                                f'{sum_distance_5}'

                                distances.append(sum_distance_5)
                                strs.append(str_5)

print(strs[distances.index(min(distances))])
