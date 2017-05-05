def sumUpNumbers(inputString):
    p = re.compile(r'\d+')
    return sum(map(int, p.findall(inputString)))
