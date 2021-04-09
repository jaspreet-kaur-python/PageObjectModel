import xlrd


class XLSReader:
    def __init__(self,path):
        self.readxls = xlrd.open_workbook(path)

    def getCellValue(self, sheetname, rowIndex, colIndex):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.cell_value(rowIndex, colIndex)

    def getCellValueByColName(self, sheetname, rowIndex, colname):
        sheet = self.readxls.sheet_by_name(sheetname)
        for cnum in range(0, self.getColCount(sheetname)):
            extractedcolname = sheet.cell_value(0, cnum)
            if(extractedcolname == colname):
                celldata = sheet.cell_value(rowIndex, cnum)
                if(celldata!=''):
                    return celldata
                else:
                    return ''


    def getRowCount(self, sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.nrows

    def getColCount(self, sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.ncols

    def checkCellEmpty(self, sheetname, rowIndex, colIndex):
        sheet = self.readxls.sheet_by_name(sheetname)
        celltype = sheet.cell_type(rowIndex, colIndex)
        if(celltype==xlrd.XL_CELL_EMPTY):
            return True
        else:
            return False