def higherVersion2(ver1, ver2):
    ver1 = list(map(int, ver1.split(".")))
    ver2 = list(map(int, ver2.split(".")))
    if ver1 < ver2:
        return -1
    elif ver1 > ver2:
        return 1
    else:
        return 0