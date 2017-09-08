def mostFreqInt(intArr):
    frequencyHash = {}
    currentMostFreq = None
    currentMostFreqVal = 0

    for x in intArr:
        if frequencyHash[intArr[x]] is None:
            frequencyHash[intArr[x]] = 1
        else:
            frequencyHash[intArr[x]] = frequencyHash[intArr[x]] + 1

        if frequencyHash[intArr[x]] > currentMostFreqVal:
            currentMostFreqVal = frequencyHash[intArr[x]]
            currentMostFreq = intArr[x]

    return currentMostFreq