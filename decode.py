def decode(originalPw):
    newPw = ""
    temp = str(originalPw)
    for number in temp:
        if int(number) >= 3:
            newPw += str( int(number) - 3 )
        else:
            difference = abs( int(number) - 3)
            newPw += str( 10 - difference )
    return newPw