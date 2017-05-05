def evenDigitsOnly(n):
    even = "24680"
    for c in str(n):
        if c not in even:
            return False
    return True