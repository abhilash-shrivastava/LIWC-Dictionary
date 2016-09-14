# loading all the positive words in the the variable array posWords
with open("PosWords.txt") as f:
    posContent = f.readlines()

    posWords = []
    for num in range(0, len(posContent)):
        posContent[num] = posContent[num].split("\n")
        posWords.append(posContent[num][0]);

# loading all the negative words in the variable array negWords
with open("NegWords.txt") as f:
    negContent = f.readlines()

    negWords = []
    for num in range(0, len(negContent)):
        negContent[num] = negContent[num].split("\n")
        negWords.append(negContent[num][0]);

    posTriGrams = open("PosTriGrams.txt", "wb");
    negTriGrams = open("NegTriGrams.txt", "wb");

# reading the trigrams files and matching trigrams
with open("dummy_Google_Ngram.txt") as f:
    for line in f:
        lineElements = line.split();
        # check for the second word is AND or OR
        if (lineElements[1].upper() == "AND" or lineElements[1].upper() == "OR"):
            # for all the positive words in array check the first word is positive
            for posword in posWords:
                if posword == lineElements[0].upper():
                    # if the first word is positive then check the second word for negative
                    for negword in negWords:
                        # if the third word is also negative then store the trigram in positive trigram file
                        if negword == lineElements[2].upper():
                            posTriGrams.writelines(line);
                # if first word of the trigram is not positive then check that third word is positive
                elif posword == lineElements[2].upper():
                    # if third word is positive then check that first word is negative
                    for negword in negWords:
                        # if first word is negative then store the trigram in negative trigram file
                        if negword == lineElements[0].upper():
                            negTriGrams.writelines(line);





