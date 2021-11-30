try:
    import Reader, pyautogui, time, cv2
    last = ()
    this = ()
    lastRR = -1
    thisRR = -1
    while True:
        #print('ran')
        try:
            t = pyautogui.locateOnScreen('mpRanked.png', grayscale=True, region=(810,670, 140, 60), confidence=0.9)
            im = pyautogui.screenshot('test.png',  region=(810,670, 140, 60))
            #print(t)
            if t != None:
                this = Reader.readScreen()
                if this != last:
                    (start, startRed, endRed, startBlue, endBlue, startWhite, endWhite, end) = this

                    if(endBlue > -1):
                        thisRR = round((endBlue - start) * 100 / (end - start))
                    else:
                        if(endWhite > -1):
                            thisRR = round((endWhite - startWhite) * 100 / (end - start))
                        else:
                            thisRR = 0

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
                    print("from last match your change is:" + str(round(thisRR - lastRR)))
                    print("-----------------"+str(time.time())+"-------------------------------")
                    lastRR = thisRR 
                    last = this

            time.sleep(1)
        except Exception as e:
            pass
            #print(e)

    input()
except Exception as e:
    print(e)
    input()