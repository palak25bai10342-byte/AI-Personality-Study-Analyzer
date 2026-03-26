def ask_questions():

    # Initialize scores
    E = I = S = N = T = F = J = P = 0

    # Question number 1

    print("Q1: When you've had a really exhausting day, what do you prefer?")
    print("A) Being alone to recharge")
    print("B) Being around people to feel better")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        I += 1
    elif ans == "B":
        E += 1
    else:
        print("Invalid input")

    # Question number 2 

    print("\nQ2: In a group discussion, you usually:")
    print("A) Observe and speak when necessary")
    print("B) Speak freely and express ideas quickly")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        I += 1
    elif ans == "B":
        E += 1
    else:
        print("Invalid input")

    #Question number 3

    print("\nQ3: When learning something new, you prefer:")
    print("A) Clear facts and step-by-step guidance")
    print("B) Big ideas and understanding the concept")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        S += 1
    elif ans == "B":
        N += 1
    else:
        print("Invalid input")

    #Question number 4

    print("\nQ4: You are more interested in:")
    print("A) What is happening right now")
    print("B) What could happen in the future")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        S += 1
    elif ans == "B":
        N += 1
    else:
        print("Invalid input")

    #Question number 5

    print("\nQ5: When making an important decision, you rely more on:")
    print("A) Logic and reasoning")
    print("B) Feelings and personal values")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        T += 1
    elif ans == "B":
        F += 1
    else:
        print("Invalid input")

    #Question number 6

    print("\nQ6: If your decision hurts someone but is logically correct, you:")
    print("A) Still go with logic")
    print("B) Feel uncomfortable and reconsider")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        T += 1
    elif ans == "B":
        F += 1
    else:
        print("Invalid input")

    #Question number 7

    print("\nQ7: How do you handle tasks?")
    print("A) Plan everything in advance")
    print("B) Go with the flow")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        J += 1
    elif ans == "B":
        P += 1
    else:
        print("Invalid input")

    #Question number 8

    print("\nQ8: Deadlines for you are:")
    print("A) Fixed targets to finish early")
    print("B) Pressure points that push you last moment")

    ans = input("Enter A or B: ").upper()

    if ans == "A":
        J += 1
    elif ans == "B":
        P += 1
    else:
        print("Invalid input")

    # Return all scores
    return E, I, S, N, T, F, J, P
