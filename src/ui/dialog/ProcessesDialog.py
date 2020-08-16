import os
import json
import src.ui.dialog.dialogDisplay as dialogDisplay

gsDialogFile = os.path.join("resource", "dialogs", "start.json")

gsStartingState = "$$start"
ghName = "name"
ghExp = "exp"
ghTxt = "txt"
ghOptName = "optName"
ghOpts = "opts"

def DialogDict(sDialogFile):
    return json.load(open(sDialogFile, "r"))

def ValidateState(sState, asKeys):
    if sState is None:
        return False
    return sState in asKeys

def rd(dDict, skey):
    asKeys = dDict.keys()
    if skey in asKeys:
        return dDict[skey]
    else:
        return None

def IsWhiteListStr(sStr, sWhitelist):
    for sChar in sStr:
        if sChar not in sWhitelist:
            return False
    return True

def IsStrAllNum(sStr):
    return IsWhiteListStr(sStr.strip(), "0123456789")

def UserChoice(asOptionTxts, sText="choice:"):
    iChoiceIdx = -1
    bContinue = True
    while bContinue:
        choice = input("Choice:")
        if IsStrAllNum(choice):
            iChoiceIdx = int(choice)-1
            if iChoiceIdx < len(asOptionTxts):
                bContinue = False
    return asOptionTxts[iChoiceIdx]

def ProcessesDialog(dDialog):
    print(rd(dDialog, ghName) + ": "+rd(dDialog, ghExp))
    oDia = dialogDisplay.DialogDisplay()
    oDia.displayString("  "+rd(dDialog, ghTxt))

    sOptName = rd(dDialog, ghOptName)
    if sOptName is not None:
        print("\n\n"+sOptName)
    dOptions = rd(dDialog, ghOpts)
    if dOptions is not None:
        asOptionTxts = list(dOptions.keys())
        for i in range(len(asOptionTxts)):
            iI = i+1
            sOptionTxt = asOptionTxts[i]
            # print("   "+str(iI)+": "+
            print("   " + sOptionTxt)

        sOption = UserChoice(asOptionTxts)
        return dOptions[sOption]
    return None

def ProcessesDialogs(sDialogFile):
    dDialogs = DialogDict(sDialogFile)
    sState = gsStartingState
    asKeys = dDialogs.keys()
    while ValidateState(sState, asKeys):
        dDialog = dDialogs[sState]
        sState = ProcessesDialog(dDialog)

def Test():
    ProcessesDialogs(gsDialogFile)
    input("\n\npress enter to exit the game...")



