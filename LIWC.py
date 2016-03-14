with open("Posemo.txt") as f:
    content = f.readlines();

    for line in content:
        stem = line.split("\n")
        stem = stem[0].split("*")
        print stem[0];