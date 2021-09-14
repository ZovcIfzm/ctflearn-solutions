def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False

num = 5432100000001234

# For loop, starting at num, ending at num+1E10, each loop adds by 10000.
for i in range(num, num+10000000000, 10000):
    if checkLuhn([digit for digit in str(i)]) == True:
        if i % 123457 == 0:
            print(i)
