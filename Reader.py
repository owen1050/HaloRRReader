import pyautogui

def readScreen():
    im = pyautogui.screenshot(region=(850,810, 500, 1))
    startBlue = -1
    startWhite = -1
    startRed = -1
    endWhite = -1
    endBlue = -1
    endRed = -1
    end = -1
    count = 0
    for i in range(500):
        p = im.getpixel((i,0))
        if startBlue == -1 and p == (46,195,229):
            startBlue = count
        if startWhite == -1 and p == (255,255,255):
            startWhite = count
        if startRed == -1 and p == (231, 149, 149):
            startRed = count

        if p == (112,112,112):
            end = count
        if p == (255,255,255):
            endWhite = count
        if p == (46,195,229):
            endBlue = count
        if p == (231, 149, 149):
            endRed = count
        count = count + 1

    start = startWhite
    if(startWhite > -1):
        if(startRed > -1):
            if(startRed < startWhite):
                start = startRed
        if(startBlue > -1):
            if(startBlue < startWhite):
                start = startBlue
    else:
        if(startRed > -1 and startBlue > -1):
            if(startRed < startBlue):
                start = startRed
            else:
                start = startBlue

        else:
            if(startRed > -1):
                start = startRed
            if(startBlue > -1):
                start = startBlue

    return (start, startRed, endRed, startBlue, endBlue, startWhite, endWhite, end)

    if(startBlue == -1 and startRed == -1):
        white = endWhite - startWhite
        whole = end - start
        print(str(int(white * 100 / whole)) + "/100")

    if(startBlue >= 0 and startRed == -1):
        blue = endBlue - startBlue
        white = endWhite - startWhite
        whole = end - start
        print(str(round((blue + white) * 100 / whole)) + "/100 overall and gained " + str(round((blue) * 100 / whole)))

    if(startBlue == -1 and startRed >= 0):
        red = endRed - startRed
        white = endWhite - startWhite
        whole = end - start
        print(str(round((white) * 100 / whole)) + "/100 overall and lost " + str(round((red) * 100 / whole)))

    return (start, startRed, endRed, startBlue, endBlue, startWhite, endWhite, end)

