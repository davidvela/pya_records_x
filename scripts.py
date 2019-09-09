import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

file = "db.xlsx"


def test1_readfile(): 
    sheetno = 0 
    # df = pd.read_excel(file, sheetname='db1')
    while(1)
        try
            df = pd.read_excel(file, sheetname=sheetno)#, index_col=0)
            sheetno = sheetno + 1
        except:
            break

    print("Column headings:"); print(df.columns)

def test2_readfile(): 
    xl = pd.ExcelFile(file)
    xl.sheet_names  # see all sheet names
    sheet_name = 1
    df1 = xl.parse(sheet_name)  # read a specific sheet to DataFrame


test1_readfile()
test2_readfile()
