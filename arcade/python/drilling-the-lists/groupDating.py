def groupDating(male, female):
    return zip(*[(x, y) for x,y in zip(male, female) if x != y ]) if zip(*[(x, y) for x,y in zip(male, female) if x != y ]) != [] else [[],[]]
