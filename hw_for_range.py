# hw2: creati o functie pentru codul care se repeta + spatii
def rep_construction(message):
    print()
    print("#"*150 + "\n")
    print(message + "\n")
    print("#"*150 + "\n")
rep_construction("Start APP")


def inputInt(message):  # hw1: functia inputint
    my_nr = int(input(message))
    return int(my_nr)

start_value = inputInt("Start: ")
end_value = inputInt("End: ")
# hw3: directia 1 - 100
if start_value < end_value-1:
    rep_construction("Diapason of values")

    for x in range(start_value, end_value+1):
        print(x, end=" ")
    print()

    rep_construction("Divide by 3")

    for x in range(start_value, end_value+1):
        if x % 3 == 0:
            print(x, end=" ")
    print()

    rep_construction("First 5 values that divide by 3")

    n = 0
    for x in range(start_value, end_value+1):
        if x % 3 == 0 and n < 5:
            print(x, end=" ")
            n += 1
    print()

    rep_construction("Finish APP")

# hw3: daca este introdus nr apropiat unul de altul 47-48
if start_value == end_value-1 or start_value == end_value:
    print("Error, little diapason")

if start_value > end_value:
    rep_construction("Diapason of values")

# hw3: directia 100 - 1
    for x in reversed(range(end_value, start_value+1)):
        print(x, end=" ")
    print()

    rep_construction("Divide by 3")

    for x in reversed(range(end_value, start_value+1)):
        if x % 3 == 0:
            print(x, end=" ")
    print()

    rep_construction("First 5 values that divide by 3")

    n = 0
    for x in reversed(range(end_value, start_value+1)):
        if x % 3 == 0 and n < 5:
            print(x, end=" ")
            n += 1
    print()

    rep_construction("Finish APP")
