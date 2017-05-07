def higherVersion(ver1, ver2):
    ver1 = list(map(int, ver1.split(".")))
    ver2 = list(map(int, ver2.split(".")))
    return ver1 > ver2