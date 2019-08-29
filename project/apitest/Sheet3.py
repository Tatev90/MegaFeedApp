import openpyxl

# Location of the file
from project.apitest.Sheet1 import list_of_lists

path = 'C:/Users/melikyan.tatevik/Desktop\megafeed_test_app/Soccer.xlsx'

# To open the workbook
wb = openpyxl.load_workbook(path)

# Get workbook active sheet
sheet = wb.active

wb.title = "Sheet3"

# Rows to lists
row_list2 = [row for row in sheet.values]
# print(row_list)

list_of_lists2 = [list(elem) for elem in row_list2]
print(list_of_lists)

for item in list_of_lists2:
    if item[3] == None:
        item[3] = ''

for item in list_of_lists2:
    if item[4] == None:
        item[4] = ''
