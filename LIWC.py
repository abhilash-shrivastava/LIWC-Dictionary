with open("Posemo.txt") as f:
    content = f.readlines()

    stems = []
    for line in content:
        line = line.split("\n")
        line = line[0].split("*")
        stems.append(line[0]);
    # print stem

with open("words") as f:
    content = f.readlines()

    unix = []
    for line in content:
        line = line.split("\n")
        line = line[0].split("*")
        unix.append(line[0]);
    # print unix
# Open a file
    posWords = open("PosWords.txt", "wb")


    import re
    for stem in stems:
        pattern = '(.*)'+stem+'(.*)'
        indices = [i for i, x in enumerate(unix) if re.search(pattern, x)]
        print indices
        for index in indices:
            posWords.write(unix[index]+'\n');
            print unix[index]

