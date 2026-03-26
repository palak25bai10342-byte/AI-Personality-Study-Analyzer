def calculate_personality(scores):
    E,I,S,N,T,F,J,P = scores

    personality = ""

    # E vs I 
    if E>I:
        personality += "E"
    else:
        personality += "I"

    # S vs N 
    if S>N:
        personality += "S"
    else:
        personality += "N"

    # T vs F 
    if T>F:
        personality += "T"
    else:
        personality += "F"

    # J vs P 
    if J>P:
        personality += "J"
    else:
        personality += "P"

    return personality
