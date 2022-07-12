arg = "ffff"
def getLrc(arg):
    hexT = int(arg[0] + arg[1], 16)
    for nr in range(2, len(arg), 2):
        hexT ^= int(arg[nr] + arg[nr + 1],16)
    return hex(hexT)
print(getLrc(arg))
