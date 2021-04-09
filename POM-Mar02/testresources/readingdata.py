from testresources import Constants
from testresources.readData import XLSReader

global xls
xls = XLSReader(Constants.XLS_PATH)

def getdata(testcasename):
    dataList = []

    teststartrowindex = 0
    while not(xls.getCellValue(Constants.DATASHEET, teststartrowindex, 0) == testcasename):
        teststartrowindex = teststartrowindex + 1

    colStartRowIndex = teststartrowindex + 1
    dataStartRowIndex = teststartrowindex + 2

    maxrows = 0
    try:
        while not(xls.checkCellEmpty(Constants.DATASHEET, dataStartRowIndex+maxrows, 0)):
            maxrows = maxrows + 1
    except Exception:
        pass

    maxcols = 0
    try:
        while not(xls.checkCellEmpty(Constants.DATASHEET, colStartRowIndex, maxcols)):
            maxcols = maxcols + 1
    except Exception:
        pass

    for rNum in range(dataStartRowIndex, dataStartRowIndex+maxrows):
        dataDictionary = {}
        for cNum in range(0, maxcols):
            datakey = xls.getCellValue(Constants.DATASHEET, colStartRowIndex, cNum)
            datavalue = xls.getCellValue(Constants.DATASHEET, rNum, cNum)
            dataDictionary[datakey] = datavalue
        dataList.append(dataDictionary)
    return dataList

def isRunnable(testcasename):
    rows = xls.getRowCount(Constants.TESTCASES)
    for rnum in range(0, rows):
        tname = xls.getCellValueByColName(Constants.TESTCASES, rnum, Constants.TCID_COL)
        if(testcasename == tname):
            runmode = xls.getCellValueByColName(Constants.TESTCASES, rnum, Constants.RUNMODE_COL)
            if(runmode == Constants.RUNMODE_Y):
                return True
            else:
                return False
