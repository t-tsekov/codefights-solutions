def validRow(row):
    size = len(row) - min((row + ['.']).index('.'), (row + ['#']).index('#'))
    runs = [int(x) for x in row[:len(row) - size] if x != '-']
    row = row[len(row) - size:]
    curRun = 0
    actualRuns = []
    while row and row[0] == '.':
        row = row[1:]
    while row:
        if '.' in row:
            actualRuns.append(row.index('.'))
            row = row[row.index('.'):]
        else:
            actualRuns.append(len(row))
            row = []
        while row and row[0] == '.':
            row = row[1:]
    return runs == actualRuns


def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def correctNonogram(size, nonogramField):
    matrix = transpose(nonogramField)
    matrix = matrix[len(matrix) - size:]
    nf = nonogramField[len(nonogramField) - size:]
    return sum(map(validRow, matrix)) + sum(map(validRow, nf)) == 2 * size