def startupName(companies):
    comp1 = set(companies[0])
    comp2 = set(companies[1])
    comp3 = set(companies[2])
    res = (((comp1.intersection(comp2)).union(comp1.intersection(comp3))).union(comp2.intersection(comp3))).difference(comp1.intersection(comp2).intersection(comp3))
    return list(sorted(list(res)))
