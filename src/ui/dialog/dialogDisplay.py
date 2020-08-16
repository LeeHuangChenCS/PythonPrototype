import time
import sys

class DialogDisplay:
    def __init__(self, nWaitTimeSec=.025):
        self.nWaitTimeSec = nWaitTimeSec
        self.nbufferTime = 0

    def displayString(self, sText):
        iTextLen = len(sText)
        for i in range(iTextLen):
            print(sText[i], end='')
            sys.stdout.flush()

            if i < (iTextLen-1):
                nCurTime = time.time()
                nTimeDiff = nCurTime-self.nbufferTime
                if nTimeDiff < self.nWaitTimeSec:
                    nTimeToWait = self.nWaitTimeSec - nTimeDiff
                    time.sleep(nTimeToWait)
                self.nbufferTime = time.time()

    def prompt(self, sText):
        self.displayString(sText)
        return input("")

    def enter(self):
        self.prompt("Press Enter to continue...")
