def twoTeams(students):
    return sum([x for i,x in enumerate(students) if i%2 == 0]) - sum([x for i,x in enumerate(students) if i%2 != 0])
