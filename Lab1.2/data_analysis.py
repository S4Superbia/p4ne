#!/usr/local/bin/python3

from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x): return x.value

wb = load_workbook('data_analysis_lab.xlsx')

sheet = wb['Data']
year = map(getvalue, sheet['A'][1:])
temp = map(getvalue, sheet['C'][1:])
ot = map(getvalue, sheet['D'][1:])

pyplot.plot(year, temp, label="metka")
pyplot.plot(year, ot, label="metka")

pyplot.show()