def knapsackLight(value1, weight1, value2, weight2, maxW):
    both = weight1 + weight2
    if maxW >= both:
        return value1 + value2
    else:
        if value1 >= value2:
            if maxW >= weight1:
                return value1
            elif maxW >= weight2:
                return value2
            else:
                return 0

        elif value2 > value1:
            if maxW >= weight2:
                return value2
            elif maxW >= weight1:
                return value1
            else:
                return 0

