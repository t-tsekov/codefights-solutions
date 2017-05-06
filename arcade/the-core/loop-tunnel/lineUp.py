def lineUp(commands):
    c = 0
    flag = False
    for l in commands:

        if l == "L" or l == "R":

            if flag == True:

                c += 1
                flag = False

            else:

                flag = True

        if l == "A":

            if flag == False:
                c += 1

    return c