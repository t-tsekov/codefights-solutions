def willYou(young, beautiful, loved):
    if loved and not (young and beautiful):
        return True
    if young and beautiful and not loved:
        return True

    return False