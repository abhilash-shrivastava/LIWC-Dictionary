with open("PosWords.txt") as f:
    posContent = f.readlines()

    posWords = []
    for num in range(1000, 1100):
        posContent[num] = posContent[num].split("\n")
        posWords.append(posContent[num][0]);

with open("NegWords.txt") as f:
    negContent = f.readlines()

    negWords = []
    for num in range(1, 10):
        negContent[num] = negContent[num].split("\n")
        negWords.append(negContent[num][0]);


    triGrams = open("TriGrams.txt", "wb");
    for posword in posWords:
        for negword in negWords:
            posAndTriGram = posword + " AND " + negword + "\n";
            triGrams.writelines(posAndTriGram);
            posOrTriGram = posword + " OR " + negword + "\n";
            triGrams.writelines(posOrTriGram);
            negAndTriGram = negword + " AND " + posword + "\n";
            triGrams.writelines(negAndTriGram);
            negOrTriGram = negword + " OR " + posword + "\n";
            triGrams.writelines(negOrTriGram);

