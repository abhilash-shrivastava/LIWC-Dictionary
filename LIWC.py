with open("Posemo.txt") as f:
    posContent = f.readlines()

    posStems = []
    for line in posContent:
        line = line.split("\n")
        line = line[0].split("*")
        posStems.append(line[0].upper());

with open("Negemo.txt") as f:
    negContent = f.readlines()

    negStems = []
    for line in negContent:
        line = line.split("\n")
        line = line[0].split("*")
        negStems.append(line[0].upper());

with open("words") as f:
    content = f.readlines()

    unix = []
    for line in content:
        line = line.split("\n")
        line = line[0].split("*")
        unix.append(line[0].upper());

    posWords = open("PosWords.txt", "wb")


    import re
    for stem in posStems:
        pattern = stem+'(.*)'
        indices = [i for i, x in enumerate(unix) if re.search(pattern, x)]
        for index in indices:
            posWords.write(unix[index]+'\n');

    negWords = open("NegWords.txt", "wb")

    for stem in negStems:
        pattern = '(.*)'+stem+'(.*)'
        indices = [i for i, x in enumerate(unix) if re.search(pattern, x)]
        for index in indices:
            negWords.write(unix[index]+'\n');

