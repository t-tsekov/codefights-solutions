def checkPassword(attempts, password):
    def check():
        while True:
           attempt = yield
           if attempt == password:
                yield True

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1
