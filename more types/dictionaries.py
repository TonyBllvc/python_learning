ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
print(ages["Mary"] + ages["Dave"])

#eg
primary = {
    "Red": [225, 0, 0],
    "Green": [0, 225, 0],
    "blue": [0, 0, 225],
}

print(primary["Red"])

#Dictionary functions
squares = {1: 1, 2: 4, 3: "error", 4: 16, }
squares[8] = 64
squares[3] = 9
print(squares)
print(squares[8])

#dictionary
pairs = {1: "apples",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}

print(pairs.get("orange"))
...