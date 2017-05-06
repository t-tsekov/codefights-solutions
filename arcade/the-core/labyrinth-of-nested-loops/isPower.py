def isPower(n):
    if n == 1:
        return True
    for i in range(2, 19):
        i_on_power = i
        while i_on_power <= 350:
            i_on_power =  i_on_power  * i
            if n == i_on_power:
                return True
    return False
