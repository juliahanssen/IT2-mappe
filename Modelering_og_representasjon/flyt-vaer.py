grader = int(input("Hvor mnage grader er det ute? "))

if grader < 15:
    print("Ta på jakke")
    type = input("Regner det?")
    if type.lower == "ja":
        print("Ta med peraply")
else:
    print("Ha en fin dag i varmen")