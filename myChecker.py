def intCheck(n1, n2):
    if n1.isdigit() and n2.isdigit():return True
    else: return False

def symCheck(symbol):
    if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/': return False
    else: return True