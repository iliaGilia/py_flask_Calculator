def checkSymbol(symbol, fNum, sNum):
    if symbol == '+':
        return int(fNum) + int(sNum)
    elif symbol == '-':
        return int(fNum) - int(sNum)
    elif symbol == '*':
        return int(fNum) * int(sNum)
    elif symbol == '/':
        return int(fNum) / int(sNum)
    else:
        return None  # add a default return value in case the symbol is invalid
