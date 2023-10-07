def ordinal(i):
    """
    for an int i, returns the ordinal number i.
    e.g. ordinal(1) returns "1st"
    """
    if i > 10 and i < 20:
        return str(i) + "th"
    d = {0: "th", 1: "st", 2: "nd", 3: "rd", 4: "th",
         5: "th", 6: "th", 7: "th", 8: "th", 9: "th"}
    return str(i) + d[i%10]

if __name__ == "__main__":
    for i in range(101):
        print(ordinal(i))
    